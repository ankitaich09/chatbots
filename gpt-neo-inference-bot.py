from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the fine-tuned GPT-Neo model and tokenizer
model = AutoModelForCausalLM.from_pretrained("/data/ankit/gpt-neo-finetuned")
tokenizer = AutoTokenizer.from_pretrained("/data/ankit/gpt-neo-finetuned")

# Define a function to generate a response given an input text
def generate_response(input_text):
    # Tokenize the input text
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    # Generate a response using the model
    output = model.generate(input_ids, max_length=50, pad_token_id=tokenizer.eos_token_id)
    # Decode the generated output
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def main():
    while True:
        # Get user input
        user_input = input("You: ")
        # Exit loop if user types "exit"
        if user_input.lower() == "exit":
            break
        # Generate response
        response = generate_response(user_input)
        # Print response
        print("Bot:", response)

if __name__ == "__main__":
    main()
