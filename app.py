from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('mongodb://test:test!@54.180.103.20', 27017)
db = client.user  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/robots.txt')
def robots():
    return render_template('robots.txt')

@app.route('/')
def home():
    return render_template('intro.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/loading')
def loading():
    return render_template('loading.html')


@app.route('/result/ISTJ')
def result_ISTG():
    return render_template('ISTJ.html')


@app.route('/result/ISFJ')
def result_ISFJ():
    return render_template('ISFJ.html')


@app.route('/result/INTJ')
def result_INTJ():
    return render_template('INTJ.html')


@app.route('/result/INFJ')
def result_INFJ():
    return render_template('INFJ.html')


@app.route('/result/ESTJ')
def result_ESTJ():
    return render_template('ESTJ.html')


@app.route('/result/ENTP')
def result_ENTP():
    return render_template('ENTP.html')


@app.route('/api/result', methods=['POST'])
def get_result():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    array = request.form.getlist('res[]')
    q1 = ""
    q2 = ""
    q3 = ""
    q4 = ""
    q5 = ""
    q6 = ""
    q7 = ""
    q8 = ""
    q9 = ""
    q10 = ""
    q11 = ""
    q12 = ""

    print(array)
    cnt_a = 0
    cnt_b = 0
    result = ""

    for index, value in enumerate(array):
        if value == 'A':  # a 선택 개수
            cnt_a += 1
        elif value == 'B':  # b 선택 개수
            cnt_b += 1

    # 구체적인 로직으로 변경해야해
    for index, value in enumerate(array):
        if index == 1:
            q1 = value
        elif index == 2:
            q2 = value
        elif index == 3:
            q3 = value
        elif index == 4:
            q4 = value
        elif index == 5:
            q5 = value
        elif index == 6:
            q6 = value
        elif index == 7:
            q7 = value
        elif index == 8:
            q8 = value
        elif index == 9:
            q9 = value
        elif index == 10:
            q10 = value
        elif index == 11:
            q11 = value
        elif index == 12:
            q12 = value
        elif value == 'M' or value == 'F':  # 성별
            sex = value
        else:  # 나이
            age = value

    if cnt_a <= 2:
        result = 'ISTJ'
    elif cnt_a <= 4:
        result = 'ISFJ'
    elif cnt_a <= 6:
        result = 'INFJ'
    elif cnt_a <= 8:
        result = 'INTJ'
    elif cnt_a <= 10:
        result = 'ESTJ'
    elif cnt_a <= 12:
        result = 'ENTP'

    doc = {
        'sex': sex,
        'age': age,
        'q1': q1,
        'q2': q2,
        'q3': q3,
        'q4': q4,
        'q5': q5,
        'q6': q6,
        'q7': q7,
        'q8': q8,
        'q9': q9,
        'q10': q10,
        'q11': q11,
        'q12': q12,
        'result': result,
    }
    db.user.insert_one(doc)

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
