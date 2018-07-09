import parse
from flask import abort, Flask, jsonify, request


app = Flask(__name__)


def is_request_valid(request):
    is_token_valid = request.form['token'] == '4z0DNKZgbNxVoiythlKxqfUc'
    is_team_id_valid = request.form['team_id'] == 'CBJ19H5K2'

    return is_token_valid and is_team_id_valid


@app.route('/', methods=['POST', 'GET'])
def start():
    return 'jopa'


@app.route('/hello-there', methods=['POST', 'GET'])
def hello_there():
    return jsonify(
        response_type='in_channel',
        text='<https://youtu.be/frszEJb0aOo|General Kenobi!>',
    )


@app.route('/mem', methods=['POST', 'GET'])
def send_mem():
    return jsonify(
        response_type="in_channel",
        text=parse.give_back_mem()
    )


@app.route('/bash', methods=['POST', 'GET'])
def send_mem():
    return jsonify(
        response_type="in_channel",
        text=parse.parse_random_bash_cit()
    )


@app.route('/jokes', methods=['POST', 'GET'])
def send_mem():
    return jsonify(
        response_type="in_channel",
        text=parse.parse_random_anekdot()
    )


@app.route('/habr', methods=['POST', 'GET'])
def send_mem():
    return jsonify(
        response_type="in_channel",
        text=parse.parse_popular_habr_posts()
    )


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
