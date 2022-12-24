# qa_365

Project contains functional tests for API and Web e2e tests:
/tests/functional/test_api.py
/tests/functional/test_e2e.py

### How to install project:
1. Make 'git clone' project 
2. cd to the directory with requirements.txt
3. activate your virtualenv
4. install requirements
```
git clone https://github.com/alekseyby/qa_365.git
cd qa_356
python -m venv <directory>
python -m venv venv
pip install -r requirements.txt
```
### Hot to run tests:
Default run for all test, supports all default pytest flags, eg -m that allows to run "tagged" test.
This project contains tests marked as "e2e_test" and "api_test"
```
pytest -l -m api_test
```
will run only api tests
### Custom run tests option:
```
--browser_type  | Allow to run test for Chrome and Firefox, default settings - "Chrome"
--headless | Allow to run test in 'headless' mode, default settings - True
--file_log_level | Sets log level to write logs to files. default setting  - 'WARNING'. See "Logging" part below
```

### Run example:
Will run tests in 'n' parallel threads, only tests marked as 'api_test', will write all logs above level 'INFO',
headless mode OFF, browser Chrome
```
pytest -l -n auto -m api_test --file_log_level INFO --headless False --browser_type Chrome 
```

### Run in parallel with pytest xdist plugin:
```
pytest -n auto | With this call, pytest will spawn a number of workers processes equal to the number of available CPUs,
and distribute the tests randomly across them. 
```
for more information please check xdist project documentation

### Logging:
Project contains 'log_helper' which allows you to change the level of logging that will be logged to files.
For example, if you set the DEBUG level, all messages will go to the log files.
If set ERROR, then only errors of the ERROR, CRITICAL level will get into the logs.
Log levels, from high to low:
```
CRITICAL
ERROR
WARNING
INFO
DEBUG
```

### Reporting:
To create Allure report, eg. est_api.py:
```
pytest --alluredir=<path to report directory> test_api.py
allure serve <path to report directory>
```

