import json

adj_list = []
max_node_i = 0

with open("./lab01/input.json", encoding="utf-8") as input_file:
    data = json.load(input_file)
    
    for node in data["nodes"].keys():
        origin = int(node)
        for dest in data["nodes"][node]:
            dest = int(dest)
            adj_list.append((origin, dest))
            max_node_i = max(max_node_i, dest, origin)
    
adj_matrix = [[0 for _ in range(max_node_i + 1)] for _ in range(max_node_i + 1)]

for origin, dest in adj_list:
    adj_matrix[origin][dest] = 1
    # adj_matrix[dest][origin] = 1
    
parent_list = [None for _ in range(max_node_i + 1)]

for origin, dest in adj_list:
    parent_list[dest] = origin
    
print("Список связности:")
print(f"\t{adj_list}")
print()
print("Список родителей:")
print(f"\t{parent_list}")
print()
print("Матрица смежности:")
for row in adj_matrix:
    print(f"\t{row}")
    