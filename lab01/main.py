from csv import reader as csv_reader

adj_list = []
max_node_i = 0

with open("input.csv", encoding="utf-8") as input_file:
    for line in csv_reader(input_file.readlines()[1:]):
        origin, dest = int(line[0]), int(line[1])
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
    