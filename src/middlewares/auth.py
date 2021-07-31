import requests
from functools import wraps
from flask import request, jsonify

def auth_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'NOT_AUTHENTICATE'})
        if token:
            try:
                r = requests.post('http://10.98.22.58:3000/auth',
                    json={
                        'query':"""
                            query Request {
                                Me{
                                    id
                                    email
                                    firstname
                                    lastname
                                    phoneNumber
                                }
                            }
                        """
                    },
                    headers={
                        "Authorization": token
                    }
                )
                result = r.json()
                if not result['data']:
                    return jsonify({'error': result['errors'][0]['message']})
            except:
                return jsonify({'error': 'NOT_AUTHENTICATE'})
        return f(*args, **kwargs)
    return decorator