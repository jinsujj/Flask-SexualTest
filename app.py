import datetime

from flask import Flask, render_template, jsonify, request, send_file
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('mongodb://jinsu:wlstncjs1!@54.180.103.20', 27017)
db = client.log  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.

@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml')


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

@app.route('/img/ISTJ')
def img_ISTJ():
    return send_file('./static/goza.png')



@app.route('/result/ISFJ')
def result_ISFJ():
    return render_template('ISFJ.html')

@app.route('/img/ISFJ')
def img_ISFJ():
    return send_file('./static/hut.png')



@app.route('/result/INTJ')
def result_INTJ():
    return render_template('INTJ.html')

@app.route('/img/INTJ')
def img_INTJ():
    return send_file('./static/heeek.png')



@app.route('/result/INFJ')
def result_INFJ():
    return render_template('INFJ.html')

@app.route('/img/INFJ')
def img_INFJ():
    return send_file('./static/hiiikkkkk.png')



@app.route('/result/ESTJ')
def result_ESTJ():
    return render_template('ESTJ.html')

@app.route('/img/ESTJ')
def img_ESTJ():
    return send_file('./static/guriguri.png')



@app.route('/result/ENTP')
def result_ENTP():
    return render_template('ENTP.html')

@app.route('/img/ENTP')
def img_ENTP():
    return send_file('./static/normal.png')


@app.route('/board')
def result_board():
    return render_template('board.html')


@app.route('/api/histogram', methods=['GET'])
def show_histogram():
    type = list(db.user.find({},{"_id":0 , "date":1,"sex":1}))
    print(type)

    day1 = 0
    day2 = 0
    day3 = 0
    day4 = 0
    day5 = 0
    day6 = 0
    day7 = 0
    other = 0

    today = datetime.date.today()
    day_1 = (datetime.date.today() - datetime.timedelta(1)).strftime("%Y-%m-%d")
    day_2 = (datetime.date.today() - datetime.timedelta(2)).strftime("%Y-%m-%d")
    day_3 = (datetime.date.today() - datetime.timedelta(3)).strftime("%Y-%m-%d")
    day_4 = (datetime.date.today() - datetime.timedelta(4)).strftime("%Y-%m-%d")
    day_5 = (datetime.date.today() - datetime.timedelta(5)).strftime("%Y-%m-%d")
    day_6 = (datetime.date.today() - datetime.timedelta(6)).strftime("%Y-%m-%d")
    day_7 = (datetime.date.today() - datetime.timedelta(7)).strftime("%Y-%m-%d")

    for index, value in enumerate(type):
        if value['date'][0:10] > day_1:
            day1 += 1
        elif value['date'][0:10] > day_2 and value['date'][0:10] <= day_1:
            day2 += 1
        elif value['date'][0:10] > day_3 and value['date'][0:10] <= day_2:
            day3 += 1
        elif value['date'][0:10] > day_4 and value['date'][0:10] <= day_3:
            day4 += 1
        elif value['date'][0:10] > day_5 and value['date'][0:10] <= day_4:
            day5 += 1
        elif value['date'][0:10] > day_6 and value['date'][0:10] <= day_5:
            day6 += 1
        elif value['date'][0:10] > day_7 and value['date'][0:10] <= day_6:
            day7 += 1
        else:
            other += 1

    return jsonify(
        {'result': 'success', 'day1': day1, 'day2': day2, 'day3': day3, 'day4': day4, 'day5': day5, 'day6': day6,'day7': day7, 'other' : other,
         'date1': day_1 , 'date2': day_2, 'date3': day_3, 'date4': day_4, 'date5' :day_5, 'date6' :day_6, 'date7': day_7})



@app.route('/api/list', methods=['GET'])
def show_graph():
    type = list(db.user.find({}, {'_id': False, 'result': 1}))
    ISTJ = 0
    ISFJ = 0
    INTJ = 0
    INFJ = 0
    ESTJ = 0
    ENTP = 0
    print(type)
    for index, value in enumerate(type):
        if value['result'] == 'ISTJ':
            ISTJ += 1
        elif value['result'] == 'ISFJ':
            ISFJ += 1
        elif value['result'] == 'INTJ':
            INTJ += 1
        elif value['result'] == 'INFJ':
            INFJ += 1
        elif value['result'] == 'ESTJ':
            ESTJ += 1
        else:
            ENTP += 1

    print(ISTJ)
    print(ISFJ)
    print(INTJ)
    print(INFJ)
    print(ESTJ)
    print(ENTP)
    return jsonify(
        {'result': 'success', 'ISTJ': ISTJ, 'ISFJ': ISFJ, 'INTJ': INTJ, 'INFJ': INFJ, 'ESTJ': ESTJ, 'ENTP': ENTP})


@app.route('/api/result', methods=['POST'])
def get_result():
    dt = datetime.datetime.now()
    date = str(dt)[:19]
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

    print(date)
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

    if q1 == 'A' and q3 == 'B' and q5 == 'B':
        result = 'ISTJ'
    elif q4 == 'A' and q7 == 'A' and q8 == 'B' and q10 == 'B':
        result = 'ISFJ'
    elif q1 == 'B' and q4 == 'B' and q7 == 'B' and q11 == 'B':
        result = 'INTJ'
    elif q5 == 'A' and q6 == 'B' and q7 == 'A' and q12 == 'A':
        result = 'INFJ'
    elif q1 == 'A' and q4 == 'B' and q8 == 'B' and q11 == 'A':
        result = 'ESTJ'
    elif q1 == 'A' and q4 == 'B' and q7 == 'B' and q8 == 'A':
        result = 'ENTP'

    if result == "":
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
        'date': date,
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
    app.run('127.0.0.1', port=5000, debug=True)
