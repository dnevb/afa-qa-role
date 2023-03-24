# This project is a QA Engineer rol test for Aid for Aids

- [test_json_placeholder.py] (Task #1)
- [tets_afa_search_results.py] (Task #2)
- [task#3.md] (Task #3)
- [task#4.md] (Task #4)

## How to run this project

Setup venv

```sh
# Replace with python3 if python is not found
python -m venv .env
source .env/bin/activate
```

Install required packages

```sh
pip install -r requirements
playwright install
```

Run playwright test, after execution a tmp folder is created with screenshots of the tests

```sh
pytest -s
```
