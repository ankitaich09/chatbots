from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling, TextDataset
import pandas as pd
from datasets import Dataset

# Load your CSV file
df = pd.read_csv('substances.csv')

# Specify input and output column names
input_column = 'Questions'
output_column = 'Answers'

df = df.dropna(subset=[input_column, output_column])

# Create a tokenizer and model
cache_dir = '/data/ankit/model_caches'

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B", cache_dir=cache_dir)
# Add a padding token to the tokenizer
tokenizer.add_special_tokens({'pad_token': '[PAD]'})
# Create a new tokenizer object with the padding token
tokenizer.pad_token = '[PAD]'

model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B", cache_dir=cache_dir)

# Tokenize the data
tokenized_inputs = []
for index, row in df.iterrows():
    tokenized_input = tokenizer(row[input_column], truncation=True, return_tensors="pt")
    tokenized_inputs.append(tokenized_input)

# Prepare the dataset
dataset = Dataset.from_dict({"input_ids": [ti["input_ids"][0].tolist() for ti in tokenized_inputs],
                              "attention_mask": [ti["attention_mask"][0].tolist() for ti in tokenized_inputs]})

model.resize_token_embeddings(len(tokenizer))

# Define the training arguments
training_args = TrainingArguments(
    output_dir="/data/ankit/gpt-neo-finetuned",
    overwrite_output_dir=True,
    num_train_epochs=10,
    per_device_train_batch_size=1,
    save_steps=10_000,
    save_total_limit=2,
    prediction_loss_only=True,
)

# Instantiate the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
    train_dataset=dataset,
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained("/data/ankit/gpt-neo-finetuned")
tokenizer.save_pretrained("/data/ankit/gpt-neo-finetuned")
