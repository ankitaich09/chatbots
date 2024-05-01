python gpt_j_sft_chatbot.py \
> --model_name_or_path google/flan-t5-large \
> --text_column Questions \
> --summary_column Answers \
> --num_train_epochs 30 \
> --output_dir /data/ankit/flan-finetuned/ \
> --per_device_train_batch_size 2 \
> --do_train \
> --overwrite_output_dir
