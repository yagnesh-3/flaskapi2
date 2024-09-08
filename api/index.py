from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'
@app.route('/get_data', methods=['GET'])
def get_data():
    """
    API endpoint to get user details from LPU Live.
    """
    id = "12223854"
    token = "9daacfb1e97a628660431de6c9442481"
    url = f"https://lpulive.lpu.in/fugu-api/api/chat/groupChatSearch?en_user_id={token}&search_text={id}&user_role=USER"
    return {"id" : id}

@app.route('/about')
def about():
    return 'About'
