from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/service3', methods=['GET'])
def service3():
    fruit = ["apple ", "banana ", "strawberry "]
    fruit1 = random.choice(fruit)
    fruit2 = random.choice(fruit)
    fruit3 = random.choice(fruit)
    fruit_string = str(fruit1 + fruit2 + fruit3)
    return f'{fruit_string}'


if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')