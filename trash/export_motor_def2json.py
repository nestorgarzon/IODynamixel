import json
motors = {
		'abs_z':{'id':33, 'type':'MX-28'},
		'bust_y':{'id':34, 'type':'RX-28'},
		'bust_x':{'id':35, 'type':'RX-28'},
		'head_z':{'id':36, 'type':'AX-12'},
		'head_y':{'id':37, 'type':'AX-12'},
		'l_shoulder_y':{'id':41, 'type':'RX-28'},
		'l_shoulder_x':{'id':42, 'type':'RX-28'},
		'l_arm_z':{'id':43, 'type':'RX-28'},
		'l_elbow_y':{'id':44, 'type':'RX-28'},
		'r_shoulder_y':{'id':51, 'type':'RX-28'},
		'r_shoulder_x':{'id':52, 'type':'RX-28'},
		'r_arm_z':{'id':53, 'type':'MX-28'},
		'r_elbow_y':{'id':54, 'type':'MX-28'}
		}

with open('motor_definitions.json', 'w') as outfile:
	json.dump(motors, outfile)

with open("motor_definitions.json") as f:
	data = json.load(f)

print(data)