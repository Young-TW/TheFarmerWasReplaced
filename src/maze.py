import position

def pick_treasure():
	if get_entity_type() == Entities.Treasure:
		harvest()

def detect_road():
	directions = {North: False, East: False, South: False, West: False}
	for direction in directions:
		if can_move(direction):
			direction = True

	return directions

def DFS_with_target():
	map_row = [False, False, False, False, False, False, False, False, False, False, False, False]
	walked_map = [map_row, map_row, map_row, map_row, map_row, map_row, map_row, map_row, map_row, map_row, map_row, map_row]
	found = get_pos_x(), get_pos_y() == measure()
	if found:
		return "found"

	walked_map[get_pos_x()][get_pos_y()] = True

	# 1. 取得所有鄰居 (上, 下, 左, 右)
	roads_can_walk = detect_road()

	# 2. 關鍵步驟：依照「離寶藏的距離」對鄰居進行排序
	# 離寶藏越近的鄰居，排在越前面
	roads_can_walk.sort(依據 = 與寶藏的直線距離, 由小到大)

	# 3. 依序嘗試
	對於 每一個 鄰居 在 候選名單 中:
		如果 鄰居 沒有牆壁 且 鄰居 沒有走過:
			# 實際控制無人機移動
			move(鄰居)

			# 遞迴繼續探索
			result = DFS_with_target()

			if result == "found":
				return "found"

			# 如果這條路走不通（死胡同），要走回來（回溯）
			move(當前位置)

	# 如果所有鄰居都試過且都失敗
	return "not found"

def maze_1x1():
	pick_treasure()
	plant(Entities.Bush)
	substance = 1
	use_item(Items.Weird_Substance, substance)

if __name__ == "__main__":
	while 1:
		maze_1x1()
	pick_treasure()
	plant(Entities.Bush)