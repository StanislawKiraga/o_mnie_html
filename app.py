from flask import Flask, render_template
from flask import request, redirect


app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template('me.htm')

@app.route('/mypage/contact', methods = ['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.htm")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")


