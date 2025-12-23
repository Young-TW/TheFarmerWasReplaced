import position
import operate
import maze
import drone

def next_line():
	position.move_x_to(0)
	move(North)

def row():
	grass_row = [Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass]
	tree_row = [Entities.Carrot, Entities.Sunflower, Entities.Sunflower, Entities.Grass, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree]
	sunflower_row = [Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass]
	row = [Entities.Carrot, Entities.Sunflower, Entities.Sunflower, Entities.Tree, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass]
	pumpkin_row = [Entities.Carrot, Entities.Sunflower, Entities.Sunflower, Entities.Tree, Entities.Carrot, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass]
	carrot_row = [Entities.Carrot, Entities.Sunflower, Entities.Sunflower, Entities.Tree, Entities.Tree, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Carrot, Entities.Carrot, Entities.Carrot, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass]
	cactus_row = [Entities.Carrot, Entities.Sunflower, Entities.Sunflower, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass]

	for i in cactus_row:
		operate.operate_and_next(i)

def main():
	position.move_to(0, 0)
	while True:
		# for current_row in range(12):
		if num_drones() < max_drones():
			drone.record_drone_place()
			if spawn_drone(row):
				if drone.row_have_drone[get_pos_y()] == True:
					drone.record_drone_leave_place()
					move(North)
					# row()
					drone.record_drone_place()
				else:
					row()
					drone.record_drone_leave_place()
	# spawn_drone(maze.maze1x1())
	# loop()
	
def loop():
	while 1:
		row()
		next_line()

if __name__ == "__main__":
	main()