# Algorithms and Data Structures on Python implemented, tested and documented

All folders' and files' places are given as if you are in Algorithms-master
folder.

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
[here](./docs/Table_of_contents.md).

All documentation is within the source code so that it automatically loads by
any decent IDE. In Vim works perfectly :)

All tests are inside `Algorithms/tests/`, examples of usage are also there.

For sorts and some interesting data types performance tuning and comparing
to python standard ones can be found in
[here](./speed_tuning/README.md).

Virtual environment made by venv with requirements for python listed in
`./requirements.txt`

Tests are performed by pytest.

Tests coverage checked by

```bash
coverage run
```

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

All configs are in `setup.cfg`.

Workflows are set using Github Actions with
`./.github/workflows/python-app.yml` file

## TODOs

- enable html for docs through scripts for markdownlint

## Contact

[baravoi.ivan@gmail.com](mailto:baravoi.ivan@gmail.com)
