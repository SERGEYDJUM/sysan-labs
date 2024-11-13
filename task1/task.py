import json

def main(path: str, row: int, column: int) -> int:
    adj_list = []
    max_node_i = 0

    with open(path, encoding="utf-8") as input_file:
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
        
    print(adj_matrix[row][column])
    return adj_matrix[row][column]
    
if __name__ == "__main__":
    main("assets/task1.json", 0, 0)