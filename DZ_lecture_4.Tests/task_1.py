geo_logs = [
    {"visit1": ["Москва", "Россия"]},
    {"visit2": ["Дели", "Индия"]},
    {"visit3": ["Владимир", "Россия"]},
    {"visit4": ["Лиссабон", "Португалия"]},
    {"visit5": ["Париж", "Франция"]},
    {"visit6": ["Лиссабон", "Португалия"]},
    {"visit7": ["Тула", "Россия"]},
    {"visit8": ["Тула", "Россия"]},
    {"visit9": ["Курск", "Россия"]},
    {"visit10": ["Архангельск", "Россия"]},
]
ids = {
    "user1": [213, 213, 213, 15, 213],
    "user2": [54, 54, 119, 119, 119],
    "user3": [213, 98, 98, 35],
}
stats = {"facebook": 55, "yandex": 120, "vk": 115, "google": 99, "email": 42, "ok": 98}


def filter_country(dict_, country):
    dict_ = dict_.copy()
    dictionary = 0
    while dictionary < len(dict_):
        for key in dict_[dictionary]:
            if dict_[dictionary][key][1] != country:
                dict_.remove(dict_[dictionary])
            else:
                dictionary += 1
    return dict_


def get_unique_id(id_list):
    return list(set(sum(list(id_list.values()), [])))


def get_max_sale(statistics):
    final_dict = {k: v for k, v in statistics.items() if v == max(statistics.values())}
    return final_dict
