from flask import Flask,render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']=



@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello, World!' 

@app.route('/products')
def products():
    return 'Facial products can be purchased from this site'

if __name__=="__main__":
    app.run(debug=True)