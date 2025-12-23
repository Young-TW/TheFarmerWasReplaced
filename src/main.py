import position
import operate

def next_line():
	position.move_x_to(0)
	move(North)

def row():
	get_water()
	grass_row = [Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass]
	tree_row = [Entities.Carrot, Entities.Sunflower, Entities.Sunflower, Entities.Grass, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree, Entities.Tree]
	sunflower_row = [Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Sunflower, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass]
	row = [Entities.Carrot, Entities.Sunflower, Entities.Sunflower, Entities.Tree, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass]
	pumpkin_row = [Entities.Carrot, Entities.Sunflower, Entities.Sunflower, Entities.Tree, Entities.Carrot, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass]
	carrot_row = [Entities.Carrot, Entities.Sunflower, Entities.Sunflower, Entities.Tree, Entities.Tree, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Carrot, Entities.Carrot, Entities.Carrot, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass]
	cactus_row = [Entities.Carrot, Entities.Sunflower, Entities.Sunflower, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Cactus, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass]

	for i in tree_row:
		operate.operate_and_next(i)

def main():
	change_hat(Hats.Cactus_Hat)
	position.move_to(0, 0)
	loop()
	
def loop():
	while 1:
		row()
		next_line()

if __name__ == "__main__":
	main()