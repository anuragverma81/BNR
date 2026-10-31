from flask import Flask,render_template

app=Flask(__name__)

#prototype configuration - These are displayed values, not verified on-chain token data
BNR={
    "name":"BNR",
    "symbol":"BNR",
    "network":"Solana Devnet",
    "supply":"100,000,000,000",
    "status":"Prototype - not launched",
    "mint_address":None
}

@app.route("/")
def home():
    return render_template("index.html",bnr=BNR,page="home")

@app.route("/about")
def about():
    return render_template("about.html",bnr=BNR,page="about")

@app.route("/tokenomics")
def tokenomics():
    return render_template("tokenomics.html",bnr=BNR,page="tokenomics")

@app.route("/roadmap")
def roadmap():
    return render_template("roadmap.html",bnr=BNR,page="roadmap")

if __name__=="__main__":
    app.run(debug=True)