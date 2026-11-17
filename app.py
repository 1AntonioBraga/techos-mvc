from flask import Flask
from controllers.chamado_controller import chamado_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "chave-secreta-pit-ii"
    app.register_blueprint(chamado_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
