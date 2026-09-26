\# Video Demonstrations

This folder contains video demonstrations to help understand Selenium and get started with Python automation. The demonstrations cover installing Python and Selenium, configuring the automation environment, and completing initial Selenium assignment exercises.

## Concept Demonstrated

The assignment demonstrates how to:

- Identify multiple web elements using `find_elements()`
- Use XPath to locate multiple checkboxes
- Store multiple elements in a list
- Iterate through the list of elements
- Check whether a checkbox is already selected
- Click unchecked checkboxes
- Retrieve element attributes using `get_attribute()`

## Implementation

The following XPath identifies the checkboxes:

```python
//input[@type='checkbox' and @id]
```

Selenium returns all matching elements using:

```python
driver.find_elements(By.XPATH, ...)
```

The assignment then prints the total number of checkboxes and their IDs before selecting the unchecked checkboxes.

## Execution

Run:

```bash
python multiple_elements_checkbox.py
```

## Expected Output

```text
Total Checkboxes: ...
Checkbox ID: sunday
Checkbox ID: monday
...
```

All identified unchecked checkboxes are then selected.

## Video Demonstration

The working of this assignment is demonstrated in:

```text
Python_Assignment_Demonstration.mp4
```

## Result

The assignment successfully identifies multiple checkbox elements, retrieves their IDs, and selects the unchecked checkboxes using Selenium WebDriver.
