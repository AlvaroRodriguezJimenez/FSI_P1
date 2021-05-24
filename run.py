# Search methods

import search
import random


#ab = search.GPSProblem('A', 'B'
#                       , search.romania)

#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450


cities = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L",
          "M", "N", "O", "P", "R", "S", "T", "U", "V", "Z"]

for i in range(3):
    x = cities[random.randint(0,19)]
    y = cities[random.randint(0,19)]

    xy = search.GPSProblem(x, y
                       , search.romania)
    print()

    print("------------------ Brunch and Bound with acumulated cost ------------------")
    print("Result: ", search.brunch_and_bound_cost_graph_search(xy).path(), "\n")

    print("------------------ Brunch and Bound with acumulated cost and heuristic ------------------")
    print("Result: ", search.brunch_and_bound_cost_with_heuristic_graph_search(xy).path(), "\n")
    print()

