from transformers import AutoModelForCausalLM, AutoTokenizer

def generate_with_gpt2(prompt):
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text