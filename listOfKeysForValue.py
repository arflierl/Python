sample_dictionary = {"car color": "red", "shirt color": "orange", "pant color":
                     "blue", "favorite color": "orange", "sock color": "stained"}

sample_keys = sample_dictionary.keys()
sample_values = sample_dictionary.values()
print(sample_dictionary["car color"]) #how I will pair the value to the keys

def list_of_keys_for_value(x: dict, value) -> list:
    list_of_keys = []
    for i in sample_dictionary.keys():
        if sample_dictionary[i] == value:
            list_of_keys.append(i)

    print(list_of_keys)


list_of_keys_for_value(sample_dictionary, "orange")
