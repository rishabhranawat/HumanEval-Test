PROMPT_STRATEGY_SELF_CORRECT = 'SELF_CORRECT'

def GenerateTestSuitPrompt(output_test_class_name: str, function_code: str) -> list:
    return [{
        "role": "system",
                "content": "You are an expert test software engineer. You are not verbose and you ONLY very strictly only output code."
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
    }]


def GenerateSelfCorrectionPrompt(prev_output: str, output_test_class_name: str, function_code: str) -> list:
    return [{
        "role": "system",
                "content": "You are an expert test software engineer. You are not verbose and you ONLY very strictly only output code."
    },
        {
        "role": "user",
        "content": f"Your previous response was {prev_output}. \n Can you double check if violated any of the \
            following rules and correct accordingly?: \n \
            1. Do not include any import statements. \n \
            2. Do not include any comments. \n \
            3. Do not output a if __main__ code block. \n \
            4. Do not output anything other than the {output_test_class_name} class"
    }]
