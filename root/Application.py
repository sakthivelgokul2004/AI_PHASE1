from flask import Flask, render_template,request,jsonify
from modal import infer,load_or_train_model
import re
app = Flask(__name__)
load_or_train_model()
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat",methods=['POST'])
def chatRequest():
    if request.method == 'POST':
        data = request.get_json()
        user_message = data['text'].lower()
        response=infer(user_message)
        response=re.sub(r'<startofstring>|<endofstring>', '', response)
        response = re.sub(r'<bot>:', '', response)
        return jsonify({'message': response})
    

if __name__ == "__main__":
    app.run(debug=True)
