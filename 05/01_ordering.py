with open("./rules.txt") as rules_file:
    rules: list[tuple[int, int]] = []

    for line in rules_file.readlines():
        line = line.strip().split("|")
        rules.append((int(line[0]), int(line[1])))

with open("./updates.txt") as file:
    sum_of_middles = 0
    
    for line in file.readlines():
        nums = [int(n) for n in line.split(",")]

        valid = True
        for rule in rules:
            if rule[0] in nums and rule[1] in nums:
                if nums.index(rule[1]) <= nums.index(rule[0]):
                    valid = False
                    break
        if valid:
            sum_of_middles += nums[len(nums)//2] 

    print(sum_of_middles)
                
     
            
