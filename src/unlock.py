def auto_unlock():
	cost = get_cost(Unlocks.Grass)
	# print(cost)
	can_unlock = True
	for item in cost:
		print(cost[item])
		if cost[item] > num_items(Items.Hay):
			can_unlock = False
	if can_unlock:
		unlock(Unlocks.Grass)
	print(can_unlock)
		


auto_unlock()