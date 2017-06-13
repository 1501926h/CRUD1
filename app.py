#!flask/bin/python
from flask import Flask, jsonify, request
import Process
call = Flask(__name__)



@call.route('/todo-apin/getssl',methods=['GET'])

def get_ssl():
	return Process.get_ssl()
@call.route('/todo-apin/setssl',methods=['POST'])
def set_ssl():
	key = request.json['key']
	cert = request.json['cert']
	ca = request.json['ca']
	Process.set_ssl(key,cert,ca)
	return jsonify({'Private key' : key,
			'Certificate' : cert,
			'Certificate Authority' : ca
						}), 201

@call.route('/todo-apin/delssl',methods=['GET'])
def del_ssl():
	return Process.del_ssl()

@call.route('/todo-apin/getbridge/<string:input>',methods=['GET'])
def get_bridge_controller(input):
	config = Process.get_bridge_controller(input)
	return jsonify({'Config' : config })
@call.route('/todo-apin/setbridge',methods=['POST'])
def set_bridge_controller():
	bridge = request.json['bridge']
	prot = request.json['prot']
	ip = request.json['ip']
	port = request.json['port']
	result = Process.set_bridge_controller(bridge,prot,ip,port)
	return jsonify({'Bridge' : bridge,
			'Type' : prot,
			'IP' : ip,
			'Port' : port
					}), 201


@call.route('/todo-apin/setbridge2',methods=['POST'])
def set_bridge_controller2():

#	json_dict = request.get_json(force=True)
	bridge = request.json['bridge']
	insert = request.json['insert']

	result = Process.set_bridge_controller2(bridge,insert)
	return jsonify({'Bridge' : bridge,
                         'Insert' : insert
                                         }), 201

@call.route('/todo-apin/delbridge/<bridge>',methods=['DELETE'])
def del_bridge_controller(bridge):
	Process.del_bridge_controller(bridge)
	return jsonify({'Result': True
					}), 
@call.route('/todo-apin/updatebridge/<bridge>/<insert>',methods=['PUT'])
def update_bridge_controller(bridge,insert):
	Process.update_bridge_controller(bridge,insert)
	return jsonify({'Bridge' : bridge,
			'Config' : insert
					})
if __name__=='__main__':
	call.run(debug=True)
