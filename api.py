from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/name')
def name():
	out = subprocess.check_output('hostname', shell=True)
	return out

@app.route('/<char>/<nb>')
def char(char, nb):
	return char*int(nb)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
