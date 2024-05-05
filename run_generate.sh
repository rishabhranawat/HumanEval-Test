# python generate.py \
#     --model_name=meta-llama/Llama-2-70b-chat-hf \
#     --model_output_prefix=results/llama270b/base \
#     --model_backend=together \
#     --num_tasks=20 \
#     --prompt_strategy=PROMPT_STRATEGY_BASE;

python generate.py \
    --model_name=meta-llama/Llama-2-70b-chat-hf \
    --model_output_prefix=results/llama270b/self_correct \
    --model_backend=together \
    --num_tasks=20 \
    --prompt_strategy=PROMPT_STRATEGY_SELF_CORRECT;

python generate.py \
    --model_name=meta-llama/Llama-2-70b-chat-hf \
    --model_output_prefix=results/llama270b/self_correct_and_verbal_rl \
    --model_backend=together \
    --num_tasks=20 \
    --prompt_strategy=PROMPT_STRATEGY_SELF_CORRECT_AND_VERBAL_RL;

python generate.py \
    --model_name=google/gemma-7b-it \
    --model_output_prefix=results/gemma7bit/base \
    --model_backend=together \
    --num_tasks=20 \
    --prompt_strategy=PROMPT_STRATEGY_BASE;

python generate.py \
    --model_name=google/gemma-7b-it \
    --model_output_prefix=results/gemma7bit/self_correct \
    --model_backend=together \
    --num_tasks=20 \
    --prompt_strategy=PROMPT_STRATEGY_SELF_CORRECT;

python generate.py \
    --model_name=google/gemma-7b-it \
    --model_output_prefix=results/gemma7bit/self_correct_and_verbal_rl \
    --model_backend=together \
    --num_tasks=20 \
    --prompt_strategy=PROMPT_STRATEGY_SELF_CORRECT_AND_VERBAL_RL;