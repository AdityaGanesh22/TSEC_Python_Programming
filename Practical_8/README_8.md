# Regular Expressions in Python

## Introduction
Regular Expressions (regex) are powerful tools for searching, matching, and manipulating text. They allow us to define patterns that can match strings of interest. Python provides the `re` module to work with regular expressions.

## Learning Objectives
By the end of this practical, students will be able to:
- Understand what regular expressions are and why they are useful.
- Use Python’s `re` module to search, match, and manipulate text.
- Apply regex for tasks such as validation, extraction, and substitution.
- Practice writing regex patterns through examples and exercises.


## 1. Basics of Regular Expressions

### Importing the `re` module
```python
import re
```

### Common Functions
- `re.match(pattern, string)` → Checks if the string starts with the pattern.
- `re.search(pattern, string)` → Searches for the first occurrence of the pattern.
- `re.findall(pattern, string)` → Returns all occurrences of the pattern.
- `re.sub(pattern, replacement, string)` → Replaces occurrences of the pattern.

### Example
```python
import re

text = "Python is powerful and Python is easy."
result = re.findall("Python", text)
print(result)  # ['Python', 'Python']
```
```python
text = "I like cats"

# re.match() checks only at the beginning of the string
result_match = re.match("I", text)
print(result_match.group())  # I

# re.search() looks anywhere in the string
result_search = re.search("cats", text)
print(result_search.group())  # cats
```

```python
text = "I like cats"
result = re.sub("cats", "dogs", text)
print(result)  # I like dogs
```
---

## 2. Regex Metacharacters

- `.` → Matches any character except newline.
- `^` → Matches the beginning of a string.
- `$` → Matches the end of a string.
- `*` → Matches 0 or more repetitions.
- `+` → Matches 1 or more repetitions.
- `?` → Matches 0 or 1 repetition.
- `{n}` → Matches exactly n repetitions.
- `{n,m}` → Matches between n and m repetitions.
- `[]` → Matches any one character inside the brackets.
- `|` → OR operator.
- `()` → Groups patterns.

### Example
```python
text = "cat, bat, rat, mat"
result = re.findall("[cr]at", text)
print(result)  # ['cat', 'rat']
```
---

## 3. Character Classes and Special Sequences

- `\d` → Matches any digit (0–9).
- `\D` → Matches any non-digit.
- `\w` → Matches any word character (letters, digits, underscore).
- `\W` → Matches any non-word character.
- `\s` → Matches any whitespace (space, tab, newline).
- `\S` → Matches any non-whitespace.

### Example
```python
text = "My number is 12345."
result = re.findall("\d+", text)
print(result)  # ['12345']
```

---

## 4. Anchors and Boundaries

- `^pattern` → Matches if the string starts with the pattern.
- `pattern$` → Matches if the string ends with the pattern.
- `\b` → Matches word boundary.
- `\B` → Matches non-word boundary.

### Example
```python
text = "hello world"
result = re.findall(r"\bworld", text)
print(result)  # ['world']
```

---

## 5. Grouping and Capturing

- Parentheses `()` are used to group patterns.
- Capturing groups allow extraction of specific parts of a match.

### Example
```python
text = "Email: student@example.com"
result = re.search(r"(\w+)@(\w+\.\w+)", text)
print(result.group(0))  # student@example.com
print(result.group(1))  # student
print(result.group(2))  # example.com
```
---

## 6. Practical Examples

### Validate a phone number
```python
text = "Call me at 9876543210"
result = re.findall(r"\b\d{10}\b", text)
print(result)  # ['9876543210']
```

### Extract all words starting with capital letters
```python
text = "Python is Fun and Powerful"
result = re.findall(r"\b[A-Z][a-z]*\b", text)
print(result)  # ['Python', 'Fun', 'Powerful']
```

### Replace multiple spaces with a single space
```python
text = "This   sentence    has   extra spaces."
result = re.sub(r"\s+", " ", text)
print(result)  # This sentence has extra spaces.
```
---

## Summary
- Regular expressions are powerful for text processing.
- Python’s re module provides functions like match, search, findall, and sub.
- Regex uses metacharacters, character classes, anchors, and groups to define patterns.
- Practice is key — try writing regex for validation, extraction, and substitution tasks.