from flask import Flask, render_template, request

app = Flask(__name__)


def predict_label(img_path):
	pass
	


@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

if __name__ =='__main__':
	app.run(debug = True)