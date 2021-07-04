# 必要なモジュールの読み込み
from flask import Flask, jsonify, abort, make_response, request
# from api_analysis_get.app import lambda_handler as get_analysis
# from api_lock_validation_post.app import lambda_handler as lock_validation

import sys
import os

os.path.dirname(sys.modules['__main__'].__file__)

# Flaskクラスのインスタンスを作成
# __name__は現在のファイルのモジュール名

api = Flask(__name__)

"""
# This flask API is only used for the development stage.
# DO NOT deploy on production
"""

@api.route('/test/api/v1/softbank/business-logic/1/common/analysis',
           methods=['get'])  # TODO : Insert any URL
def get_analysis_get():
    # Get body, headers
    body = None
    headers = None

    # Insert necessary data to body
    data = {
        'body-json': body,
        'params': {
            'header': headers,
            "querystring": {
                "simulation_key": "test",
            },
        },
        'context': {
            'http-method': 'GET'
        }
    }

    result = data

    return make_response(jsonify(result))

# POSTの実装
@api.route('/test/api/v1/softbank/business-logic/1/common/lock',
           methods=['post'])  # TODO : Insert any URL
def lock_validation_post():
    # Get body, headers
    body = request.json
    headers = request.headers

    # Insert necessary data to body
    data = {
        'body-json': body,
        'params': {
            'header': headers
        },
        'context': {
            'http-method': 'POST'
        }
    }

    result = lock_validation(data)

    return make_response(jsonify(result))


# エラーハンドリング
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# ファイルをスクリプトとして実行した際に
# ホスト0.0.0.0, ポート3001番でサーバーを起動
if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8081)  # TODO : Insert any port number
