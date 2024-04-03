from flask import Flask, request

app = Flask(__name__)

# Basic chatbot responses
chatbot_responses = {
    "hi": "Hello! How can I help you?",
    "how are you": "I'm a chatbot, so I'm always ready to assist you!",
    "bye": "Goodbye! Have a great day."
}

@app.route('/chatbot1', methods=['GET', 'POST'])
def chatbot1():
    if request.method == 'POST':
        user_input = request.form['user_input'].lower()
        if user_input in chatbot_responses:
            return chatbot_responses[user_input]
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"
    return """
    <form method="post">
        <label for="user_input">User Input:</label><br>
        <input type="text" id="user_input" name="user_input"><br>
        <input type="submit" value="Submit">
    </form>
    """
@app.route('/chatbot2')
def chatbot2():
    # Run backend logic for Chatbot 2
    return "Chatbot 2 Backend"

@app.route('/chatbot3')
def chatbot3():
    # Run backend logic for Chatbot 3
    return "Chatbot 3 Backend"

@app.route('/chatbot4')
def chatbot4():
    # Run backend logic for Chatbot 4
    return "Chatbot 4 Backend"

@app.route('/chatbot5')
def chatbot5():
    # Run backend logic for Chatbot 5
    return "Chatbot 5 Backend"

if __name__ == '__main__':
    app.run(debug=True)
