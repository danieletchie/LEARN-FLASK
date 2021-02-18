from flask import Flask, render_template, url_for, request, redirect
from settings import sell_percent as Test
import average as A

app = Flask(__name__)

@app.route("/")
def index():
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

        # , test= Test, users = users, current= A)
        return render_template('home.html', checker= checker, users = users, current= A)
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
