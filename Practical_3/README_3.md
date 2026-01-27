# Practical 3 – Python Concepts Overview

This document introduces the core programming concepts used in Practical 3 (Tasks 1–9).
Read this before attempting the assignments. The examples here are different from your
practical tasks — they exist only to teach the concepts.

-----------------------------------------------------------------------

## Conditional logic: if, elif, else

Concept:
- Make decisions based on boolean conditions.
- Only the first matching branch runs; the rest are skipped.

Key ideas:
- Comparison operators: `==, !=, <, <=, >, >=`
- Logical operators: `and, or, not`
- Order matters; design non-overlapping ranges.

Example (concept-only):
```python
    score = 78
    if score >= 90:
        category = "A"
    elif score >= 75:
        category = "B"
    elif score >= 60:
        category = "C"
    else:
        category = "D"
    print(category)
```

Common pitfalls:
- Overlapping conditions causing unreachable code.
- Deep nesting; prefer elif chains for clarity.

-----------------------------------------------------------------------

## For loops: counting and iteration

Concept:
- Repeat actions over a known range or over items in a sequence.

Key ideas:
- `range(start, stop, step)` — stop is exclusive.
- Iterate over lists, strings, sets, dicts (keys/values/items).
- Use break to exit early; continue to skip to next iteration.

Example (concept-only):
```python
    items = ["pen", "notebook", "eraser"]
    for idx, item in enumerate(items, start=1):
        print(f"{idx}. {item}")
```
Patterns:
- Accumulation (sum, product, concatenation)
- Filtering (collect items meeting a condition)
- Transformation (map input to output)

Pitfalls:
- Off-by-one errors with range.
- Mutating a list while iterating over it — build a new list instead.

-----------------------------------------------------------------------

## While loops: condition-driven repetition

Concept:
- Repeat while a condition remains true; stop when it becomes false.

Key ideas:
- Use when the number of iterations is unknown in advance.
- Ensure loop variables change so the loop eventually ends.

Example (concept-only):
```python
    balance = 1000
    monthly_fee = 85
    months = 0
    while balance > 0:
        balance -= monthly_fee
        months += 1
    print("Months until zero:", months)
```

Pitfalls:
- Infinite loops from unchanged conditions.
- Complex conditions — extract into named variables for readability.

-----------------------------------------------------------------------

## String and character methods

Concept:
- Built-in helpers to analyze and transform text.

Useful checks:
- `s.isdigit()`, `s.isalpha()`, `s.islower()`, `s.isupper()`, `s.isalnum()`, `s.isspace()`

Transformations:
- `s.lower()`, `s.upper()`, `s.strip()`, `s.replace(old, new)`

Example (concept-only):
```python
    user_id = "  Abc123  "
    clean = user_id.strip()
    if clean.isalnum():
        print("Valid ID:", clean.lower())
    else:
        print("Invalid characters found")
```
Pitfalls:
- `isdigit()` is False for negatives or decimals; parse numbers instead.

-----------------------------------------------------------------------

## Functions: modular, reusable building blocks

Concept:
- Named blocks of code that take parameters and return values.

Key ideas:
- Keep functions small and focused on one job.
- Use clear names and docstrings.
- Prefer returning values over printing inside utility functions.

Example (concept-only):
```python
    def normalize(scores):
        """Scale scores to 0–1 range."""
        if not scores:
            return []
        mn, mx = min(scores), max(scores)
        if mn == mx:
            return [0.0 for _ in scores]
        return [(s - mn) / (mx - mn) for s in scores]
```
Pitfalls:
- Hidden dependencies on global state.
- Side effects (printing, mutating external data) that hinder reuse.

-----------------------------------------------------------------------

## Iterative patterns: accumulation and paired state updates

Accumulation (sum/product):
```python
    numbers = [2, 3, 4]
    product = 1
    for n in numbers:
        product *= n
    print(product)  # 24
```
Paired state updates (Fibonacci-like):
```python
    a, b = 2, 3
    for _ in range(5):
        print(a, end=" ")
        a, b = b, a + b
```

Pitfalls:
- Update order errors; use tuple assignment to update together.

-----------------------------------------------------------------------

## Primality concepts: efficient divisibility checks

Concept:
- A prime has no divisors other than 1 and itself.

Key ideas:
- Numbers <= 1 are not prime.
- Check divisibility only up to `sqrt(n)`.
- After handling 2, skip even numbers.

Example (concept-only):
```python
    def has_divisor(n):
        if n <= 3:
            return False
        if n % 2 == 0:
            return True
        i = 3
        while i * i <= n:
            if n % i == 0:
                return True
            i += 2
        return False
```
Pitfalls:
- Checking up to n is slow; use the `sqrt(n)` rule.
- Edge cases: 0, 1, 2, 3.

-----------------------------------------------------------------------

## Arithmetic operations and error handling

Core operators:
- +, -, *, / (float division), // (floor division), % (modulo), ** (power)

Division by zero:
- Guard with a check or raise an exception.

Example (concept-only):
```python
    def safe_divide(a, b):
        if b == 0:
            return None  # or raise ValueError("Division by zero")
        return a / b
```
Type notes:
- / returns float; // returns integer (floor).
- Convert types explicitly when mixing strings and numbers.

Pitfalls:
- Silent truncation with //.
- Relying on implicit conversions.

-----------------------------------------------------------------------

## Randomness and user interaction

Random numbers:
- `random.randint(a, b)` returns an integer in `[a, b]`
- `random.seed(x)` makes results reproducible for testing

Input handling:
- Validate and convert input; handle bad input gracefully.

Example (concept-only):
```python
    import random
    def roll_until_target(target):
        random.seed(42)  # deterministic for demonstration
        attempts = 0
        while True:
            attempts += 1
            r = random.randint(1, 6)
            if r == target:
                return attempts
```
Pitfalls:
- Trusting raw input; wrap conversions in try/except.
- Infinite loops when exit depends on invalid input.

-----------------------------------------------------------------------

## Control-flow toolkit: how concepts combine

- Branching: choose one path (if, elif, else).
- Counting: repeat a known number of times (for with range).
- Condition-driven repetition: repeat until a condition changes (while).
- State updates: maintain variables across iterations (accumulators, paired updates).
- Modularity: encapsulate logic in functions for clarity and reuse.
- Robustness: validate inputs and handle errors (e.g., division by zero).

-----------------------------------------------------------------------

## Practice prompts (concept-only, not your tasks)

- Conditionals: classify a temperature into “cold”, “mild”, “warm”, “hot” using non-overlapping ranges.
- For loop: build a list of squares for numbers 1–12, skipping multiples of 3.
- While loop: simulate withdrawing a fixed amount until a threshold; count withdrawals.
- Strings: validate a username that starts with a letter, is alphanumeric/underscore, and 5–12 chars long.
- Functions: write clamp(x, low, high) that limits x to the [low, high] range.
- Iteration: compute a running average of a stream without storing all values.
- Primality: count primes between 50 and 100 using an efficient check.
- Arithmetic + errors: implement `safe_mod(a, b)` returning `None if b == 0`, `else a % b`.
- Random + interaction: simulate rolling two dice until their sum is 9; report roll count.

-----------------------------------------------------------------------

## Mindset for success

- Plan first: define inputs, outputs, and control flow (branching vs looping).
- Name things well: clear variable and function names reduce mistakes.
- Test small: include edge cases (0, 1, negatives, empty lists).
- Iterate: start simple, then refine.
- Explain your logic: if you can describe it plainly, you can code it.

-----------------------------------------------------------------------

By mastering these concepts, you’ll be ready to implement Practical 3 tasks confidently
without needing to see any specific answers.