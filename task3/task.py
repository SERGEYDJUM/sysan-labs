import task2.task as task
from math import log2, isclose


def main(csv_input: str) -> str:
    rels = task.TreeRelationships(csv_input).get_relationships()
    objects_cnt = len(rels)

    h = 0.0
    for object_rels in rels:
        h_object = 0.0
        for rel in object_rels:
            if rel != 0:
                p = rel / (objects_cnt - 1)
                h_object -= log2(p) * p
        h += h_object
        
    return f"{h:.3f}"
            
    

if __name__ == "__main__":
    with open("assets/task2.csv", encoding="utf-8", mode="r") as csv_file:
        print(f"Общая энтропия: {main(csv_file.read())}")
