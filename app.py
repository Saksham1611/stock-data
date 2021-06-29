from flask import Flask

# Create instance of flask
app = Flask(__name__)


#home function
@app.route('/')
def index():
    return f'HI its My FIRST FLASK thing'

    

