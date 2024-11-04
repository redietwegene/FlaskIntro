from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
 
app=Flask(__name__)

client = MongoClient('localhost',27017)
db =client.flask_database
todos=db.todos

@app.route('/')
def index():
    return render_template('index.html')
 
 
if __name__=="__main__":
    app.run(debug=True)