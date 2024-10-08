from flask import Flask,request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'
@app.route('/get_data', methods=['GET'])
def get_data():
    """
    API endpoint to get user details from LPU Live.
    """
    id = request.args.get('id')
    token = "9daacfb1e97a628660431de6c9442481"
    url = f"https://lpulive.lpu.in/fugu-api/api/chat/groupChatSearch?en_user_id={token}&search_text={id}&user_role=USER"
    
    try:
        response = requests.get(
            url, headers={"app_version": "1.0.0", "device_type": "WEB"}
        )
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        res_json = response.json()
        users = res_json.get("data", {}).get("users", [])

        if not users:
            return jsonify({"detail": "No user found."}), 404

        return users[0], 200
    except requests.exceptions.HTTPError as http_err:
        # Specific exception for HTTP errors
        return jsonify({"error": "HTTPError", "message": str(http_err)}), 500
    except requests.exceptions.RequestException as req_err:
        # Catch other request-related exceptions
        return jsonify({"error": "RequestException", "message": str(req_err)}), 500
    except Exception as e:
        # Generic exception handler
        return jsonify({"error": "Exception", "message": str(e)}), 500

@app.route('/about')
def about():
    return 'About'
if __name__ == '__main__':
    app.run(debug=True)

