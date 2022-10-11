

sample_dictionary = {"car color": "red", "shirt color": "orange", "pant color":
                     "blue", "favorite color": "orange", "sock color": "stained"}

sample_keys = sample_dictionary.keys()

sample_values = sample_dictionary.values()


def dictionary_inverter(x: dict) -> dict:

    inverted_dictionary = {}
    for i, j in sample_dictionary.items():  #use i and j to show they are variables and do not need to be "key" and "value"
        inverted_dictionary.setdefault(j, list()).append(i) #https://www.programiz.com/python-programming/methods/dictionary/setdefault

    print(inverted_dictionary)

dictionary_inverter(sample_dictionary)

