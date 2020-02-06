from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

def create_app(config_class=DevConfig):

    # Register Blueprints
    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app
