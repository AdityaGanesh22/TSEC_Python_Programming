# Practical 2 Concepts: Introduction to Python Data Structures

Python provides several built‑in data structures that help us organize and manage information. In this practical, we explore four of the most important ones: lists, tuples, sets, and dictionaries. Each has its own purpose and way of working, and together they form the foundation for most Python programs.

---

## 1. Lists

A list is an ordered collection of items. You can think of it like a shopping list or a playlist: items are kept in order, and you can add, remove, or change them whenever you like.

### Key ideas:
- Lists are written with square brackets: `[ ]`.
- Items inside a list can be numbers, words, or even other lists.
- Lists are mutable, meaning they can be changed after creation.

### Common operations:
- Add an item: use append to put something at the end.
- Remove an item: use remove to delete something by name.
- Update an item: use indexing (like `list[0]`) to change a specific position.
- Sort items: use sort to arrange them in order.

#### Example:
```python
items = ["apple", "banana"]
items.append("cherry")      # ["apple", "banana", "cherry"]
items.remove("banana")      # ["apple", "cherry"]
items[0] = "grape"          # ["grape", "cherry"]
items.sort()                # ["cherry", "grape"]
```
---

## 2. Tuples

A tuple is like a list, but once created, it cannot be changed. Tuples are useful when you want to store information that should stay fixed, like a pair of values or a record.

### Key ideas:
- Tuples are written with parentheses: `( )`.
- They can hold multiple items, often grouped together logically.
- Tuples are immutable, meaning they cannot be modified directly.

#### Example:
```python
point = (3, 5)
date = ("January", 2026)
```

Here, point might represent coordinates, and date might represent a month and year. You cannot change the values inside these tuples once they are created.

---

## 3. Sets

A set is an unordered collection of unique items. Sets are useful when you want to avoid duplicates or when you care about membership rather than order.

### Key ideas:
- Sets are written with curly braces: `{ }`.
- Items in a set must be unique.
- Sets are great for comparing groups of things.

### Common operations:
- Union: combine two sets to include everything.
- Intersection: find items common to both sets.
- Difference: find items in one set but not the other.

Example:
```python
group1 = {"Alice", "Bob"}
group2 = {"Bob", "Charlie"}

group1.union(group2)        # {"Alice", "Bob", "Charlie"}
group1.intersection(group2) # {"Bob"}
group1.difference(group2)   # {"Alice"}
```
---

## 4. Dictionaries

A dictionary stores information as key–value pairs. Think of it like a real dictionary: each word (the key) maps to a definition (the value).

### Key ideas:
- Dictionaries are written with curly braces `{ }`, but in the form key: value.
- Keys must be unique, while values can repeat.
- Dictionaries are useful for storing structured information.

### Common operations:
- Create a record: assign a key to a value.
- Update a value: change the value for a given key.
- Delete a record: remove a key and its value.

#### Example:
```python
student = {"name": "Alex", "grade": "A", "attendance": 95}

student["grade"] = "B"      # {"name": "Alex", "grade": "B", "attendance": 95}
student["attendance"] = 100 # {"name": "Alex", "grade": "B", "attendance": 100}
del student["name"]         # {"grade": "B", "attendance": 100}
```
---

## Summary

- Lists: ordered, changeable collections. Use them when you need flexibility.
- Tuples: ordered, fixed collections. Use them when values should not change.
- Sets: unordered collections of unique items. Use them for comparisons and membership.
- Dictionaries: key–value pairs. Use them to store structured records.

---

## Tips for Beginners

- Start with small examples. Try creating a list of two items, a tuple of two values, a set with a few names, or a dictionary with one record.
- Remember the difference between mutable (lists, sets, dictionaries) and immutable (tuples).
- Use built‑in methods (append, remove, union, sort, etc.) instead of writing complex logic.
- Don’t worry about loops or conditionals yet—focus on understanding how these structures behave.

---

This file is meant to be a self‑study guide. Read through the examples, try them out in Python, and experiment by changing the values. The more you practice, the more natural these structures will feel.