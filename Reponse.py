from flask import Flask, jsonify,request, render_template
from datetime import datetime
from uuid import uuid4
import json

req = {}
app = Flask(__name__)

# 요청을 처리하고 로깅하는 라우트
@app.route('/', methods=['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'DELETE'])
def index():
    request_info = {
        "url" : ""
    }
    # 요청 데이터를 웹 페이지에 표시
    return render_template('request_info.html', request_info=request_info)

    # 고유한 Url 생성 함수
@app.route('/generate', methods=['GET'])
def generate():
    unique_id = uuid4().hex
    new_url = f"/endpoint/{unique_id}"

    return jsonify({'url': new_url})

@app.route('/endpoint/<unique_id>', methods=['GET', 'POST', 'HEAD', 'OPTIONS'])
def handle_endpoint(unique_id):
    endpoint = f"endpoint/{unique_id}"
    now = datetime.now()
    print(endpoint)
    full_url = request.url
    method = request.method
    #headers = request.headers
    base_url = request.base_url
     #query_params = request.args
    data = request.data.decode('utf-8') if request.data else ''
    text_data = request.get_data(as_text=True)
    req[unique_id] = {
        'method': method,
        'headers' : {key: value for key, value in request.headers.items()},
        "url" :  full_url,
        "endurl" : endpoint,
        'base_url' : base_url,
        'query_params' : {key: value for key, value in request.args.items()},
        'data' : data,
        'text_data' : text_data,
        "time" : now.strftime("%Y-%m-%d %H:%M:%S"),
    }
       
        
    
    return jsonify(req[unique_id])

@app.route('/endpoint/<unique_id>/loglist', methods=['GET'])
def loglist(unique_id):
    if unique_id in req:
        return jsonify(req[unique_id])
    else :
        return jsonify({'error': 'No data found for this unique ID'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
