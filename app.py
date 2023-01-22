from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')

@app.route('/mypage/me')
def me():
    return render_template('me.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    elif request.method == 'POST':
        print(request.form)
        return redirect("/mypage")

@app.route('/mypage')
def index():
    return render_template('index.html')