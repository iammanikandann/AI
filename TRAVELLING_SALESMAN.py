
from sys import maxsize 
from itertools import permutations
V = 5


def travellingSalesmanProblem(graph, s): 


	vertex = [] 
	for i in range(V): 
		if i != s: 
			vertex.append(i) 

	
	min_path = maxsize 
	next_permutation=permutations(vertex)
	for i in next_permutation:

	
		current_pathweight = 0

		 
		k = s 
		for j in i: 
			current_pathweight += graph[k][j] 
			k = j 
		current_pathweight += graph[k][s] 

		min_path = min(min_path, current_pathweight) 
		
	return min_path 


if __name__ == "__main__": 

	
	graph = [[0, 2, 0, 3, 6], [2, 0, 4, 3, 0],[0, 4, 0, 7, 3], [3, 3, 7, 0, 3], [6, 0, 3, 3, 0]]
 
	s = 0
	print(travellingSalesmanProblem(graph, s))
