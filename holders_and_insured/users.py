from holders_and_insured.names import transliterated_names as first_names, transliterated_last_names as last_names
from random import randint, choice


class User:
    def __init__(self, holder_id):
        self.first_name = choice(first_names)
        self.last_name = choice(last_names) + ('a' if self.first_name[-1] == 'a' else '')
        self.document_number = randint(10 ** 9, 10 ** 10 - 1)
        self.phone = f'+79{randint(10_000_00_00, 99_999_99_99)}'
        age = randint(18 if holder_id is None else 3, 80)
        self.birth_date = f'{2021 - age}-{str(randint(1, 12)).zfill(2)}-{str(randint(1, 28)).zfill(2)}'
        self.holder_id = holder_id

    # id | first_name | last_name | document_number | birth_date | [phone or holder_id]
    def __str__(self):
        if self.holder_id is None:
            last_attr = f"'{self.phone}')"
        else:
            last_attr = f"{self.holder_id})"
        return f"('{self.first_name}', '{self.last_name}', '{self.document_number}', '{self.birth_date}', " + last_attr


# policy_holders = list(map(lambda _: User(holder_id=None), range(50)))
# list(map(print, policy_holders))
