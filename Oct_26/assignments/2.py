import random
from typing import List, Dict, Any, ItemsView

COLORS = ["Red", "Yellow", "Green", "Blue", "Pink", "Brown", "Purple"]
SPEEDS = ["Slow", "Medium", "Fast"]
ALIEN_COUNT = 50

aliens = []
for _ in range(ALIEN_COUNT):
    aliens.append({ "id": int(random.random() * 10000000),
                    "color": random.choice(COLORS), 
                    "points": random.randrange(10, 30),
                    "speed": random.choice(SPEEDS) })

def group_by(items: List[Dict[str, Any]], grouping_basis: str, known_groups: List[str] | None = None) -> Dict[str, List[Dict[str, Any]]]:
    result: Dict[str, List[Dict[str, Any]]] = {}

    if known_groups is not None:
        for group in known_groups:
            result[group] = []

    for item in items:
        basis = item[grouping_basis]

        if not basis in result:
            result[basis] = [ item ]
        else:
            added = False
            for index, cached_item in enumerate(result[basis]):
                if cached_item["id"] > item["id"]:
                    result[basis].insert(index, item)
                    added = True
                    break
            
            if not added:
                result[basis].append(item)

    return result

def print_groups(grouped_items: Dict[str, List[Dict[str, Any]]]):
    for k, v in grouped_items.items():
        print(k)
        print()
        for item in v:
            print(item, sep="\t")
        print()

aliens_by_color = group_by(aliens, "color", COLORS)
aliens_by_speed = group_by(aliens, "speed", SPEEDS)

print("## By color:\n")
print_groups(aliens_by_color)

print("## By speed:\n")
print_groups(aliens_by_speed)
