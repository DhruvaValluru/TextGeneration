import os
import json

# Avoid TensorFlow-related issues
os.environ["TRANSFORMERS_NO_TF"] = "1"

from datasets import load_dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration, TrainingArguments, Trainer

# Load model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-small")
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")

# Preprocessing function (updated to match your dataset keys)
def preprocess(example):
    input_text = "Poster Request: " + example["prompt"]
    target_text = json.dumps(example["response"])  # Convert JSON object to string
    inputs = tokenizer(input_text, truncation=True, padding="max_length", max_length=512)
    labels = tokenizer(target_text, truncation=True, padding="max_length", max_length=512)
    inputs["labels"] = labels["input_ids"]
    return inputs

# Load and preprocess dataset
dataset = load_dataset("json", data_files="data/train.jsonl")["train"].map(preprocess)

# Training configuration
args = TrainingArguments(
    output_dir="outputs",
    evaluation_strategy="no",
    per_device_train_batch_size=4,
    num_train_epochs=5,
    save_total_limit=1,
    logging_steps=10,
)

# Trainer setup
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=dataset,
    tokenizer=tokenizer
)

# Train and save model
trainer.train()
model.save_pretrained("outputs")
tokenizer.save_pretrained("outputs")
