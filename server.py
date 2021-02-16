from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from settings import sell_percent as Test
import average as A

app = Flask(__name__)


# config

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "Daniel"
app.config["MYSQL_PASSWORD"] = "12345678"
app.config["MYSQL_DB"] = "flask"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# Init MYSQL
mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/test", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        api_key = request.form["api_key"]
        secret_key = request.form["secret_key"]
        product = request.form["product"]
        margin_p = float(request.form["margin_p"])
        sell_p = float(request.form["sell_p"])
        trades = int(request.form["trades"])
        users = {"api_key": api_key, "secret_key": secret_key, "product": product,
                 "margin_p": margin_p, "sell_p": sell_p, "trades": trades}
        checker = True

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO user(API_KEY, SECRET_KEY, PRODUCT, MARGIN_P, SELL_P, TRADES ) VALUES(%s, %s, %s, %s, %s, %s)",
                    (api_key, secret_key, product, margin_p, sell_p, trades))

        # COMMIT DB
        mysql.connection.commit()

        # close connection
        cur.close()

        # , test= Test, users = users, current= A)
        return render_template("home.html", checker= checker, users = users, current= A)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
