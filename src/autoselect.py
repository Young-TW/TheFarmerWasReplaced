def select_entities():
	if num_items(Items.Hay) < 1048576:
		return Entities.Grass
	elif num_items(Items.Wood) < 1048576:
		return Entities.Tree
	elif num_items(Items.Carrot) < 524288:
		return Entities.Carrot
	elif num_items(Items.Pumpkin) < 262144:
		return Entities.Pumpkin
	elif num_items(Items.Cactus) < 131072:
		return Entities.Cactus
	return Entities.Grass