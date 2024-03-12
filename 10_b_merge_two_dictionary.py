#merge two dictionary using the update method


dict1 = {}
while True:
    key = input("Enter a key for the first dictionary (press Enter to stop): ")
    if not key:
        break
    value = input("Enter the value for '{}' key: ".format(key))
    dict1[key] = value

dict2 = {}
while True:
    key = input("Enter a key for the second dictionary (press Enter to stop): ")
    if not key:
        break
    value = input("Enter the value for '{}' key: ".format(key))
    dict2[key] = value

dict1.update(dict2)

print("Merged dictionary:", dict1)
