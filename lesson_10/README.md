# Lesson 10: Allure reports

The project contains Page Object tests for the slow calculator and the
SauceDemo shop. Test steps, checks, titles, descriptions, features, and
severity levels are marked for Allure Report.

## Install dependencies

```bash
pip install -r lesson_10/requirements.txt
```

## Run tests and collect Allure results

Chrome and Firefox must be installed. Run the tests from the repository root:

```bash
pytest lesson_10 --alluredir=allure-results
```

## View the report

Install Allure Commandline, then build and open the report:

```bash
allure serve allure-results
```

The generated `allure-results` and `allure-report` directories do not need to
be committed to the repository.
