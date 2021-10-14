import socket
import json
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 53533))
print("127.0.0.1:53533 running!")

while True:
	print("Server is listening.")
	data, address = s.recvfrom(1024)
	re_info = json.load(data)
	print("Request received.")
	if os.path.exist('./data.json'):
		with open('./data.json', 'r') as file:
			info = json.load(file)
			if info["name"] == re_info["name"] and info["type"] == re_info["type"]:
				s.sendto(file.encode(), address)
				print("info sent")
			else:
				print("no record")
	else:
		with open('./data.json', 'a') as file:
			file.write(data)
			

