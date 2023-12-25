from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from process import search_vec

app = Flask(__name__)
CORS(app)

@app.route('/query', methods=['POST'])
@cross_origin()
def query():
    try:
        # Assuming the input is sent as JSON with the key 'input'
        input_text = request.json.get('input', '')
        docs = search_vec(input_text,"vault_chroma_db")
        response_data = [f"Source : {doc.metadata['source']}" 
                         + doc.page_content for doc in docs]
        

        return jsonify(response_data), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
