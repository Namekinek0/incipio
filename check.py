import json

def read_dict(word):
    with open('dictionary_compact.json', 'r') as file:
        dictionary = json.load(file)
        if not word in dictionary.keys():
            print("There is not such lemma in the dictionary :(\nCheck for any mispelling and try again.")
        else:
            print(dictionary[word])
        
