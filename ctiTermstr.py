!pip install datasets
!pip install peft
!pip install transformers

import os
import torch
from transformers import MBartForConditionalGeneration, MBartTokenizer, Seq2SeqTrainer, Seq2SeqTrainingArguments
from datasets import Dataset, DatasetDict
from peft import LoraConfig, get_peft_model
import pandas as pd

df = pd.read_csv('/content/Siber_Guvenlik_Terim_Karsiliklari_duzenlenmis.csv', delimiter=';')

dataset = Dataset.from_pandas(df[['English Term', 'Turkish Term']])

split_dataset = dataset.train_test_split(test_size=0.1)
tokenized_datasets = DatasetDict({
    'train': split_dataset['train'],
    'validation': split_dataset['test']
})


model_name = 'facebook/mbart-large-50-many-to-many-mmt'
tokenizer = MBartTokenizer.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)


lora_config = LoraConfig(
    r=8,                       
    lora_alpha=32,        
    target_modules=["q_proj", "v_proj"],  
    lora_dropout=0.1,         
    bias="none",                
    task_type="SEQ_2_SEQ_LM"  
)
model = get_peft_model(model, lora_config)

def preprocess_function(examples):
    inputs = examples['English Term']
    targets = examples['Turkish Term']

    model_inputs = tokenizer(inputs, max_length=128, truncation=True, padding='max_length')
    labels = tokenizer(targets, max_length=128, truncation=True, padding='max_length').input_ids

    labels = [[(label if label != tokenizer.pad_token_id else -100) for label in labels_seq] for labels_seq in labels]

    model_inputs["labels"] = labels
    return model_inputs

tokenized_datasets = tokenized_datasets.map(preprocess_function, batched=True)

training_args = Seq2SeqTrainingArguments(
    output_dir='./results',               
    evaluation_strategy='epoch',          
    learning_rate=3e-5,                   
    per_device_train_batch_size=4,        
    per_device_eval_batch_size=4,         
    num_train_epochs=5,                  
    weight_decay=0.01,                   
    save_total_limit=2,                  
    logging_dir='./logs',                 
    logging_steps=10,                  
    fp16=True,                           
    gradient_accumulation_steps=2,        
    lr_scheduler_type='cosine',         
    warmup_steps=500,                    
)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['validation'],
    tokenizer=tokenizer,
)

trainer.train()

model_name = './fine-tuned-model'
tokenizer = MBartTokenizer.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

eval_results = trainer.evaluate()
print(eval_results)
