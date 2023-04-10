from datetime import date
from application.db.salary import calculate_salary
from application.people import get_employees

if __name__ == '__main__':
    print(date.today())
    calculate_salary()
    get_employees()

