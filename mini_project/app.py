from flask import Flask
from login import login_bp
from persnol import persnol_bp
from sslc import sslc_bp
from hsc import hsc_bp
from ug import ug_bp

app= Flask(__name__)

app.secret_key = "my_secret_key"

app.register_blueprint(login_bp)
app.register_blueprint(persnol_bp)
app.register_blueprint(sslc_bp)
app.register_blueprint(hsc_bp)
app.register_blueprint(ug_bp)

if __name__ == "__main__":
    app.run(debug=True)