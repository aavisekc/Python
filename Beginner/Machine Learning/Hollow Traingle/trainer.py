from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import load_dataset
import torch

# Load dataset
dataset = load_dataset("json", data_files="hollow_triangle_data.jsonl", split="train")

# Load tokenizer and model
model_id = "microsoft/phi-3-mini-128k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto", trust_remote_code=True)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Tokenization function
def tokenize(example):
    tokenized = tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized

tokenized_dataset = dataset.map(tokenize, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir="./phi3_triangle_model",
    overwrite_output_dir=True,
    per_device_train_batch_size=4,
    max_steps=300,  # Try increasing for better results
    logging_steps=10,
    save_strategy="no",
    report_to="none"
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

# Train
print("🚀 Starting training with Phi-3 Mini...")
trainer.train()
print("✅ Training complete!")

# Save model
model.save_pretrained("./phi3_triangle_model")
tokenizer.save_pretrained("./phi3_triangle_model")

# Generation
prompt = (
    "Write a Python function to print a hollow triangle using stars (*). "
    "The function should take height as input and print the triangle accordingly.\n\n"
    "Python Code:\n"
)

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=100,
    do_sample=True,
    top_k=50,
    top_p=0.9,
    temperature=0.7,
    pad_token_id=tokenizer.eos_token_id
)

print("\n🧠 Generated output:\n")
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
print("\n✅ Phi-3 Mini model and tokenizer saved successfully!")
print("✅ Model training and generation complete!")
print("✅ Model and tokenizer saved successfully!")