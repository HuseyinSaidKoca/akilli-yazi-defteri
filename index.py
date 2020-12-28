#öğrenci ek ödev kontrol yap sistem günlük ödeve ulaşınca true göndersin
from flask import Flask, render_template, redirect, url_for, request, json, jsonify
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
import requests
import random
import datetime
import locale

app = Flask(__name__, static_url_path='/static')
import pymongo  
client = pymongo.MongoClient("mongodb+srv://admin:admin1234@akilliyazidefteri-lhf4s.mongodb.net/test?retryWrites=true&w=majority") 

mongo=client.okul

@app.route("/", methods=['GET', 'POST'])
 
def index():
	if request.method=="POST":
		myogrt_id=request.form["ogrt_id"]
		mysifre=request.form["pass"]
		sonuc=mongo.ogretmenler.find({"ogretmen_id":int(myogrt_id),"sifre":mysifre})
		if sonuc.count()>0:
			ogrenciler=mongo.ogrenciler.find({"ogretmen_id":int(myogrt_id)})
			return render_template("listele.html",ogrenciler=ogrenciler,ogt=sonuc,ogt_id=int(myogrt_id))
		else:
			return render_template("hataliogt.html")
	return render_template("index.html")

@app.route("/listele/<ogrt_id>", methods=['GET', 'POST'])
def listele(ogrt_id):
	ogrenciler=mongo.ogrenciler.find({"ogretmen_id":int(ogrt_id)})
	return render_template("listele.html",ogrenciler=ogrenciler,ogt_id=int(ogrt_id))

@app.route('/ogrenciler/<ogrn_id>', methods=['GET', 'POST'])
def ogrenciler(ogrn_id):
	ogrenci=mongo.ogrenciler.find_one({"ogrenci_id":int(ogrn_id)})
	ogrt_id=ogrenci["ogretmen_id"]
	sinir=ogrenci["seviye"]
	if request.method=="POST":
		if request.form["btn"]=="sinir":
			sinir_ayar=request.form["sinir_ayar"]
			seviye=ogrenci["seviye"]
			dogrular=ogrenci["dogrular"]
			mongo.ogrenciler.update_one({"ogrenci_id":int(ogrn_id)},{ "$set": { "sinir"+str(seviye): int(sinir_ayar) } })

		if request.form["btn"]=="odev":
			odev_ayar=request.form["sinir_ayar"]
			mongo.ogrenciler.update_one({"ogrenci_id":int(ogrn_id)},{ "$set": { "odev": int(odev_ayar) } })

	return render_template("ogrenci_incele.html", ogrenci=ogrenci,ogrt_id=ogrt_id ,sinir=sinir, max=17000)

@app.route("/ogrenci", methods=['GET', 'POST'])
def ogrenci():
	if request.method=="POST":
		myogrn_id=request.form["ogrn_id"]
		mysifre=request.form["pass"]
		sonuc=mongo.ogrenciler.find({"ogrenci_id":int(myogrn_id),"sifre":mysifre})
		if sonuc.count()>0:
			ogrenci=mongo.ogrenciler.find_one({"ogrenci_id":int(myogrn_id)})
			sinir=ogrenci["seviye"]
			return render_template("ogrenci_incele2.html", ogrenci=ogrenci,sinir=sinir, max=17000)
		else:
			return render_template("hataliogr.html")
	return render_template("ogrenci.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
	if request.method=="POST":
		myad=request.form["ogrn_adk"]
		myogrn_no=request.form["ogrn_nok"]
		myogrn_id=request.form["ogrn_nok"]+str(random.randint(10000,100000))
		myogrt_id=request.form["ogrt_idk"]
		mysifre=request.form["pass"]
		sonuc=mongo.ogrenciler.find({"ogrenci_no":int(myogrn_no),"sifre":mysifre})
		if sonuc.count()>0:
			return render_template("hatalireg.html")
		else:
			locale.setlocale(locale.LC_ALL, '')
			an = datetime.datetime.now()
			tarih = datetime.datetime.strftime(an,'%Y %B %d %a %X')
			mongo.ogrenciler.insert_one({"ogrenci_no":int(myogrn_no),"ogrenci_id":int(myogrn_id),"ogretmen_id":int(myogrt_id),"isim":myad,"sifre":mysifre,
			"zaman":str(tarih),
			"dogrular":0,
			"hgdogrular":0,
			"seviye":1,
			"odev":5,
			"sinir1": 100, 
			"sinir2": 100, 
			"sinir3": 100, 
			"sinir4": 100, 
			"sinir5": 100,
			"toplam_yanlis":0,
			"elakin": 0,
			"omutuy": 0,
			"oridsb": 0,
			"zcgscp": 0,
			"hvgfj": 0
			})
			return render_template("kayittamam.html",ogrenci_id=myogrn_id)
	else:
		return render_template("register.html")



@app.route("/forget", methods=['GET', 'POST'])
def forget():
	if request.method=="POST":
		myogrn_no=request.form["ogrn_no"]
		mysifre=request.form["pass"]
		sonuc=mongo.ogrenciler.find_one({"ogrenci_no":int(myogrn_no),"sifre":mysifre})
		if sonuc!=None:
			return render_template("forget2.html", ogrenci_id=sonuc["ogrenci_id"], max=17000)
		else:
			return render_template("hatalifor.html")
	return render_template("forget.html")

@app.route("/ekle/<ogrt_id>", methods=['GET', 'POST'])
def ekle(ogrt_id):
	ornek=mongo.ornekler
	if request.method=="POST":
		listbox=request.form["grup"] 
		gir_ornek=request.form["gir_ornek"]
		print(listbox)
		print(gir_ornek)
		bulunan=mongo.ornekler.ornek.find_one({str(listbox):str(gir_ornek)})
		print("-------------------------------------------",bulunan)
		if mongo.ornek.bulunan==None:
			mongo.ornek.insert_one({"yazi":str(gir_ornek),"grup":str(listbox)})
			print("eklendi")
			return render_template("eklendi.html", max=17000)
			
		else:
			return render_template("ekle2.html", max=17000)
	return render_template("ekle.html")

if __name__ =="__main__":
 
	app.run(debug =True)