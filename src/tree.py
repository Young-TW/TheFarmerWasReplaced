import operate
import position

if __name__ == "__main__":
	position.move_to(0, 0)
	while 1:
		for i in range(get_world_size()):
			if get_pos_y() % 2 == 0:
				for j in range(get_world_size()):
					if get_pos_x() % 2 == 0:
						operate.operate(Entities.Tree)
					else:
						operate.operate(Entities.Grass)
					move(East)
			else:
				for j in range(get_world_size()):
					if get_pos_x() % 2 != 0:
						operate.operate(Entities.Tree)
					else:
						operate.operate(Entities.Grass)
					move(East)
			move(North)
