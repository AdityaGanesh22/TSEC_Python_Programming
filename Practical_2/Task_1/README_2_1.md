# Practical 2 – Task 1: Task List Manager

## Objective
Develop a Python program to manage a task list using lists and tuples.

## Instructions
- Implement the following functions in `student_code_2_1.py`:
  1. `add_task(task_list, task_name, priority)`
     - Adds a new task as a tuple (task_name, priority).
  2. `remove_task(task_list, task_name)`
     - Removes the task with the given name.
  3. `update_task(task_list, task_name, new_priority)`
     - Updates the priority of the given task.
  4. `sort_tasks(task_list)`
     - Sorts tasks by priority (ascending).

- Each function should return the updated task list.



## Objective
Write Python functions to manage a simple task list using built-in list methods and tuples.

## Instructions
Implement the following functions in `student_code_2_1.py`:

### Using Lists
1. `add_task_list(task_list, task_name)`
   - Adds a new task using append.
2. `remove_task_list(task_list, task_name)`
   - Removes a task using remove.
3. `update_task_list(task_list, index, new_task)`
   - Updates a task at a given position using indexing.
4. `sort_tasks_list(task_list)`
   - Sorts tasks alphabetically using sort.

### Using Tuples
Each tuple is (task_name, priority).
1. `add_task_tuple(task_list, task_name, priority)`
   - Adds a new task as a tuple.
2. `remove_task_tuple(task_list, task_name)`
   - Removes a tuple by task_name.
3. `update_task_tuple(task_list, task_name, new_priority)`
   - Updates the priority of a tuple.
4. `sort_tasks_tuple(task_list)`
   - Sorts tasks by priority (ascending).

## Examples with Lists
```python
add_task_list([], "Distillation column design")
# Output: ["Distillation column design"]

remove_task_list(["Heat exchanger sizing"], "Heat exchanger sizing")
# Output: []

update_task_list(["Pump selection"], 0, "Compressor selection")
# Output: ["Compressor selection"]

sort_tasks_list(["Reactor design", "Absorption study", "Catalyst testing"])
# Output: ["Absorption study", "Catalyst testing", "Reactor design"]

## Examples with Tuples
add_task_tuple([], "Distillation column design", 2)
# Output: [("Distillation column design", 2)]

remove_task_tuple([("Heat exchanger sizing", 1)], "Heat exchanger sizing")
# Output: []

update_task_tuple([("Pump selection", 3)], "Pump selection", 1)
# Output: [("Pump selection", 1)]

sort_tasks_tuple([("A", 3), ("B", 1), ("C", 2)])
# Output: [("B", 1), ("C", 2), ("A", 3)]
```

## How to check your solution
1. Open CLI and navigate to the assignment folder.
2. Run Python and import your functions:
   `from student_code_2_1 import *`
3. Test your functions interactively.
