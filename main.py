import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv",encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    contacts_list_updated = list()
    def format_number(contacts_list):
        pattern_1 = r"(\+7|8)?\s*\((\d+)\)\s*(\d+)[\s-]+(\d+)[\s-]+(\d+)"
        pattern_2 = r"(\+7|8)\s*(\d{3})[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s-]*"
        pattern_3 = r"\(*(доб\w*)(\.*)(\s*)(\d*)\)*"
        pattern_4 = r"^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)+(\,?)(\,?)(\,?)(\,?)"
        num_pattern = r"+7(\2)\3-\4-\5"
        num_pattern_2 = r"доб.\4"
        name_pattern = r"\1,\4,\7,"
        for card in contacts_list:
            card_as_string = ','.join(card)
            formatted_1 = re.sub(pattern_1, num_pattern, card_as_string)
            formatted_2 = re.sub(pattern_2, num_pattern, formatted_1)
            formatted_3 = re.sub(pattern_3, num_pattern_2, formatted_2)
            formatted_card = re.sub(pattern_4, name_pattern, formatted_3)
            card_as_list = formatted_card.split(',')
            contacts_list_updated.append(card_as_list)
        # pprint(contacts_list_updated)
        return contacts_list_updated
def join_duplicates(contacts_list):
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    for i in contacts_list:
        if i[0] not in list_1:
            list_1.append(i[0])
            list_3.append(i)
        elif i[0] in list_1:
            list_2.append(i[0])
            list_4.append(i)

    print(list_3)
    print(list_4)


    contacts_list_updated = list()
    for card in contacts_list:
        if card not in contacts_list_updated:
            contacts_list_updated.append(card)
    # pprint(contacts_list_updated)
format_number(contacts_list)
join_duplicates(contacts_list_updated)
# format_name(contacts_list_updated)
# format_name(contacts_list)
# format_number(contacts_list)
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding='utf-8') as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)