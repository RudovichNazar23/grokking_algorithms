
graph = {
    "start": {"A": 6, "B": 2},
    "A": {"end": 1},
    "B": {"A": 3, "end": 5},
    "end": {}
}

costs = {
    "B": 2,
    "A": 6,
    "end": float("inf")
}

parents = {
    "A": "start",
    "B": "start",
    "end": None
}


processed = []


def find_lowest_cost_node(dct: dict):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in dct:
        cost = dct[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra():
    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]

            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return cost, costs
