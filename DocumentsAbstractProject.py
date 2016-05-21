import json
from flask import Flask, render_template, request, make_response
from nlp_tools.log_utils import da_logger
from nlp_tools.textrank_utils import extract_abstracts

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/da_demo')
def demo():
    da_logger.info('PV from %s' % (request.remote_addr))
    return render_template('da_demo.html')


@app.route('/da_demo/textrank', methods=['POST', 'GET'])
def da():
    if request.method == 'POST':
        data = request.form
        # print data
        da_logger.info(
            'request from %s, request abstract nums=%s, text:\n%s' % (
                request.remote_addr, eval(data['sent_nums']), data['text']))
        keysents = extract_abstracts(data['text'], sent_num=eval(data['sent_nums']))
        return make_response(json.dumps(keysents), 200)
    else:
        return 'get'


if __name__ == '__main__':
    app.run('0.0.0.0', port=9527)
