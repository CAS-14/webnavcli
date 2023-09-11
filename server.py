from flask import Flask

app = Flask("webnav")

@app.route("/")
def home():
    return "hello world"

if __name__ == "__main__":
    app.run()