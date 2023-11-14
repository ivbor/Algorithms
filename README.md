## Algorithms and Data Structures implemented, tested and explained

All documentation and notebooks with some visualizations and experimenting 
are [here](docs/build/html/index.html') if the repo is on the local machine
and [here](https://htmlpreview.github.io/?https://github.com/ivbor/Algorithms/blob/master/docs/build/html/index.html) 
if viewed on the github (notebooks will load raw from htmlpreview, but are still
accessible from repo's page).

All source code is inside the `./Algorithms/python_solutions/` folder and can be imported with statement
```python
from Algorithms.python_solutions.... import ...
```
provided you are inside `Algorithms-master/` or this folder is added to your PYTHONPATH by
```python
import sys

sys.path.append('path/to/Algorithms-master/')
```
or any other way.

All tests are inside `./Algorithms/tests/`.

The dashboard for what is done and what has to be done is 
[here](https://ivbor.atlassian.net/jira/software/projects/KAN/boards/1) and
works only if you have a Jira account.

## Workflows are set up as following:

Virtual environment made by venv with requirements for python listed in `./requirements.txt`

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

Docstrings coverage checked by 
```bash
interrogate ./Algorithms/python_solutions -vv
```
 
Precommits are set using Github Actions with `./.github/workflows/python-app.yml` file

## Contact: 

baravoi.ivan@gmail.com
