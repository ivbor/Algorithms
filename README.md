## Algorithms and Data Structures implemented, tested and documented

All source code is inside the `./Algorithms/python_solutions/` folder 
and can be imported with statement
```python
from Algorithms.python_solutions.... import ...
```
provided you are inside `Algorithms-master/` or this folder is added 
to your PYTHONPATH by
```python
import sys

sys.path.append('path/to/Algorithms-master/')
```
or any other way.

Table of contents is 
[here](Algorithms/python_solutions/docs/Table_of_contents.md).

All documentation is within the source code so that it automatically loads by 
any decent IDE. In Vim works perfectly :)

All tests are inside `Algorithms/tests/`, examples of usage are also there.

For sorts and some interesting data types performance tuning and comparing
to python standard ones can be found in 
[here](Algorithms/python_solutions/speed_tuning/README.md).

## What is planned:

* Translations to C, for this purpose folder `Algorithms/C_solutions` 
was created.
Objective is to try to increase performance even further

* Performance studies for these pairs or special structures
(implementation here/well-known implementation if I happen to know one):
heap/heapq, hashtable/dict, bloom_filter/-, hyperloglog/-, 
sparse_table/slice, segment_tree/slice, trees between themselves/-,
graphs/-, bs within array/index, bs for different functions/-, 
split_find/sorted+index, ternary search for different functions/-

* Animations for dp solutions

* Example of work of matrix visualizer

## Workflows are set up as following:

Virtual environment made by venv with requirements for python listed in 
`./requirements.txt`

Tests performed by pytest with all configs in `./pytest.ini`

Tests coverage checked by  
```bash
coverage run
``` 
with all configs in `./.coveragerc`

Security issues discovered by 
```python
bandit -r ./Algorithms/python_solutions -b bandit.json
```

Baseline for bandit was generated using 
```bash
bandit -r ./Algorithms/python_solutions -f json -o bandit.json
```

Documentation coverage is checked by 
```bash
interrogate ./Algorithms/python_solutions -vv
```

Precommits are set using Github Actions with 
`./.github/workflows/python-app.yml` file

## Contact: 

baravoi.ivan@gmail.com
