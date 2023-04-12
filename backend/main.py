from flask import Flask
import modelrunner as mod
app = Flask(__name__)

#api route

@app.route("/<artist>")
def artists(artist):
    # call main function inside this
    if artist=="Taylor Swift":
        lyrics=mod.taylor_caller()
    elif artist=="Ed Sheeran":
        lyrics=mod.ed_caller()
    elif artist=="Rihanna":
        lyrics=mod.rihanna_caller()
    else:
        lyrics=''
    return {"lyric" : f"{lyrics}"}


if __name__ ==  "__main__":
    app.run(debug=True)