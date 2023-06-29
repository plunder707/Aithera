from transformers import AutoModelForCausalLM, AutoTokenizer

def generate_with_bloom(prompt):
    model = AutoModelForCausalLM.from_pretrained("bigscience/bloom-1b3")
    tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom-1b3")
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text
