from list_with_10000_nums import list_values

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    num_of_loops = 0
    while low<=high:
        num_of_loops+=1
        print(f"low -> {low}")
        print(f"high -> {high}")
        print(f"Loop Number -> {num_of_loops}")

        mid = int((low + high)/2)
        print(f"mid -> {mid}")
        guess = list[mid]
        print(f"Guess Value -> {guess}")

        if guess == item:
            print(f"Value Found -> {guess}")            
            return mid
        if guess > item:            
            high = mid - 1
        else:
            low = mid + 1

        print()        
    return None

item = 1453
binary_search(list_values, item)