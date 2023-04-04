import pytest

from main import Stack


class TestBalanceCheck:

    def setup(self):
        self.stack = Stack()

    @pytest.mark.parametrize(
        'line, expected',
        (
                ('(((([{}]))))', 'Сбалансированно'),
                ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
                ('{{[()]}}', 'Сбалансированно'),
                ('}{}', 'Несбалансированно'),
                ('{{[(])]}}', 'Несбалансированно'),
                ('[[{())}]', 'Несбалансированно'),
        )
    )
    def test_balance_check(self, line: str, expected):
        assert self.stack.balance_check(line) == expected
