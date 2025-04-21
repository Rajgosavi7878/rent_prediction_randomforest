from flask import Flask,render_template,request
from pickle import load

with open("rent_model.pkl","rb") as f:
	model = load(f)

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
	if request.method == "POST":
		br = int(request.form.get("br"))
		if br == 1:
			d1 = [1,0,0,0]
		elif br == 2:
			d1 = [0,1,0,0]
		elif br == 3:
			d1 = [0,0,1,0]
		else:
			d1 = [0,0,0,1]

		fs = int(request.form.get("fs"))
		if fs == 1:
			d2 = [1,0,0]
		elif fs == 2:
			d2 = [0,1,0]
		else:
			d2 = [0,0,1]

		loc = int(request.form.get("loc"))
		if loc == 1:
			d3 = [1,0,0]
		elif loc == 2:
			d3 = [0,1,0]
		else:
			d3 = [0,0,1]

		d = [d1 + d2 + d3]
		ans = model.predict(d)
		msg = "Expected rent = ₹" + str(round(ans[0],2))
		return render_template("home.html",msg=msg,loc=loc,br=br,fs=fs)
	else:
		return render_template("home.html")

if __name__ == "__main__":
	app.run(use_reloader=True,debug=True)