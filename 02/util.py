def is_safe(numbers):
    if len(numbers) < 2:
        return False
    
    prev_num = numbers[0]
    greater_than_prev = None
    
    for num in numbers[1:]:
        distance = num - prev_num

        is_increasing = (distance > 0)
        if greater_than_prev is None:
            greater_than_prev = is_increasing
        else:
            if greater_than_prev != is_increasing:
                return False
           
        if abs(distance) < 1 or abs(distance) > 3:
            return False

        prev_num = num

    return True
