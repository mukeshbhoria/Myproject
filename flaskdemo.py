from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    data = "SCODEEN"
    return render_template('home.html', instname = data)
    #return f'form1{user}'

@app.route('/about')
def about():
    return  render_template(('aboutpage.html'))

@app.route('/contact')
def contact():
    return  render_template(('contact.html'))

if __name__ == '__main__':
    app.run()