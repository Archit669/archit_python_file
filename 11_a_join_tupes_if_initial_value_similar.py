#join tuples if initial value is similar

# Function to join tuples in the list whose initial value is the same
def join_tuples_with_same_initial(lst):
    print(lst)
    result = []
    current_tuple = None
    
    # Sort the list of tuples by the first element
    lst.sort(key=lambda x: x[0])
    
    for tpl in lst:
        if current_tuple is None:
            current_tuple = tpl
        elif current_tuple[0] == tpl[0]:
            # If the initial value is the same, join the tuples
            current_tuple = tuple(set(current_tuple + tpl))
        else:
            # If initial value changes, add the current tuple to the result list and update current_tuple
            result.append(current_tuple)
            current_tuple = tpl
    
    # Add the last tuple to the result list
    if current_tuple is not None:
        result.append(current_tuple)
    
    return result

# Take list of tuples from the user as input
tuples_list = []
while True:
    tuple_str = input("Enter a tuple of two numbers separated by space (e.g., '5 3'). Press Enter to stop: ")
    if not tuple_str:
        break
    tuple_data = tuple(map(int, tuple_str.split()))
    tuples_list.append(tuple_data)

# Join tuples in the list whose initial value is the same
modified_list = join_tuples_with_same_initial(tuples_list)

# Print the modified list of tuples
print("Modified list of tuples after joining similar initial values:", modified_list)



