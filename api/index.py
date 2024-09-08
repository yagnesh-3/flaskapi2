from flask import Flask
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
    id = "12224152"
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

        return jsonify({"users": users}), 200

    except:
        return "error-yagnesh"

@app.route('/about')
def about():
    return 'About'
