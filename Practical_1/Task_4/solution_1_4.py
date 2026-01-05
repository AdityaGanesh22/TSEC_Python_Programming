# solutions_1_4.py

def calculate_gross_salary(basic_salary: float) -> float:
    da = 0.70 * basic_salary
    ta = 0.30 * basic_salary
    hra = 0.10 * basic_salary
    gross_salary = basic_salary + da + ta + hra
    return gross_salary