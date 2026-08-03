from flask import Flask
from login import login_bp
from persnol import persnol_bp

app= Flask(__name__)

app.register_blueprint(login_bp)
app.register_blueprint(persnol_bp)

if __name__ == "__main__":
    app.run(debug=True)