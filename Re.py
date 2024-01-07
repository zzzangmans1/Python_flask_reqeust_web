from flask import Flask, jsonify, render_template
from datetime import datetime
from uuid import uuid4



app = Flask(__name__)

# 요청을 처리하고 로깅하는 라우트
@app.route('/', methods=['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'DELETE'])
def index():
    now = datetime.now()
    request_info = {
        "random_endpoint" : generate(),
        "time" : now.strftime("%Y-%m-%d %H:%M:%S")
    }
    # 요청 데이터를 웹 페이지에 표시
    return render_template('request_info.html', request_info=request_info)

    # 고유한 Url 생성 함수
@app.route('/generate', methods=['GET'])
def generate():
    new_url = f"http://{uuid4().hex}.lwj"
    return jsonify(url=new_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
