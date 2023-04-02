from pprint import pprint

from task_1 import filter_country, get_unique_id, get_max_sale, geo_logs, ids, stats
from task_2 import YandexFolder

if __name__ == "__main__":
    for i in ["Россия", "Франция", "Португалия", "Индия"]:
        print(f'Фильтр "{i}": ')
        pprint(filter_country(geo_logs, i))
    print("\n", get_unique_id(ids))
    print(
        "\n",
        *[
            f"Максимальный объём продаж у {k} = {v}"
            for k, v in get_max_sale(stats).items()
        ],
    )
    folder = YandexFolder()
    print(folder.add_folder("task_2"))
    print(folder.delete_folder("task_2"))
