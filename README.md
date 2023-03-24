# This project is a QA Engineer rol test for Aid for Aids

- [Task #1](test_json_placeholder.py)
- [Task #2](tets_afa_search_results.py)
- [Task #3](task3.md)
- [Task #4](task4.md)

## How to run this project

This project only runs in a unix OS like Linux or Macos

Setup venv:

```sh
# Replace with python3 if python is not found
python -m venv .env
source .env/bin/activate
```

Install required packages:

```sh
pip install -r requirements
playwright install
```

Run playwright test, after execution a tmp folder is created with screenshots of the tests:

```sh
pytest -s
```
