# HumanEval-Test Benchmark

## Background

Writing tests is an essential aspect of sustainable software development and is considered a core skill for a competent Software Engineer (SWE). We wanted to understand how good are LLMs at generating effective test suites.

## Implementation Details

### Data

From the HumanEval dataset, we utilize the following data:
- `declaration`: The function declarations.
- `canonical_solution`: The reference solutions to the tasks.
- `test`: The tests written for these solutions.

For our benchmark, the combination of `declaration` and `canonical_solution` to prompt an LLM to generate a runnable test suite.

### Evaluation
To evaluate how well a model does, we simply look at the coverage of the generated test suites.

## How To Use
To generate the test evaluations for a given model, you can use the `generate.py` module like so:

```
python generate.py \
    --model_name=gpt-3.5-turbo \
    --model_output_prefix=gpt_35_turbo_v3 \
    --model_backend=openai \
    --num_tasks=5 \
    --prompt_strategy=PROMPT_STRATEGY_SELF_CORRECT
```
Once you have a `_test.py` file generated, you can run the coverage benchmark:
```
sh run_benchmark.sh generated-tests/gpt_35_turbo_test.py 
```

## Results
We report the coverage of the generated tests for the first 20 samples. `f` below is the number of failures.

| Model         | Base          | Self Correct    | Self Correct and Tool Use  |
|---------------|---------------|-----------------|----------------------------|
| GPT-3.5-Turbo | 73.13% (f=11) | 73.88% (f=18)   | 73.13% (f=11)              |
| Llama70b      | 73.88% (f=49) | 73.88% (f=49)   | 73.88% (f=49)              |
| Gemma-7b-it   | 70.14% (f=9)  | 44.77% (f=4)    | 44.77% (f=4)               |

- You can find the results for all the three models and all the three startegies in results/{gpt35, llama70b, gemma7bit}.

- Not all tests passed for any of the models.

- All models required some Human Edits but GPT-3.5 required the least and Gemma-7b the most. Note: these edits were mostly around the output language (for e.g., the non-code conversations) and there were no specific code that was human edited.

- It is quite impressive that Gemma-7b-it does comparably for the Base strategy. Using it where low latency test generation is critical seems quite plausible. (Although, ofcourse, this dataset is small and one can imagine the larger models doing better for tail end of the queries).

- It is quite impressive that they can generate such tests, however, to generate work-able code with just some vanilla prompting techniques seems brittle.

- The prompting self-correction/tool use does not add much value. We should be able to improve upon this and presents some opportunities. Why Gemma-7b-it does poorly on the tool use/self correction one is not completely clear and would require some further analysis.

## References

1. **HumanEval**: Evaluating Large Language Models Trained on Code
2. **HumanEval**: [Further documentation or repository]
3. **Coverage Tool**: [Documentation or tool link]