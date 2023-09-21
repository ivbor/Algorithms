### There are some algorithms implemented on python and some experiments with them

### All code is inside the ./Algorithms/python_solutions/ folder and can be imported with statement
```
from Algorithms/python_solutions/... import ...
```
### provided you are inside Algorithms/ or this folder is added to your PYTHONPATH

### The next table shows what is ready for which structures and what is yet planned to be done

| Algorithm/Structure | Initial code | Necessary tests | Tests up to 100% coverage | Stress tests | Docstring | Documentation | Experiments |
| :-----------------: | :----------: | :---: | :-------------: | :----------: | :-------: | :-----------: | :---------: |
| **Sorts**  | | | | | | | |
| | | | | | | | | 
| Count sort | done | done | done | not started | done | not started | not started |
| | | | | | | | |
| Count sort for array by key |
| inside 2-dimensional array | done | done | done | not started | done | not started | not started |
| | | | | | | | |
| Count sort |
| for 2-dimensional array | done | done | done | not started | started | not started | not started |
| | | | | | | | | 
| Digit sort | done | done | done | not started | started | not started | not started |
| Insertion sort | done | done | done | not started | started | not started | not started |
| Merge sort | done | done | done | not started | started | not started | not started |
| Quick sort | done | done | done | not started | started | not started | not started |
| **Searches** | | | | | | | |
| | | | | | | | |
| Binary search | done | done | done | not started | done | not started | not started |
| Lower and upper bounds | done | done | done | not started | done | not started | not started |
| Real binary search | done | done | done | not started | started | not started | not started |
| Ternary extrema search | done | done | done | not started | started | not started | not started |
| Split search | done | done | done | not started | started | not started | not started |
| **Data structures** | | | | | | | |
| | | | | | | | |
| Bloom filter | done | done | done | not started | done | not started | not started |
| Cyclic Linked List | done | done | done | not started | started | not started | not started |
| Deque | done | done | done | not started | not started | not started | not started |


### Workflows are set up as following:
#### Virtual environment made by venv with requirements for python listed in ./requirements.txt
#### Tests performed by pytest with all configs in ./pytest.ini
#### Coverage checked by coverage run command with all configs in ./.coveragerc
#### Security issues discovered by bandit -r ./Algorithms/python_solutions -b bandit.json command
#### Precommits are set using Github Actions with ./.github/workflows/python-app.yml file

### What is planned:
#### Get documentation parsed and ready-to-use with Sphinx
#### Provide some experiments using notebook for bottlenecks determination

### Contact: 
#### borovoy.vanya@gmail.com
