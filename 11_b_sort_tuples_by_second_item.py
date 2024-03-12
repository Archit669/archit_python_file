# Function to perform bubble sort on a list of tuples based on the second element
def bubble_sort_by_second_element(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j][1] > lst[j+1][1]:
                # Swap the tuples
                lst[j], lst[j+1] = lst[j+1], lst[j]

tuples_list = []
while True:
    tuple_str = input("Enter a tuple of two numbers separated by space (e.g., '5 3'). Press Enter to stop: ")
    if not tuple_str:
        break
    tuple_data = tuple(map(int, tuple_str.split()))
    tuples_list.append(tuple_data)

# Sort the list of tuples using bubble sort based on the second element
bubble_sort_by_second_element(tuples_list)

# Print the sorted list of tuples
print("Sorted list of tuples based on the second element:", tuples_list)
