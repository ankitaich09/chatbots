from transformers import GPTJForCausalLM, GPTJTokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling, TextDataset
import pandas as pd

# Load your CSV file
df = pd.read_csv('substances.csv')

# Specify input and output column names
input_column = 'Questions'
output_column = 'Answers'

# Create a tokenizer and model
tokenizer = GPTJTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
model = GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")

# Tokenize the data
def tokenize_function(examples):
    return tokenizer(examples[input_column], padding="max_length", truncation=True)

tokenized_datasets = df.map(tokenize_function, batched=True)

# Prepare the dataset
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Define the training arguments
training_args = TrainingArguments(
    output_dir="/data/ankit/gpt-j-finetuned",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=1,
    save_steps=10_000,
    save_total_limit=2,
    prediction_loss_only=True,
)

# Instantiate the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=tokenized_datasets["train"],
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained("/data/ankit/gpt-j-finetuned")
tokenizer.save_pretrained("/data/ankit/gpt-j-finetuned")
