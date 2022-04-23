from datetime import datetime
from Application import people
from Application import salary

def main():
    time_now = datetime.now()

    print(time_now)
    print(people.get_employees())
    print(salary.calculate_salary())







if __name__ == '__main__':
    main()