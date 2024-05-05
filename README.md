# HumanEval-Test Benchmark

## Background

Writing tests is an essential aspect of sustainable software development and is considered a core skill for a competent Software Engineer (SWE). Despite its importance, there currently exist no robust benchmarks to evaluate the capability of Large Language Models (LLMs) in generating such tests effectively.

## Overview

The aim of this project is to introduce a new benchmark named the "HumanEval-Test" benchmark. Traditionally, the HumanEval dataset has been utilized to assess the proficiency of LLMs in coding tasks. Our objective is to repurpose this dataset to specifically evaluate the effectiveness of LLMs in creating high-quality software tests.

## Implementation Details

### Data Utilization

From the HumanEval dataset, we utilize the following columns:
- `declaration`: The function declarations.
- `canonical_solution`: The reference solutions to the tasks.
- `test`: The tests written for these solutions.

For our benchmark, the combination of `declaration` and `canonical_solution` (denoted as {C}) will serve as inputs, while `test` (denoted as {Yt}) will be used as the ground truth label.

### Model and Prediction

We will employ an LLM (denoted as {L}) to generate an output with a specific prompt {P}. The LLM's prediction should yield a comprehensive, executable test (denoted as {Yp}).

### Evaluation

The benchmark involves comparing the ground truth test {Yt} against the predicted test {Yp} using a defined Quality measuring function Q(Yi). The evaluation metric will be calculated as `Q(Yt) - Q(Yp)`.

#### Quality Definition (Q)

The effectiveness of the tests will be measured using the following criteria, implemented in two phases:
1. **Coverage (V0)** - Evaluates how well the tests cover the code.
2. **Ablation (V1)** - Assesses the impact of removing certain parts of the test on the overall test effectiveness.

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

## References

1. **HumanEval**: Evaluating Large Language Models Trained on Code
2. **HumanEval**: [Further documentation or repository]
3. **Coverage Tool**: [Documentation or tool link]