from datetime import date
from pathlib import Path
import re

logfile_path = "/home/hendrik/PycharmProjects/TUcontact/personal_data/"
logfile_name = "entry_log.txt"


def is_registered(path=logfile_path, file=logfile_name):
    with open(Path(path, file), "r") as logfile:
        for line in logfile:
            continue  # Skip to last line
        if convert_date(line) != date.today():
            # print("Fill out form")
            return False
        else:
            return True


def convert_date(date_obj):
    """Converts date string (dd-mm-yy) to datetime.date object and vice versa"""
    if isinstance(date_obj, str):
        date_obj = re.compile(r'\d+').findall(date_obj)  # Returns ["dd", "mm", "yyyy"] if date_obj has right format
        date_obj = list(map(int, date_obj))
        return date(day=date_obj[0], month=date_obj[1], year=date_obj[2])

    elif isinstance(date_obj, date):
        day, month, year = str(date_obj.day), str(date_obj.month), str(date_obj.year)
        # add leading 0 to day/month string, if needed
        if len(day) == 1:
            day = f"0{day}"
        if len(month) == 1:
            month = f"0{month}"
        return f"{day}-{month}-{year}"

    else:
        raise TypeError("date_obj must be of type str or datetime.date")


def write_log(path=logfile_path, file=logfile_name):
    today = date.today()
    with open(Path(path, file), "a") as logfile:
        logfile.write(convert_date(date.today()))
        logfile.write("\n")
