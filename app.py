from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')


@app.route("/blogs")
def blogs():
	return render_template('blogs.html')


@app.route("/faqs")
def fags():
	return render_template("faqs.html")

@app.route("/login")
def login():
	return render_template("login.html")