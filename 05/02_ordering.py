def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                dfs(neighbour)
        stack.append(node)

    nodes = set(graph.keys()).union({node for neighbours in graph.values() for node in neighbours})

    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]

def sort_list(nums, rules):
    graph = {}
    for a, b in rules:
        if a in nums and b in nums:
            if a not in graph:
                graph[a] = []
                
            graph[a].append(b)

    order = topological_sort(graph)
    order_dict = {num: i for i, num in enumerate(order)}
    
    return sorted(nums, key=lambda x: order_dict.get(x, len(nums)))

with open("./rules.txt") as rules_file:
    rules: list[tuple[int, int]] = []

    for line in rules_file.readlines():
        line = line.strip().split("|")
        rules.append((int(line[0]), int(line[1])))

with open("./updates.txt") as file:
    sum_of_middles = 0
    
    for line in file.readlines():
        nums = [int(n) for n in line.split(",")]
        original_nums = nums.copy()
        sorted_nums = sort_list(nums, rules)

        if sorted_nums != original_nums:
            sum_of_middles += sorted_nums[len(sorted_nums)//2]

    print(sum_of_middles)
                
     
            
