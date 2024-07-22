from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Словарь для хранения сообщений по вкладкам
messages = {
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_messages/<tab_number>', methods=['GET'])
def get_messages(tab_number):
    return jsonify(messages[tab_number])

@app.route('/send_message', methods=['POST'])
def send_message():
    tab_number = request.form['tab_number']
    message = request.form['message']
    messages[tab_number].append(message)
    return 'Message sent'

if __name__ == '__main__':
    app.run()