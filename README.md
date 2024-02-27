# Test project REST API
The project is built on __Python__, __Playwright__ and __Allure__

## Set up virtual environment
Create a virtual environment
```
python -m venv .venv
```
Activate the virtual environment (Linux)
```
source .venv/bin/activate
```
Install dependencies
```
pip install -r requirements.txt
```

## Run tests
```
python -m pytest
```

## Generate and open an Allure report
```
allure serve allure-results
```