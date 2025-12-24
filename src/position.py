def move_to(x, y):
	x_now, y_now = get_pos_x(), get_pos_y()
	if x_now < x:
		for i in range((-x_now) + x):
			move(East)
	elif x_now > x:
		for i in range(x_now - x):
			move(West)
	if y_now < y:
		for i in range((-y_now) + y):
			move(North)
	elif y_now > y:
		for i in range(y_now - y):
			move(South)

def move_x_to(x):
	x_now = get_pos_x()
	if x_now < x:
		for i in range((-x_now) + x):
			move(East)
	elif x_now > x:
		for i in range(x_now - x):
			move(West)

def move_y_to(y):
	y_now = get_pos_y()
	if y_now < y:
		for i in range((-y_now) + y):
			move(North)
	elif y_now > y:
		for i in range(y_now - y):
			move(South)

def traverse_map(operation_type):
    map_size = get_world_size()
    move_to(0, 0)
    for x in range(map_size):
        for y in range(map_size):
			move(North)
			operate.operate(operation_type)
		move(East)