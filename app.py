from flask import Flask, render_template

app = Flask(__name__ ,static_url_path='/static')
app.secret_key = "adkviergbieriw8r5y25y025gtreiuugbfdhgb8r7505702rebgwhg"

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
@app.route("/blogs")
@app.route("/blogs/<int:id_>")
def blogs(id_=None):

	if id_ is not None:
		return render_template('blog.html', data=id_)

	all_blogs = []

	for i in range(10):
		all_blogs.append(Blog(f"Blog Title {i} ", "Blog small Introduction Text ...", i))

	return render_template('blogs.html', blogs=all_blogs)


@app.route("/faqs")
def fags():
	all_quest = []
	for i in range(15):
		all_quest.append(Question("Question " + str(i), "Answer" + str(i), i))
	return render_template("faqs.html", question=all_quest)
