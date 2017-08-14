import hashlib
import hmac

from flask import Flask, render_template

app = Flask(__name__)
ID_VERIFICATION_SECRET = ""
APP_ID = ""

def get_user_hash(user):
    data = user['email']
    result = hmac.new(ID_VERIFICATION_SECRET, data, hashlib.sha256).hexdigest()
    return result
    
@app.route('/')
def index():
    user = {}
    user['email'] = 'id_ver_test@example.com'
    user['name'] = "Guy McMan"
    user['user_hash'] = get_user_hash(user)

    return render_template('index.html', user=user, app_id=APP_ID)     

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)  
    
