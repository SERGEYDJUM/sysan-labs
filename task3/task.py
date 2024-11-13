from math import log2, isclose
import csv
import sys


class TreeRelationships:
    def __init__(self, csv_string: str):
        adj_list = []
        max_node_id = 0
        min_node_id = sys.maxsize

        for line in csv.reader(csv_string.splitlines()):
            origin, dest = int(line[0]), int(line[1])
            adj_list.append((origin, dest))

            max_node_id = max(origin, dest, max_node_id)
            min_node_id = min(origin, dest, min_node_id)

        node_count = max_node_id - min_node_id + 1

        adj_matrix = [[False for _ in range(node_count)] for _ in range(node_count)]
        for origin, dest in adj_list:
            adj_matrix[origin - min_node_id][dest - min_node_id] = True

        self.root_node = min_node_id
        self.last_node = max_node_id
        self.node_count = node_count
        self.adj_matrix = adj_matrix

        self.peers = [set() for _ in range(node_count)]
        self.children = [set() for _ in range(node_count)]
        self.descendants = [set() for _ in range(node_count)]
        self.parents = [set() for _ in range(node_count)]
        self.ancestors = [set() for _ in range(node_count)]

    def _dfs(self, node: int):
        for child, connected in enumerate(self.adj_matrix[node]):
            if not connected:
                continue

            self.children[node].add(child)
            self.parents[child].add(node)

            self.ancestors[child].add(node)
            for ancestor in self.ancestors[node]:
                self.ancestors[child].add(ancestor)

            self._dfs(child)

            self.descendants[node].add(child)
            for descendant in self.descendants[child]:
                self.descendants[node].add(descendant)

        for child in self.children[node]:
            for peer in self.children[node]:
                if peer != child:
                    self.peers[child].add(peer)

    def get_relationships(self) -> list[list[int]]:
        self._dfs(0)
        output = []
        for node in range(self.node_count):
            r1 = len(self.children[node])
            r2 = len(self.parents[node])
            r3 = len(self.descendants[node]) - r1
            r4 = len(self.ancestors[node]) - r2
            r5 = len(self.peers[node])

            output.append([r1, r2, r3, r4, r5])

        return output


def task(csv_input: str) -> str:
    rels = TreeRelationships(csv_input).get_relationships()
    objects_cnt = len(rels)

    h = 0.0
    for object_rels in rels:
        h_object = 0.0
        for rel in object_rels:
            if rel != 0:
                p = rel / (objects_cnt - 1)
                h_object -= log2(p) * p
        h += h_object

    return f"{h:.1f}"


if __name__ == "__main__":
    with open("assets/task2.csv", encoding="utf-8", mode="r") as csv_file:
        print(f"{task(csv_file.read())}")
