from flask import Flask

app=Flask(__name__)


@app.route('/')
def get_news():
	return "no news yet"

if __name__=='__main__':
	app.debug=True
	app.run(host='0.0.0.0',port=5000)