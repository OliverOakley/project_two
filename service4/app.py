from flask import Flask, Response, request, jsonify
import requests

app = Flask(__name__)

@app.route('/service4', methods=['GET'])
def service4():
    randomfruit = requests.get('http://service3:5003/service3').text
    diceroll = requests.get('http://service2:5002/service2').text
    win_list = ['banana banana ', 'apple apple ', 'melon melon ', 'banana banana banana ', 'apple apple apple ', 'melon melon melon ']
    prize_string = ' '
    if any(ele in randomfruit for ele in win_list) and diceroll == '1':
        prize_string = '100'
    elif any(ele in randomfruit for ele in win_list) and diceroll == '2':
        prize_string = '200'
    elif any(ele in randomfruit for ele in win_list) and diceroll == '3':
        prize_string = '300'
    elif any(ele in randomfruit for ele in win_list) and diceroll == '4':
        prize_string = '400'
    elif any(ele in randomfruit for ele in win_list) and diceroll == '5':
        prize_string = '500'
    elif any(ele in randomfruit for ele in win_list) and diceroll == '6':
        prize_string = '600'
    else:
        prize_string = '0'
    data = {"random_fruit": randomfruit, "dice_roll": diceroll, "prize": prize_string}
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=5004, debug=True, host='0.0.0.0')