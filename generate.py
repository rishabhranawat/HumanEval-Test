import os
import time

from absl import app
from absl import flags
from openai import OpenAI
from datasets import load_dataset

# Define flags
FLAGS = flags.FLAGS
flags.DEFINE_string('model_name', None,
                    'Name of the model to use for inference')
flags.DEFINE_string('model_output_prefix', None,
                    'Prefix for the output model files')
flags.DEFINE_string('model_backend', None,
                    'Backend for the model to use for inference')


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


def get_model_completion(client, model, function_code, output_test_class_name):
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
        messages=[
            {
                "role": "system",
                "content": "You are an expert test software engineer."
            },
            {
                "role": "user",
                "content": f"For the following Python function, \
                    create a unnittest class named {output_test_class_name} that tests this function appropriately. \
                        Do not include the actual input function \n \
                        Do not include any import statements. \n \
                        Do not output anything other than the {output_test_class_name} class definition itself.\
                        Do not include any comments. \n \
                        ```{function_code}```"
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content


def evaluate_model(model_name, model_output_prefix, model_backend):
    """
    Evaluates a model.

    This function evaluates the performance of a specified model using a specific backend. 
    The results are saved with a specified output prefix.

    Args:
        model_name (str): The name of the model to evaluate.
        model_output_prefix (str): The prefix for the output files where the results will be saved.
        model_backend (str): The backend to use for the evaluation (e.g., 'tensorflow', 'pytorch').

    Returns:
        None
    """

    dataset = load_dataset("THUDM/humaneval-x")
    client = construct_client(model_backend)

    generated_test_classes = []
    for i, task in enumerate(dataset['test']):
        if i % 10 == 0:
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
                client, model_name, function_code, test_class_name)

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
                   FLAGS.model_backend)


if __name__ == '__main__':
    app.run(main)
