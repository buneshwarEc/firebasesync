import firebase_admin
from firebase_admin import credentials , firestore


def fire():
    data={
    "type": "service_account",
    "project_id": "fir-sync-a3379",
    "private_key_id": "ce74ad8e70606cc0114ad5c87bd28e224d3aa144",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQD4mwINdgkP7JFA\nVQljTSBWf27XC/cBp10yIiIXIvauI5tNmyrTMSj7wvQjqHV5T/zOos33q6W4cZYL\neOk/XIoknjGiaeyEAi6wihGVy1QNeeDVtne4aeq09rkrvUYSk2OVIX/nUOHNg6Pv\nibZIE7OK+0vbt5qr0GrzYKty6MkzENqg8pVWRjOfLg8c+RyT40MpODyRc5vO2GVr\nRj/U7/uIeyPvc7YI1a/CZztBfgcH5BBVvv47ETyEsUlAy6ceW0qW6nWSCI/eCjv3\nfht9R+cmyVky2frvVm8CiXWzlcyysBu/eeQgWiIHj3l7LeUeDtgdD6+r86gTZfQF\nMy3GNb5bAgMBAAECggEAItEVVNdJZkkw/9Eo/cGTxtQVV4QIdYXVSoEh7xrpcJ1H\nUci/vaYZNvEoX0S8zF7vE+1pv8bymvCQHU6ItA6na4DFiMPMPkyj8ft+16YLQSaR\niLyuQE3XyLzzqp7ZDR7xMmCSWM3+DFnkVVbJstx3fP5mswB1ZpygwzGwW+kizHDI\nKIe6MOmcfkQasW8HKIKdnh/bqbE6PC7p3weqkE0av5FwEi0G+q0y141ysDgYqMUa\nUs+s+IKaIvlhG+lP0twvqhmiGzYkQmCKbsNb7mhluzJFPH29kf5E17u0KF5atdlV\n9m45GtQND0b4IHIj7sYOlVq8NGs9Rn4kR77T3e7pqQKBgQD+xXGBBZV2IgO2U8g7\nVNkSn0fcBPQUGYBTB9Hk/1VEEugpCiZBpc6uSF0CBWZNPG3rgt3PY0/iFwIS+qva\nn/+kohL58fLP0gxjKd/ElYjZVb0MnxyhOoVUyMRyVfDEaGxA8SalNlaR+HW8kPF7\n9+8SNDEJpjkf9/BKX2mKmfR3rQKBgQD5zfO2iNUu9MIKwfJlJAc9InJ9KOPxSS9U\naO8nsOrWynZToVY8eNo013qEuBsC1nd/pqvSov73evJO2QcadwNM5jfX3iWDtjYc\nIn+9zfSx/VcS/x1EvTd6qCGirn0W00lpEd+2X4bjvmZHwglW8oGK2e3vq8Ppbdvf\nr7kxKtHvJwKBgQCViMngEqjxF3HaWD6UJG7scTS6POYNzhH1qgdWQ0+GjxpYzC48\nJdezj6GXiBfNiYRy0PLjwMSoTRzYiuzHe1WPCdndflcoB39hzLgcKDCUb7BwcgtZ\nzoFnjBdRjIOupCO10lT+b3BMaOqh7Ojv/EwEAUIvCbNJwjr1TB8kTMyiWQKBgQDF\nXhekrM/i3bdCUKJ3jtO5VbIneVs/lJc0lgP+1CV3t1duFBbSiJm/DlDa86tDvreD\nv+gZ8HaKijVQXuDh5A5Tf8G3aOky+5AdApTzHfqrdoKJm89ANE/VNWn94ucqVZ22\nykx7B1bIMfMV1xUSAWCgmDcKGigcEpSaU3h6hF6CGQKBgQDQ4rayPDSS0YWzgypm\nMQmkFkKdnKfCDa5AZBZZrPxJIi/2Sf9sG4JuCO3lt49VqryUao/Ga0awg9diHxG3\nPxVjd8d9CZ47KR7isLezsZ4XoHE3m75cQiBGrnR2vdfB+OXbZK4jHkaP8b8Dkis/\nhD57CMXmv+M17v0Ry7ZiWhnqaw==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-m10u0@fir-sync-a3379.iam.gserviceaccount.com",
    "client_id": "102592241655082055308",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-m10u0%40fir-sync-a3379.iam.gserviceaccount.com"
    }

    cred = credentials.Certificate(data)
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    print(db)
    id=2
    raw_notification={"name":"bunny","roll":"121"}
    print(raw_notification)
    b=db.collection('notifications').document(str(id)).create(raw_notification)
    print(b)