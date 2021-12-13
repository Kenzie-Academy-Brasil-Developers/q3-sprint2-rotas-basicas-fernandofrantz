# Código do dev aqui

from flask import Flask
from datetime import datetime

app = Flask(__name__)
now = datetime.now()

@app.route('/')
def home():
    return {'data': 'Hello Flask!'}


@app.route('/current_datetime')
def datetime():
    current_datetime = now.strftime('%d')
    current_datetime += '/' + now.strftime('%m')
    current_datetime += '/' + now.strftime('%Y')

    current_datetime += ' ' + now.strftime('%H')
    current_datetime += ':' + now.strftime('%M')
    current_datetime += ':' + now.strftime('%S')

    current_datetime += ' ' + now.strftime('%P').upper()

    hr = now.strftime('%H')
    hr = int(hr)
    if hr > 18:
        message = 'Boa noite!'
    elif hr > 12 and hr < 18:
        message = 'Boa tarde!'
    else:
        message = 'Bom dia!!'

    message = str(message)

    return {'current_datetime': current_datetime, 'message': message}

# .