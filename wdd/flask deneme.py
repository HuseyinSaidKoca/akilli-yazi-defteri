from flask import Flask, render_template,request,json
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
import request

 
app = Flask(__name__)
app.config["MONGO_DBNAME"]="okul"
app.config["MONGO_URI"]="mongodb://admin:admin1234@akilliyazidefteri-lhf4s.mongodb.net/test?retryWrites=true&w=majority"
mongo=PyMongo(app)
ogrenci=mongo.db.ogrenciler
@app.route("/")
 
def index():
    return "Merhaba Dünya"
 
@app.route("/login")
 
def login():
    return "Kayıt Ekranı"

@app.route("/register")

def register():
    return "Kayıt Ekranı"

@app.route("/deneme")

def deneme():
	ogrenciler=ogrenci.find({"ogretmen_id":285463})
	if ogrenciler!=None:
		for x in ogrenciler:
			return "Kelime"

if __name__ =="__main__":
 
    app.run(debug =True,port=2000)