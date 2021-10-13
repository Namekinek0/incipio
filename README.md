## ![Incipio's logo](https://camo.githubusercontent.com/85f336b99a9ef0a0aa5ed0631d8917aba2481ec6680f94b192ba7b50206e12ba/68747470733a2f2f692e706f7374696d672e63632f7a444648596a32562f696e636970696f2e706e67)

## Incĭpĭo (i'ntʃipjo)

Incipio is a [CLI](https://en.wikipedia.org/wiki/Command-line_interface) English dictionary viewer written in Python. In Latin, incipio means "I begin, I undertake." I think I couldn't find a better name, since I'm an English graduate who's learning Python for pure fun and willing to learn new skills, and this project is my first enterprise. At the moment, Incipio is a bare-boned project: users can:
* Input a word and check for its definition from the Webster's Unabridged Dictionary released by Project Gutenberg in 2009
* Launch few commands to interact with the app  
  
I'm a total beginner in programming, thus any comment or suggestion are welcomed.

## How to use

### On Windows

Windows doesn't have a python interpreter installed by default. After [cloning the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository), you can go inside the local cloned folder, go to \dist\main\ folder and run main.exe. 
EDITED: Git doesn't push the folder. Try to solve ASAP.

### On Linux

Linux has a python interpreter by default. Just run main.py

## Future features

* Adding commands like: comparing two lemmas, adding custom lemmas
* The current json which contains the dictionary must be improved, since it misses syllabications, parts of speech and etymologies.     Moreover, it returns corrupted text sometimes
* Adding more languages
* Switching among different dictionaries
* Using updated dictionaries by API

## Acknowledgements

* The JSON file which stores the whole dictionary is provided by [matthewreagan](https://github.com/matthewreagan/WebstersEnglishDictionary)
* Webster's Unabridged Dictionary is provided by [Project Gutenberg](https://www.gutenberg.org/ebooks/29765)

## License

This project is released under MIT License. However, dictionary_compact.json is licensed under GPL v2 license by its creator, and WebstersEnglishDictionary.txt is licensed under The Project Gutenberg License.
