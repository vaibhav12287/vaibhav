from flask import Flask,render_template,redirect,request,url_for,session,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')

app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



db = SQLAlchemy(app)

class users(db.Model):
	_id = db.Column("id", db.Integer,primary_key=True)
	name=db.Column("name",db.String(100))
	email=db.Column("email",db.String(100))

	def __init__(self,name,email):
		self.name=name
		self.email=email

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/login",methods=["POST","GET"])
def login():
	if request.method == "POST":
		user=request.form["nm"]
		session["user"]=user
		found_user = users.query.filter_by(name=user).first()
		if found_user:
			session["email"] = found_user.email
		else:
			usr = users(user,None)
			db.session.add(usr)
			db.session.commit()

		flash("Login Succesful!")
		return redirect(url_for("user"))
	else:
		if "user" in session:
			flash("You have been already looged in!")
			return redirect(url_for("user"))
		return render_template("login.html")

@app.route("/user",methods=["POST", "GET"])
def user():
	email = None
	if "user" in session:
		user = session["user"]
		if request.method == "POST":
			email = request.form["email"]
			session["email"]=email
			found_user = users.query.filter_by(name=user).first()
			found_user.email = email
			db.session.commit()
			flash("Your email has been recorded")
		else:
			if "email" in session:
				email=session["email"]
				
		return render_template("user.html",email=email)
	else:
		flash("You are not logged in")
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	if "user" in session:
		user=session["user"]
		flash(f"You have been logged out! ,{user}","info")
	session.pop("user",None)
	session.pop("email",None)
	return redirect(url_for("login"))

@app.route("/picture")
def picture():
	return render_template("picture.html")

@app.route("/view")
def view():
	return render_template("view.html",values=users.query.all())

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)