import json
from flask import Flask, render_template, request, make_response
from nlp_tools.textrank_utils import extract_abstracts

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/')
def demo():
    return render_template('da_demo.html')


@app.route('/textrank', methods=['POST', 'GET'])
def da():
    if request.method == 'POST':
        data = request.form
        # print data
        keysents = extract_abstracts(data['text'], sent_num=eval(data['sent_nums']))
        return make_response(json.dumps(keysents), 200)
    else:
        return 'get'


if __name__ == '__main__':
    app.run('0.0.0.0', port=9527)
