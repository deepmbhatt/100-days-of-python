from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess/<name>')
def guess(name):
    response1 = requests.get("https://api.agify.io/?name=" + name)
    response2 = requests.get("https://api.genderize.io/?name=" + name)
    age = response1.json()["age"]
    gender = response2.json()["gender"]
    return render_template('genderage.html', name=name, age=age, gender=gender)

@app.route('/blog/<num>')
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", blog=all_posts)

if __name__ == '__main__':
    app.run(debug=True)
