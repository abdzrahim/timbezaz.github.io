from flask import Flask, render_template
 
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.errorhandler(405)
def method_not_found(e):
    return render_template("405.html")

@app.route('/form/')
def form():
    return render_template("form.html")

@app.route('/chat/', methods=["GET","POST"])
def chat():
    try:
        if request.method == "POST":
        
            attempted_username = request.form['human']
            attempted_password = request.form['robot']

            #flash(attempted_username)
            #flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('homepage'))
                # return 
            else:
                error = "Invalid credentials. Try Again."

        return render_template("chat.html", error = error)
    except Exception as e:
        #flash(e)
        return render_template("chat.html", error = error)

if __name__ == "__main__":
    app.run(debug=True)
