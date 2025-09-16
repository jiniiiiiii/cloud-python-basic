from flask import Flask

app = Flask(__name__)   # Flask 객체 선언 
@app.route("/")
def hom():
    return "<h1>안녕하세요, 웹 서버 프로그래밍을 시작합니다. </h1>"

if __name__=="__main__":
    app.run(debug=True)