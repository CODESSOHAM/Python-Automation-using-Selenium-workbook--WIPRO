# M4 Assignment 1 – Robot Framework Web Automation

## Module
M4 – Robot Framework Web Automation

## Assignment Title
E-Commerce Website Automation using Robot Framework

## Problem Statement
Automate basic web functionality of an e-commerce website using Robot Framework and SeleniumLibrary.

## Objective
The objective of this assignment is to automate the following activities:

- Launch the browser
- Open the e-commerce website
- Verify the page title
- Verify page content
- Enter a product search term
- Perform the search
- Verify the search page
- Capture a screenshot
- Close the browser after execution

## Application Used

Demo Web Shop

URL:
https://demowebshop.tricentis.com/

## Tools and Technologies

- Python
- Robot Framework
- SeleniumLibrary
- Selenium WebDriver
- Google Chrome
- PowerShell
- Visual Studio Code

## Project Structure

```text
Assignment-1_Robot_Framework_Web_Automation/
├── screenshots/
│   └── search_result.png
├── robot_ecommerce_test.robot
├── README.md
├── requirements.txt
├── output.xml
├── log.html
└── report.html
```

## Robot Framework Concepts Used

1. Test Setup
2. Test Teardown
3. Variables
4. SeleniumLibrary
5. User-defined keywords
6. ID locator
7. XPath locator
8. Assertions
9. Screenshot capture

## Test Cases
### Test Case 1 – Verify E-Commerce Website

Verifies:

Website content
Page title

### Test Case 2 – Verify Search Functionality

Steps:

Enter laptop in the search field.
Click the Search button.
Verify the search page.
Capture a screenshot.

## Execution Command

Run the following command from the assignment directory:

robot robot_ecommerce_test.robot

## Execution Result
2 tests, 2 passed, 0 failed
Reports Generated

## Robot Framework generated the following reports:

output.xml
log.html
report.html

## Result

The Robot Framework automation executed successfully.
Both test cases passed without failures.

## Conclusion

This assignment demonstrated basic web automation using Robot Framework and SeleniumLibrary.
The test successfully verified the e-commerce website and automated product search functionality with assertions, locators, setup/teardown, and screenshot capture.
