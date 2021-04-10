from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/service2', methods=['GET'])
def service2():
    number_string = ''
    randomnumber = random.randint(1,6)
    number_string += str(randomnumber)
    return f'{number_string}'


if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')