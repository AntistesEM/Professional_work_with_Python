# ----------------------------------Задача № 3---------------------------------
class FlatIterator:

    def __init__(self, list_of_list):
        self.new_list = []
        self.chang(list_of_list, self.new_list)

    def __iter__(self):
        self.index_item = -1
        return self

    def __next__(self):
        self.index_item += 1
        if self.index_item == len(self.new_list):
            raise StopIteration
        return self.new_list[self.index_item]

    def chang(self, first_list, new_list):
        for item in first_list:
            if isinstance(item, list):
                self.chang(item, new_list)
            else:
                new_list.append(item)


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e',
                                                   'f', 'h', False, 1, 2, None,
                                                   '!']


if __name__ == '__main__':
    test_3()
