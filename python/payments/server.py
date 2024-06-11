# payments/server.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/payment_notification', methods=['POST'])
def payment_notification():
    data = request.json
    # Process payment notification
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
