import pytest

from task_1 import filter_country, get_unique_id, get_max_sale, geo_logs, ids, stats


@pytest.mark.parametrize(
    "geo, country, expected",
    (
        (
            geo_logs,
            "Россия",
            [
                {"visit1": ["Москва", "Россия"]},
                {"visit3": ["Владимир", "Россия"]},
                {"visit7": ["Тула", "Россия"]},
                {"visit8": ["Тула", "Россия"]},
                {"visit9": ["Курск", "Россия"]},
                {"visit10": ["Архангельск", "Россия"]},
            ],
        ),
        (geo_logs, "Индия", [{"visit2": ["Дели", "Индия"]}]),
        (
            geo_logs,
            "Португалия",
            [
                {"visit4": ["Лиссабон", "Португалия"]},
                {"visit6": ["Лиссабон", "Португалия"]},
            ],
        ),
        (geo_logs, "Франция", [{"visit5": ["Париж", "Франция"]}]),
    ),
)
def test_filter_country(geo, country, expected):
    result = filter_country(geo, country)
    assert result == expected


@pytest.mark.parametrize(
    "dict_ids, expected",
    (
        (ids, [98, 35, 15, 213, 54, 119]),
        ({"user1": [213, 213, 213, 15, 213]}, [213, 15]),
        ({"user2": [54, 54, 119, 119, 119]}, [54, 119]),
        ({"user3": [213, 98, 98, 35]}, [98, 35, 213]),
    ),
)
def test_get_unique_id(dict_ids, expected):
    for value in dict_ids.values():
        for item in value:
            assert isinstance(item, int)
    result = get_unique_id(dict_ids)
    assert result == expected


@pytest.mark.parametrize(
    "statistics, expected",
    (
        (stats, {"yandex": 120}),
        (stats | {"vk": 150}, {"vk": 150}),
        (stats | {"ok": 130}, {"ok": 130}),
        (stats | {"ok": 130}, {"ok": 130}),
        (stats | {"google": 145}, {"google": 145}),
        (stats | {"facebook": 200}, {"facebook": 200}),
    ),
)
def test_get_max_sale(statistics, expected):
    assert isinstance(statistics, dict)
    result = get_max_sale(statistics)
    assert isinstance(result, dict)
    assert result == expected
