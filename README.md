### Superlists
A django app developed with TDD approach as described here http://www.obeythetestinggoat.com/ .

## Dependencies

- Python 3
- Django 1.10.*
- Selenium 2.53.6
- MySQL

## Getting Started
How to setup local environment? Follow given steps.
### Step 1
Create a virtual environment for project.Follow this guide http://docs.python-guide.org/en/latest/dev/virtualenvs/

Note:
- Run virtualenv with `--no-site-packages` option
- Include Python 3 path
- Install other packages using pip

### Step 2
For installing packages you need to first activate the virtualenv then perform following command.
```
$ pip install "django<1.11" "selenium<3" PyMySQL
```
You will also need google webdriver for functional tests in selenium.
- Download the driver from https://sites.google.com/a/chromium.org/chromedriver/getting-started
- Move the `chromedriver` file to directory /usr/bin/

### Step 3
Take clone in the project directory.You are now ready for development.

## License

This project is available under MIT license.
