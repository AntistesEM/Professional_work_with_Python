from datetime import datetime

from tqdm import tqdm

from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    for i in tqdm(range(1)):
        print(calculate_salary(), datetime.today().replace(microsecond=0))
        print(get_employees(), datetime.now().replace(microsecond=0))
