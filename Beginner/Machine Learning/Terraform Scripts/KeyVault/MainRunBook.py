# %% [markdown]
"""
# Terraform Generator with Dependency Resolution
"""

# %%
# STEP 1: Complete clean installation
!pip uninstall -y torch torchvision torchaudio transformers sentence-transformers peft accelerate
!rm -rf /usr/local/lib/python3.11/dist-packages/transformers*

# Install compatible versions
!pip install -q torch==2.0.1+cu118 torchvision==0.15.2+cu118 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
!pip install -q transformers==4.41.0 datasets==2.13.1 peft==0.4.0 accelerate==0.20.3 sentence-transformers==3.4.1

# Restart runtime
from IPython.display import clear_output
clear_output()
print("Please go to Runtime > Restart runtime now, then continue")

# %% [markdown]
"""
After restarting runtime, continue below
--------------------------------------
"""

# %%
# STEP 2: Verify installations
import torch
print(f"PyTorch: {torch.__version__}")
print(f"CUDA: {torch.version.cuda}")
print(f"GPU: {torch.cuda.is_available()}")

from transformers import __version__ as tf_version
from sentence_transformers import __version__ as st_version
print(f"Transformers: {tf_version}")  # Should be 4.41.0
print(f"Sentence-Transformers: {st_version}")  # Should be 3.4.1

# %%
# STEP 3: Main imports
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    default_data_collator
)
from peft import LoraConfig, get_peft_model
import json

# %%
# Load dataset
def load_jsonl(file_path):
    with open(file_path, 'r') as f:
        return [json.loads(line) for line in f]

data = load_jsonl("terraform_keyvault_finetuning.jsonl")

# %%
# Initialize tokenizer
MODEL_NAME = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token

# %%
# Tokenize data
def tokenize_function(examples):
    text = examples["prompt"] + " " + examples["completion"] + tokenizer.eos_token
    return tokenizer(
        text,
        truncation=True,
        max_length=512,
        padding="max_length"
    )

tokenized_data = [tokenize_function(d) for d in data]

# %%
# Model setup with correct LoRA targets for DistilGPT-2
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

peft_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["c_attn"],  # Correct module for DistilGPT-2
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, peft_config)
model.to('cuda' if torch.cuda.is_available() else 'cpu')

# %%
# Training
training_args = TrainingArguments(
    output_dir="./output",
    per_device_train_batch_size=4,
    num_train_epochs=3,
    learning_rate=5e-5,
    logging_steps=10,
    save_strategy="no",
    report_to="none",
    fp16=torch.cuda.is_available(),
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_data,
)

print("Training...")
trainer.train()

# %%
# Test generation
def generate(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_length=512,
        temperature=0.7,
        do_sample=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generate("Write Terraform to fetch VM credentials from Key Vault:"))