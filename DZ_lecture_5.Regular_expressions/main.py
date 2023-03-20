import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

PATTERN_PHONE = r"(\+7|8)\s*\(*(\d{3})\)*(\s|-)*(\d{3})-*(\d{2})-*(\d{2})" \
                r"(\s*)\(*(доб.)*\s*(\d+)*\)*"
PATTERN_NAME = r"^(\w+)(\s*)(,?)(\w+)(\s*)(,?)(\w*)(,?)(,?)(,?)"
REPLACER_PHONE = r"+7(\2)\4-\5-\6\7\8\9"
REPLACER_NAME = r"\1\3\10\4\6\9\7\8"


def update_name_or_phone(list_, pattern, replacer):
    update = []
    for line_ in list_:
        line_edit = re.sub(pattern, replacer, ','.join(line_))
        update.append(line_edit.split(','))
    return update


def del_duplicat():
    result_ = []
    for line in contacts_list_phone:
        for item in contacts_list_phone:
            if line[0] == item[0]:
                for k in range(1, len(contacts_list_phone[0])):
                    if item[k] == '':
                        item[k] = line[k]
                if len(line) > len(contacts_list_phone[0]):
                    line.pop()
                if line not in result_:
                    result_.append(line)
    return result_


contacts_list_name = \
    update_name_or_phone(contacts_list, PATTERN_NAME, REPLACER_NAME)
contacts_list_phone = \
    update_name_or_phone(contacts_list_name, PATTERN_PHONE, REPLACER_PHONE)
result = del_duplicat()

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result)
