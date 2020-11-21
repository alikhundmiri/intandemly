from flask import Flask

app = Flask(__name__)

@app.route("/")
def main(self):
	"welcome to My first webpage hosted in a computer. Where is my Oscar?"


# if __name__ == '__main__':
# 	app.run(debug=True, host='0.0.0.0', port=80)