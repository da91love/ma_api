# 必要なモジュールの読み込み
from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS

from api_auth_get.app import lambda_handler as get_auth
from api_auth_delete.app import lambda_handler as delete_auth
from api_bookmark_put.app import lambda_handler as put_bookmark
from api_bookmark_get.app import lambda_handler as get_bookmark
from api_valuation_put.app import lambda_handler as put_valuation
from api_valuation_get.app import lambda_handler as get_valuation
from api_comp_tg_grp_put.app import lambda_handler as put_comp_tg_grp
from api_comp_tg_grp_get.app import lambda_handler as get_comp_tg_grp

import sys
import os

os.path.dirname(sys.modules['__main__'].__file__)

# Flaskクラスのインスタンスを作成
# __name__は現在のファイルのモジュール名

api = Flask(__name__)
cors = CORS(api)

"""
# This flask API is only used for the development stage.
# DO NOT deploy on production
"""

@api.route('/dev/api/ma-api/v1/front/comp-tg-grp',
           methods=['get'])  # TODO : Insert any URL
def comp_tg_grp_get():
    body = None
    headers = request.headers
    user_id = request.args.get('userId')
    auth_id = request.args.get('authId')

    # Insert necessary data to body
    data = {
        'body-json': body,

        'params': {
            'header': headers,
            "querystring": {
                "user_id": user_id,
                "auth_id": auth_id,
            },
        },
        'context': {
            'http-method': 'GET'
        }
    }

    result = get_comp_tg_grp(data)

    return make_response(jsonify(result))


@api.route('/dev/api/ma-api/v1/front/comp-tg-grp',
           methods=['put'])  # TODO : Insert any URL
def comp_tg_grp_put():
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
            'http-method': 'PUT'
        }
    }

    result = put_comp_tg_grp(data)

    return make_response(jsonify(result))

@api.route('/dev/api/ma-api/v1/front/valuation',
           methods=['get'])  # TODO : Insert any URL
def valuation_get():
    body = None
    headers = request.headers
    user_id = request.args.get('userId')
    auth_id = request.args.get('authId')

    # Insert necessary data to body
    data = {
        'body-json': body,

        'params': {
            'header': headers,
            "querystring": {
                "user_id": user_id,
                "auth_id": auth_id,
            },
        },
        'context': {
            'http-method': 'GET'
        }
    }

    result = get_valuation(data)

    return make_response(jsonify(result))


@api.route('/dev/api/ma-api/v1/front/valuation',
           methods=['put'])  # TODO : Insert any URL
def valuation_put():
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
            'http-method': 'PUT'
        }
    }

    result = put_valuation(data)

    return make_response(jsonify(result))

@api.route('/dev/api/ma-api/v1/front/bookmark',
           methods=['get'])  # TODO : Insert any URL
def bookmark_get():
    body = None
    headers = request.headers
    user_id = request.args.get('userId')
    auth_id = request.args.get('authId')

    # Insert necessary data to body
    data = {
        'body-json': body,

        'params': {
            'header': headers,
            "querystring": {
                "user_id": user_id,
                "auth_id": auth_id,
            },
        },
        'context': {
            'http-method': 'GET'
        }
    }

    result = get_bookmark(data)

    return make_response(jsonify(result))


@api.route('/dev/api/ma-api/v1/front/bookmark',
           methods=['put'])  # TODO : Insert any URL
def bookmark_put():
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
            'http-method': 'PUT'
        }
    }

    result = put_bookmark(data)

    return make_response(jsonify(result))

@api.route('/dev/api/ma-api/v1/front/auth',
           methods=['delete'])  # TODO : Insert any URL
def auth_delete():
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
            'http-method': 'DELETE'
        }
    }

    result = delete_auth(data)

    return make_response(jsonify(result))


@api.route('/dev/api/ma-api/v1/front/auth',
           methods=['get'])  # TODO : Insert any URL
def auth_get():
    # Get body, headers
    body = None
    headers = request.headers
    user_id = request.args.get('userId')
    pw = request.args.get('pw')

    # Insert necessary data to body
    data = {
        'body-json': body,

        'params': {
            'header': headers,
            "querystring": {
                "user_id": user_id,
                "pw": pw,
            },
        },
        'context': {
            'http-method': 'GET'
        }
    }

    result = get_auth(data)

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
