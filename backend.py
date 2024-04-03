from flask import Flask, render_template

app = Flask(__name__)

@app.route('/chatbot1.html')
def chatbot1():
    return render_template('chatbot1.html')

@app.route('/chatbot2.html')
def chatbot2():
    return render_template('chatbot2.html')

# Repeat the above for chatbot3, chatbot4, chatbot5

if __name__ == '__main__':
    app.run(debug=True)
