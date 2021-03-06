# Напишите декоратор to_json, который можно применить к различным функциям, чтобы
# преобразовывать их возвращаемое значение в JSON-формат. Не забудьте про сохранение
# корректного имени декорируемой функции.

import json
from functools import wraps


def to_json(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped


@to_json
def get_data():
    return {
        'data': 42
    }


print(get_data.__name__)
