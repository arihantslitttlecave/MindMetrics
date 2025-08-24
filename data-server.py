from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

EXCEL_FILE = 'game_data.xlsx'

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    if not data:
        return jsonify({'status': 'error', 'message': 'No data received'}), 400

    new_data = pd.DataFrame([{
        'Name': data.get('Name'),
        'Age': data.get('Age'),
        'Gender': data.get('Gender'),
        'Time': data.get('Time'),
        'Matches': data.get('Matches'),
        'Mismatches': data.get('Mismatches'),
        'Attempts': data.get('Attempts'),
        'Accuracy': data.get('Accuracy'),
        'Status': data.get('Status')
    }])

    if os.path.exists(EXCEL_FILE):
        existing = pd.read_excel(EXCEL_FILE)
        df = pd.concat([existing, new_data], ignore_index=True)
    else:
        df = new_data

    df.to_excel(EXCEL_FILE, index=False)
    return jsonify({'status': 'success', 'message': 'Saved to Excel'}), 200

if __name__ == '__main__':
    app.run(port=5000)
