from flask import Flask, request
import json
import socket


app = Flask(__name__)

@app.route('/register', methods=['PUT'])
def getNum():
	pre_data = request.get_json()
	data = json.load(pre_data)
	hostname = data["hostname"]
	ip = data["fs_port"]
	as_ip = data["as_ip"]
	as_port = data["as_port"]
	msg = {"type": "A", "name" : hostname, "value" : ip, "ttl": 10}
	jsonfy(msg)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
	server_address = (as_ip, int(as_port))
	s.connect(server_address)
	try:
		s.sendall(msg)
		data = s.recv(1024)
		print(data)
		re_info = json.load(data)

	finally: s.close()

	return "Register Succusful", 200

@app.route('/fibonacci')
def getPara():
	number = request.args.get("number")
	if number is None:
		return "Missing parameter", 400
	return str(fib(int(number)))

def fib(n):
	a = 0
	b = 1
	if n == 0: 
		return a
	elif n == 1: 
		return b
	else:
		for i in range(2, n):
			c = a + b
			a = b
			b = c
		return b

if __name__ =='__main__':
	app.run(debug=True, port=9090)