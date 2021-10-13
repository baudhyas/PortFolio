from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)

class Question:
	def __init__(self, question, answer, id):
		self.question = question
		self.answer = answer
		self.id = id

class Blog:
	def __init__(self, title, text, id):
		self.title = title
		self.text = text
		self.id = id

@app.route("/")
def index():
	return render_template('index.html')


@app.route("/blogs")
def blogs():
	all_blogs = []

	for i in range(10):
		all_blogs.append(Blog(f"Blog Title {i} ", "Blog Text", id))

	return render_template('blogs.html', blogs=all_blogs)


@app.route("/faqs")
def fags():
	all_quest = []
	for i in range(15):
		all_quest.append(Question("Question" + str(i), "Answer" + str(i), i))
	return render_template("faqs.html", question=all_quest)

@app.route("/login")
def login():
	return render_template("login.html")