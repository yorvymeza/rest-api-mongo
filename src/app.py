from flask import Flask, render_template 
from routes.rutas import  main_blueprint



app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')

# Es el registro 
app.register_blueprint(main_blueprint, url_prefix='/users')



if __name__ == '__main__':
	app.run(debug=True, port=5000)


