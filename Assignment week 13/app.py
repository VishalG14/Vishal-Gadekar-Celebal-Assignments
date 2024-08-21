from flask import Flask, request, jsonify
import openai

app = Flask(__name__)


openai.api_key = 'fabc328bf64e4c82b91b2429c03b988f'

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    response = openai.Completion.create(
        engine='text-davinci-003',  
        prompt=prompt,
        max_tokens=100
    )

    return jsonify({'text': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
