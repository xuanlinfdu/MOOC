def nfruits(initial_quantities, string_pattern):
    #check every element in the string_pattern based on its order
    for i in range(len(string_pattern)):
        #He ate one kind of fruit
        initial_quantities[string_pattern[i]] -= 1
        #except the last one which he eats just on reaching the campus
        if not i == (len(string_pattern) - 1):
            #he buyed 1 fruit of each type other than the one he just had
            for item in initial_quantities.keys():
                if not item == string_pattern[i]:
                    initial_quantities[item] += 1
    #to obtain the maximum
    max_value = 0
    for item in initial_quantities.values():
        if item >= max_value:
            max_value = item
     
    return max_value