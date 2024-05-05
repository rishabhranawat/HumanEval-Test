from string import Template
from enum import Enum


class PrompStrategy(Enum):
    PROMPT_STRATEGY_BASE = 1
    PROMPT_STRATEGY_SELF_CORRECT = 2


class Prompt():
    def __init__(self, content: str):
        self.content = content

    def SubAndGet(self, context) -> list:
        return [
            {
                "role": "system",
                "content": "You are an expert test software engineer. You are not verbose and you ONLY very strictly only output code."
            },
            {
                "role": "user",
                "content": self.content.substitute(context)

            }
        ]


def BasePrompt() -> Template:
    return Prompt(Template("For the following Python function, \
                    create a unnittest class named $output_test_class_name that tests this function appropriately. \
                        Do not include the actual input function \n \
                        Do not include any import statements. \n \
                        Do not output anything other than the $output_test_class_name class definition itself.\
                        Do not include any comments. \n \
                        ```$function_code```"
                           ))


def GenerateSelfCorrectionPrompt() -> list:
    return Prompt(Template("Your previous response was $model_output. \n Can you double check if violated any of the \
            following rules and correct accordingly?: \n \
            1. Do not include any import statements. \n \
            2. Do not include any comments. \n \
            3. Do not output a if __main__ code block. \n \
            4. Do not output anything other than the $output_test_class_name class"))


def GetPromptChainForStrategy(strategy: PrompStrategy) -> list:
    if strategy == PrompStrategy.PROMPT_STRATEGY_BASE.name:
        return [BasePrompt()]
    elif strategy == PrompStrategy.PROMPT_STRATEGY_SELF_CORRECT.name:
        return [BasePrompt(), GenerateSelfCorrectionPrompt()]
    else:
        raise ValueError("Invalid strategy")
