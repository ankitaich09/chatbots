from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the fine-tuned GPT-Neo model and tokenizer
model = AutoModelForCausalLM.from_pretrained("/data/ankit/gpt-neo-finetuned")
tokenizer = AutoTokenizer.from_pretrained("/data/ankit/gpt-neo-finetuned")
# Initialize dialogue history
dialogue_history = []

# Define a function to generate a response given an input text
def generate_response(input_text):
    global dialogue_history
    # Add user input to dialogue history
    dialogue_history.append("User: " + input_text)
    # Tokenize the dialogue history
    input_ids = tokenizer.encode("\n".join(dialogue_history[-3:]), return_tensors="pt")
    # Generate a response using the model
    output = model.generate(input_ids, max_new_tokens=500, pad_token_id=tokenizer.eos_token_id)
    # Decode the generated output
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    # Add bot response to dialogue history
    dialogue_history.append("Bot: " + response)
    return response

def main():
    global dialogue_history
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
