from flask import Flask, request
import socket
import json

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/fibonacci')
def getPara():
	hostname = request.args.get("hostname")
	fs_port = request.args.get("fs_port")
	number = request.args.get("number")
	as_ip = request.args.get("as_ip")
	as_port = request.args.get("as_port")
	if hostname is None or fs_port is None or number is None or as_ip is None or as_port is None:
		return "Missing parameters", 400
	data = {"type": "A", "hostname": hostname}
	msg_json = json.dumps(data)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
	server_address = (as_ip, int(as_port))
	print(server_address)
	# s.connect(server_address)
	try:
		s.sendall(msg_json)
		data = s.recv(1024)
		print(data)
		re_info = json.load(data)
	finally: ss.close()

	return re_info["value"], 200


if __name__ =='__main__':
	app.run(debug=True, port=8080)