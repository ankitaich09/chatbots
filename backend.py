from flask import Flask

app = Flask(__name__)

@app.route('/chatbot1')
def chatbot1():
    # Run backend logic for Chatbot 1
    return "Chatbot 1 Backend"

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
