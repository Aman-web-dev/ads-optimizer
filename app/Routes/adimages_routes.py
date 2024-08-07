from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

FACEBOOK_URL = "https://graph.facebook.com/v20.0"

@app.route('/advideo', methods=['POST'])
def upload_video():
    try:
        if 'source' not in request.files or 'access_token' not in request.form or 'ad_account_id' not in request.form:
            return jsonify({'error': 'Missing required fields'}), 400

        params = request.files['params']
        access_token = request.form['access_token']
        ad_account_id = request.form['ad_account_id']

        url = f"{FACEBOOK_URL}/act_{ad_account_id}/advideos"
        files = {'source': (source.filename, source.stream, source.content_type)}
        data = {'access_token': access_token}

        response = requests.post(url, files=files, data=data)
        response.raise_for_status()  # Ensure that HTTP errors are raised

        return jsonify(response.json()), response.status_code

    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
@app.route('/advideo/<string:id>', methods=['DELETE'])
def delete_advideo(id):
    data = request.json
    access_token = data.get('access_token')

    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    url = f'{FACEBOOK_URL}/{id}'
    params = {'access_token': access_token}

    try:
        response = requests.delete(url, params=params)
        response.raise_for_status()
        return jsonify({'message': 'advideo deleted successfully'})
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)    