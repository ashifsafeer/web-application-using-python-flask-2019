from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "helloo.........."

@app.route("/home")
def home():
    return("my home page")

@app.route("/contact")
def contavt():
    return("my contact page")
    
        
if(__name__=="__main__"):
    app.run()