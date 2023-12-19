import copy

COUNT_NODES = 4
distance_map = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [0, 10, 0, 35, 25], [0, 15, 35, 0, 30], [0, 20, 25, 30, 0]]
path_depth = 0
map_memo = []
#map_memo[]  = ([1, 2, 4, 3, 1], 80)

def min_dist_tsp(map_memo):
	global distance_map, path_depth

	if (len(map_memo) == 0):
		for num_i in range(1, COUNT_NODES + 1):
			map_memo.append(([num_i], 0))
	else:
		if (path_depth > COUNT_NODES):
			return
		len_map_memo = len(map_memo)
		for j in range(0, len_map_memo):
			path_tuple = map_memo.pop(0)
			
			for num_i in range(1, COUNT_NODES + 1):
				
				if (num_i not in path_tuple[0] 
					or (num_i == path_tuple[0][len(path_tuple[0])-1] and len(path_tuple[0]) >= COUNT_NODES)):
					num_j = path_tuple[0][0]
					map_memo.append(([num_i] + path_tuple[0], path_tuple[1] + distance_map[num_i][num_j]))

	path_depth += 1
	min_dist_tsp(map_memo)		
		
min_dist_tsp(map_memo)
print(map_memo)