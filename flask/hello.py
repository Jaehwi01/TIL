from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/python')
def python():
    return 'python is fun!'

@app.route('/dictionary/<string:word>')  
def dictionary(word):
    diction = {
        'apple':'사과', 'banana':'바나나',
        'pear':'배', 'melon':'메롱', 'orange':'오렌지'
    }
    result = diction.get(word,'나만의 단어장에 없는 단어입니다!')

    return f'{word}은(는) {result}!'