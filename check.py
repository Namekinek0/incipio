import json

def read_dict(word):
    with open('dictionary_compact.json', 'r') as file:
        dictionary = json.load(file)
        existence_test = dictionary.get(word)
        if not existence_test in locals():
            print("Lemma not found, try again. :(")
        else:
            print(dictionary[word])
        
