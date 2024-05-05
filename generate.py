import os
import time

from absl import app
from absl import flags
from openai import OpenAI
from datasets import load_dataset

import prompts
import executor
import utils

# Define flags
FLAGS = flags.FLAGS
flags.DEFINE_string('model_name', None,
                    'Name of the model to use for inference')
flags.DEFINE_string('model_output_prefix', None,
                    'Prefix for the output model files')
flags.DEFINE_string('model_backend', None,
                    'Backend for the model to use for inference')
flags.DEFINE_enum('prompt_strategy', default='PROMPT_STRATEGY_BASE',
                  enum_values=prompts.PrompStrategy.__members__.keys(), help='Choose a prompt strategy')
flags.DEFINE_integer(
    'num_tasks', 10, 'Number of HumanEval examples to generate data for')


def construct_client(model_backed):
    """
    Constructs an OpenAI client.

    This function initializes an OpenAI client with the appropriate model backend.
    Returns:
        client (openai.Client): An instance of the OpenAI client.
    """
    if model_backed == 'openai':
        return OpenAI(
            api_key=os.environ.get("OPEN_AI_API_KEY"),
            base_url="https://api.openai.com/v1",
        )
    elif model_backed == 'together':
        return OpenAI(
            api_key=os.environ.get("TOGETHER_API_KEY"),
            base_url="https://api.together.xyz/v1",
        )
    else:
        raise ValueError("Invalid model backend specified.")


def execute_chain(client, model, prompt_strategy, chain_context) -> str:
    """
    Executes a chain of prompts and returns the model's output.

    This function takes a client, a model, a prompt strategy, and a chain context as input.
    It uses the client and model to execute the prompt strategy within the given chain context,
    and returns the final output of the model.

    Args:
        client (openai.Client): An instance of the OpenAI client.
        model (str): The name of the model to use for the completion.
        prompt_strategy (str): The strategy to use for generating prompts.
        chain_context (str): The context in which to execute the chain of prompts.

    Returns:
        str: The final output of the model after executing the chain of prompts.
    """
    prompt_chain: list[prompts.Prompt] = prompts.GetPromptChainForStrategy(
        prompt_strategy)

    chain_context["model_output"] = None
    for prompt in prompt_chain:
        input = prompt.SubAndGet(chain_context)
        output = client.chat.completions.create(
            model=model,
            messages=input,
        )
        chain_context["model_output"] = output.choices[0].message.content
    return chain_context["model_output"]


def evaluate_model(model_name, model_output_prefix, model_backend,
                   prompt_strategy=None,
                   num_tasks=10):
    """
    Evaluates a model.

    This function evaluates the performance of a specified model using a specific backend. 
    The results are saved with a specified output prefix.

    Args:
        model_name (str): The name of the model to evaluate.
        model_output_prefix (str): The prefix for the output files where the results will be saved.
        model_backend (str): The backend to use for the evaluation (e.g., 'tensorflow', 'pytorch').
        num_tasks (int): The number of tasks to evaluate the model on.

    Returns:
        None
    """

    dataset = load_dataset("THUDM/humaneval-x")
    client = construct_client(model_backend)

    generated_test_classes = []
    for i, task in enumerate(dataset['test']):
        if i >= num_tasks:
            print('Generated Data for {num_tasks} tasks. Exiting')
            break
        if i % 5 == 0:
            time.sleep(10)
            print('Sleeping for 10s to avoid getting rate limited.')
        try:
            print(f"Running HumanEval-Test generation for {i+1}")

            declaration = task['declaration']
            canonical_solution = task['canonical_solution']
            indented_solution = '\n'.join(
                '    ' + line for line in canonical_solution.split('\n'))
            function_code = declaration + indented_solution

            # get task_id in alphabetical form.
            test_class_name = f"Generated{int(task['task_id'].split('/')[1])}Test"

            # generate the actual completion using the specified model
            chain_context = {
                "function_code": function_code,
                "output_test_class_name": test_class_name,
            }
            completion = execute_chain(
                client, model_name, prompt_strategy, chain_context)

            completion_indented = utils.format_generated_output(completion)

            if prompt_strategy == prompts.PrompStrategy.PROMPT_STRATEGY_SELF_CORRECT_AND_VERBAL_RL.name:
                passed, result = executor.execute(
                    model_output_prefix, function_code, completion_indented)
                print(f"Executing program: {passed}, {result}")
                if not passed:
                    chain_context["program_output"] = result
                    completion = execute_chain(
                        client,
                        model_name,
                        "PROMPT_STRATEGY_VERBAL_RL",
                        chain_context
                    )
                    completion_indented = utils.format_generated_output(
                        completion)

            generated_test_classes.append(completion_indented)
        except Exception as e:
            print(f"There was an exception, stopping at task {i}", e)
            break

    with open(f"{model_output_prefix}_test.py", 'w') as file:
        file.write('import unittest\n')
        file.write('from unittest import TestCase\n')
        file.write('\n'.join(generated_test_classes))
        file.write('\n')

    return "Completed writing generated code to files."


def main(argv):
    if (FLAGS.model_name is None or
            FLAGS.model_output_prefix is None or
            FLAGS.model_backend is None):
        raise app.UsageError(
            "Both --model_name and \
                    --model_output_prefix and \
                    --model_backend must be specified.")

    print(
        f"Running Inference \
                for Model: {FLAGS.model_name} and \
                for output prefix: {FLAGS.model_output_prefix}")

    evaluate_model(FLAGS.model_name, FLAGS.model_output_prefix,
                   FLAGS.model_backend, FLAGS.prompt_strategy, FLAGS.num_tasks)


if __name__ == '__main__':
    app.run(main)
