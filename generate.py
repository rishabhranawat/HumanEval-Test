import os
import time

from absl import app
from absl import flags
from openai import OpenAI
from datasets import load_dataset

import prompts
from prompts import GenerateTestSuitPrompt, GenerateSelfCorrectionPrompt

# Define flags
FLAGS = flags.FLAGS
flags.DEFINE_string('model_name', None,
                    'Name of the model to use for inference')
flags.DEFINE_string('model_output_prefix', None,
                    'Prefix for the output model files')
flags.DEFINE_string('model_backend', None,
                    'Backend for the model to use for inference')
flags.DEFINE_string('prompt_strategy', None,
                    'Prompt strategy to use for generating test cases')
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


def get_model_completion(client, model, prompt_strategy, function_code, output_test_class_name):
    """
    Gets a model completion from OpenAI.

    This function uses the OpenAI client to generate a completion from the given model and function code,
    and then formats the completion into a test class with the provided name.

    Args:
        client (openai.Client): An instance of the OpenAI client.
        model (str): The name of the model to use for the completion.
        function_code (str): The code of the function to generate a completion for.
        output_test_class_name (str): The name of the test class to format the completion into.

    Returns:
        response (openai.Response): The response from the model, containing the completion.
    """
    response = client.chat.completions.create(
        model=model,
        messages=GenerateTestSuitPrompt(output_test_class_name, function_code),
        temperature=1,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    test_suite_generated_response = response.choices[0].message.content
    print(f'Generated response {test_suite_generated_response}')
    if prompt_strategy == prompts.PROMPT_STRATEGY_SELF_CORRECT:
        self_corrected_response = client.chat.completions.create(
            model=model,
            messages=GenerateSelfCorrectionPrompt(
                test_suite_generated_response, output_test_class_name, function_code),
            temperature=1,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return self_corrected_response.choices[0].message.content
    return test_suite_generated_response


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
            function_code = declaration + '\n' + canonical_solution

            # get task_id in alphabetical form.
            test_class_name = f"Generated{int(task['task_id'].split('/')[1])}Test"

            # generate the actual completion using the specified model
            completion = get_model_completion(
                client, model_name, prompt_strategy, function_code, test_class_name)

            completion_indented = '\n'.join(
                line for line in completion.split('\n'))
            completion_indented = completion_indented.replace('```python', '')\
                .replace('```', '')\
                .replace("if __name__ == \'__main__\':", "")\
                .replace("if __name__ == \"__main__\":", "")\
                .replace("unittest.main()", "")\
                .replace("import unittest", "")

            generated_test_classes.append(completion_indented)
        except Exception as e:
            print(f"There was an exception, stopping at task {i}", e)
            break

    with open(f"{model_output_prefix}_test.py", 'w') as file:
        file.write('\n'.join(generated_test_classes))

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
