# AI Testing Automation 🤖

Automated UI testing framework for testing Google Gemini using Python, Selenium and PyTest.

The project focuses on validating AI responses through browser automation while measuring response time and detecting the response language.

## 🚀 Project Overview

This project was created to demonstrate a practical **AI Testing Automation** approach using industry-standard test automation tools.

The framework automates Google Gemini through Selenium and validates:

* AI response generation
* Response is not empty
* Response time
* Response language
* Test execution through PyTest
* CI execution with Jenkins
* JUnit test reporting

## 🛠️ Technologies

* Python 3.13
* Selenium WebDriver
* PyTest
* Page Object Model (POM)
* WebDriverWait
* PyTest Fixtures
* Lingua Language Detector
* Jenkins
* JUnit XML
* Git & GitHub

## 📁 Project Structure

```text
AI-Testing-Automation
│
├── pages/
│   ├── BasePage.py
│   └── Gemini_pages.py
│
├── tests/
│   ├── test_browser.py
│   └── test_chat.py
│
├── conftest.py
├── pytest.ini
├── .gitignore
├── main.py
└── README.md
```

## 🧪 Test Scenario

The main Gemini test performs the following steps:

1. Opens Google Gemini.
2. Enters a prompt.
3. Sends the prompt.
4. Waits for the AI response.
5. Verifies that a response is returned.
6. Detects the response language.
7. Measures the response time.
8. Reports the result through PyTest.

Example output:

```text
1 passed in 11.81s
```

## ⏱️ Response Time Testing

The framework measures the time between sending the prompt and receiving the AI response.

Example:

```text
Response time: 11.81 seconds
```

This allows response performance to be monitored during automated test execution.

## 🌍 Language Detection

The project uses the **Lingua Language Detector** to identify the language of the generated response.

Currently supported test languages include:

* Turkish
* English
* German
* French
* Spanish

## 🏗️ Framework Design

The project uses the **Page Object Model (POM)** architecture.

`BasePage` contains common WebDriver functionality, while `Gemini_Page` contains Gemini-specific locators and actions.

This separation keeps test logic independent from page interaction logic and makes the framework easier to maintain.

## ⚙️ PyTest

PyTest is used as the test execution framework.

Custom markers are configured in `pytest.ini`:

```ini
[pytest]
markers =
    smoke: critical smoke tests
    regression: regression tests
```

Run all tests:

```bash
python -m pytest
```

Run smoke tests:

```bash
python -m pytest -m smoke
```

## 🔄 Jenkins CI

The project is integrated with Jenkins for automated test execution.

Jenkins executes the PyTest suite and generates a JUnit XML report.

Pipeline flow:

```text
Jenkins
   ↓
PyTest
   ↓
Gemini UI Test
   ↓
JUnit XML Report
   ↓
Jenkins Test Result
```

Jenkins displays the automated test results, for example:

```text
1 test
1 passed
0 failed
```

## 📊 Test Reporting

PyTest generates a JUnit-compatible XML report:

```text
test-results.xml
```

Jenkins reads this report and displays the test results in the Jenkins interface.

## 🎯 Project Goals

The main goals of this project are:

* Practice real-world Selenium automation
* Apply Page Object Model architecture
* Automate an AI-powered web application
* Validate AI response behavior
* Measure AI response performance
* Integrate automated tests with Jenkins
* Demonstrate CI-oriented test execution
* Build a practical QA/SDET portfolio project

## 👨‍💻 Author

**Alper Türk**

QA / Test Automation enthusiast focused on:

* Selenium
* PyTest
* Java
* REST API Testing
* Jenkins
* CI/CD
* AI Testing
