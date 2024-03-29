from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "ok we locked in now"
app.config["SESSION_PERMANENT"] = False

# lord forgive me
posts = {"Welcome to TikBook": "You can post whatever you want here!"}


@app.route("/", methods=["GET", "POST"])
def index():
    global posts
    if request.method == "POST":
        if "post_button" in request.form:
            posts[request.form["title"]] = request.form["content"]
    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)
