from cs50 import *
from flask import *
from datetime import datetime
from jinja2 import *
app = Flask(__name__, template_folder="template")
db = SQL("sqlite:///project.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tanchau", methods=["GET","POST"])
def tanchau():
    if request.method == "POST":
        name = request.form.get("ten")
        comment = request.form.get("comment")
        diadiem = "TanChau"
        now = datetime.now()
        now = now.strftime("%Y/%m/%d %H:%M:%S")
        db.execute("INSERT INTO comments(diadiem, username, comment, date) VALUES(?, ?, ?, ?)", diadiem, name, comment, now)
        comments = db.execute("SELECT * FROM comments WHERE diadiem = ?;", diadiem)
        count = db.execute("SELECT COUNT(username) as count FROM comments WHERE diadiem = ?", diadiem)
        return render_template("TanChau.html", comments = comments, count = count)
    else:
        diadiem = "TanChau"
        comments = db.execute("SELECT * FROM comments WHERE diadiem = ?;", diadiem)
        count = db.execute("SELECT COUNT(username) as count FROM comments WHERE diadiem = ?", diadiem)
        return render_template("TanChau.html", comments = comments, count = count)



@app.route("/chaudoc", methods=["GET","POST"])
def chaudoc():
    if request.method == "POST":
        name = request.form.get("ten")
        comment = request.form.get("comment")
        diadiem = "ChauDoc"
        now = datetime.now()
        now = now.strftime("%Y/%m/%d %H:%M:%S")
        db.execute("INSERT INTO comments(diadiem, username, comment, date) VALUES(?, ?, ?, ?)", diadiem, name, comment, now)
        comments = db.execute("SELECT * FROM comments WHERE diadiem = ?;", diadiem)
        count = db.execute("SELECT COUNT(username) as count FROM comments WHERE diadiem = ?", diadiem)
        return render_template("ChauDoc.html", comments = comments, count = count)
    else:
        diadiem = "ChauDoc"
        comments = db.execute("SELECT * FROM comments WHERE diadiem = ?;", diadiem)
        count = db.execute("SELECT COUNT(username) as count FROM comments WHERE diadiem = ?", diadiem)
        return render_template("ChauDoc.html", comments = comments, count = count)


@app.route("/tinhbien", methods=["GET","POST"])
def tinhbien():
    if request.method == "POST":
        name = request.form.get("ten")
        comment = request.form.get("comment")
        diadiem = "TinhBien"
        now = datetime.now()
        now = now.strftime("%Y/%m/%d %H:%M:%S")
        db.execute("INSERT INTO comments(diadiem, username, comment, date) VALUES(?, ?, ?, ?)", diadiem, name, comment, now)
        comments = db.execute("SELECT * FROM comments WHERE diadiem = ?;", diadiem)
        count = db.execute("SELECT COUNT(username) as count FROM comments WHERE diadiem = ?", diadiem)
        return render_template("TinhBien.html", comments = comments, count = count)
    else:
        diadiem = "TinhBien"
        comments = db.execute("SELECT * FROM comments WHERE diadiem = ?;", diadiem)
        count = db.execute("SELECT COUNT(username) as count FROM comments WHERE diadiem = ?", diadiem)
        return render_template("TinhBien.html", comments = comments, count = count)

@app.route("/triton", methods=["GET","POST"])
def triton():
    if request.method == "POST":
        name = request.form.get("ten")
        comment = request.form.get("comment")
        diadiem = "TriTon"
        now = datetime.now()
        now = now.strftime("%Y/%m/%d %H:%M:%S")
        db.execute("INSERT INTO comments(diadiem, username, comment, date) VALUES(?, ?, ?, ?)", diadiem, name, comment, now)
        comments = db.execute("SELECT * FROM comments WHERE diadiem = ?;", diadiem)
        count = db.execute("SELECT COUNT(username) as count FROM comments WHERE diadiem = ?", diadiem)
        return render_template("TriTon.html", comments = comments, count = count)
    else:
        diadiem = "TriTon"
        comments = db.execute("SELECT * FROM comments WHERE diadiem = ?;", diadiem)
        count = db.execute("SELECT COUNT(username) as count FROM comments WHERE diadiem = ?", diadiem)
        return render_template("TriTon.html", comments = comments, count = count)

@app.route("/longxuyen", methods=["GET","POST"])
def longxuyen():
    if request.method == "POST":
        name = request.form.get("ten")
        comment = request.form.get("comment")
        diadiem = "LongXuyen"
        now = datetime.now()
        now = now.strftime("%Y/%m/%d %H:%M:%S")
        db.execute("INSERT INTO comments(diadiem, username, comment, date) VALUES(?, ?, ?, ?)", diadiem, name, comment, now)
        comments = db.execute("SELECT * FROM comments WHERE diadiem = ?;", diadiem)
        count = db.execute("SELECT COUNT(username) as count FROM comments WHERE diadiem = ?", diadiem)
        return render_template("LongXuyen.html", comments = comments, count = count)
    else:
        diadiem = "LongXuyen"
        comments = db.execute("SELECT * FROM comments WHERE diadiem = ?;", diadiem)
        count = db.execute("SELECT COUNT(username) as count FROM comments WHERE diadiem = ?", diadiem)
        return render_template("LongXuyen.html", comments = comments, count = count)
@app.route("/vechungtoi", methods=["GET","POST"])
def vechungtoi():
    return render_template("vechungtoi.html")
@app.route("/lienhe", methods=["GET","POST"])
def lienhe():
    return render_template("lienhe.html")
@app.route("/gopy", methods=["GET","POST"])
def gopy():
    return render_template("gopy.html")