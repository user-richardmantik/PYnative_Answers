import copy

n = 4
depth_reccursion = 0
distance_map = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [0, 10, 0, 35, 25], [0, 15, 35, 0, 30], [0, 20, 25, 30, 0]]

map_memo = []
#map_memo[]  = ([1, 2, 4, 3, 1], 80)
def init_map_memo(map_memo):
	global distance_map
	for n in range (1, len(distance_map)):
		for m in range(1, len(distance_map[n])):
			if distance_map[n][m] != 0:
				map_memo.append(([n, m], distance_map[n][m]))

def get_item_tuple_from_map_memo(path_list, map_memo):
	for item_tuple in map_memo:
		if (item_tuple[0] == path_list):
			return item_tuple
	return None

def min_dist_tsp(from_n,to_n, map_memo):
	global distance_map, depth_reccursion
	
	# if adjacent
	if (from_n >= 1 and from_n < len(distance_map) and distance_map[from_n][to_n] > 0):
		return distance_map[from_n][to_n]
	else:
		min_dist = None
		
		for to_n_i in range(1, len(distance_map[to_n])+1):
			
			for path_list, path_dist in map_memo:
				if (path_list[len(path_list)-1] == to_n_i
					and to_n not in path_list and len(path_list) <= n):
					new_path_list = list(path_list) + [to_n]
					new_dist	  = path_dist + distance_map[to_n_i][to_n]

					map_memo.append((new_path_list, new_dist))
					
					min_dist = min_dist_tsp(from_n, to_n_i, map_memo) + new_dist

		return min_dist
					


init_map_memo(map_memo)
min_dist_tsp(1, 1, map_memo)
print(map_memo)