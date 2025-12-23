import position

def record_drone_place():
	row_have_drone[get_pos_y()] = True

def record_drone_leave_place():
	row_have_drone[get_pos_y()] = False

row_have_drone = {
	0: False,
	1: False,
	2: False,
	3: False,
	4: False,
	5: False,
	6: False,
	7: False,
	8: False,
	9: False,
	10: False,
	11: False,
	12: False,
	13: False,
	14: False,
	15: False,
}