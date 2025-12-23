
def set_ground_type(type):
	if type == Grounds.Grassland:
		if get_ground_type() != Grounds.Grassland:
			till()
	else:
		if get_ground_type() != Grounds.Soil:
			till()

def operate(type):
	ground_plant_types = {Entities.Carrot: Grounds.Soil, Entities.Pumpkin: Grounds.Soil, Entities.Sunflower: Grounds.Soil, Entities.Cactus: Grounds.Soil,
						  Entities.Bush: Grounds.Grassland, Entities.Grass: Grounds.Grassland, Entities.Tree: Grounds.Grassland}
	if can_harvest():
		harvest()
	set_ground_type(ground_plant_types[type])
	plant(type)

def operate_and_next(type):
	operate(type)
	move(East)
	