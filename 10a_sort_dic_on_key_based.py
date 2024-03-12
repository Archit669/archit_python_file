# Take dictionary from the user as input

my_dict = {}
while True:
    key = input("Enter a key (press Enter to stop): ")
    if not key:
        break
    value = input("Enter the value for '{}' key: ".format(key))
    my_dict[key] = int(value) 

sorted_keys = sorted(my_dict.keys())
sorted_dict = {}

for key in sorted_keys:
    sorted_dict[key] = my_dict[key]

print("Sorted dictionary:", sorted_dict)
