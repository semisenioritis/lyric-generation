from flask import Flask

app = Flask(__name__)

#api route

@app.route("/<artist>")
def artists(artist):
    return {"lyric" : f"{artist}"}


if __name__ ==  "__main__":
    app.run(debug=True)