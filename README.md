# Passjoin
Python implementation of the Pass-join index.

This index allows to efficiently query similar words within a distance threshold.

The implementation is based on this [paper](http://people.csail.mit.edu/dongdeng/papers/vldb2012-passjoin.pdf) and the existing Javascript implementation in the mnemoist package ([link](https://github.com/Yomguithereal/mnemonist)).


## Installation

```bash
$ pip install passjoin
```


## Usage

### Index creation
```python
from passjoin import Passjoin
from Levenshtein import distance  # or any string distance function

max_edit_distance = 1  # maximum edit distance for retrieval
corpus = ['pierre', 'pierr', 'jean', 'jeanne']

passjoin_index = Passjoin(corpus, max_edit_distance, distance)

```

### Index querying
```python

passjoin_index.get_word_variations('pierre')
>> {'pierre', 'pierr'}

passjoin_index.get_word_variations('jeann')
>> {'jean', 'jeanne'}

passjoin_index.get_word_variations('jeanine')
>> {'jeanne'}

```

## Contributing

Clone the project.

Install [pipenv](https://github.com/pypa/pipenv).

Run `pipenv install --dev`

Launch test with `pipenv run pytest`
