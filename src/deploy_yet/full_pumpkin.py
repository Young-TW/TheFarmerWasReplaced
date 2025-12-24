import position
import operate

if __name__ == "__main__":
	while 1:
		# plant pumpkin in full area
		map_size = get_world_size()
		position.move_to(0, 0)
		harvest_all = True
		for x in range(map_size):
			for y in range(map_size):
				if can_harvest():
					move(East)
					continue
				else:
					harvest_all = False
				operate.operate_not_harvest(Entities.Pumpkin)
				move(East)
			move(North)
		if get_pos_x() == get_world_size() - 1:
			if get_pos_y() == get_world_size() - 1:
				if harvest_all:
					harvest()