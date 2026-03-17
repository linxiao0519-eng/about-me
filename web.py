from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    link = "<h1>歡迎進入陳楷修的網站首頁!</h1>"
    link += "<a href=/mis>課程</a><hr>"
    link += "<a href=/today>今日日期</a><hr>"
    link += "<a href=/about>關於我</a><hr>"
    return link

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    now = year + "年" + month + "月" + day +"日"
    return render_template("today.html", datetime = str(now))

@app.route("/about")
def about():
    return render_template("mis2A.php")

if __name__ == "__main__":
    app.run(debug=True)
