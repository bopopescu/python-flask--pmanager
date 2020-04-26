from flask import Flask
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
bcrypt = Bcrypt(app)


from pmanager import routes