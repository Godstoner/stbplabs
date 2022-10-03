# Алгоритми гешування SHA.

import hashlib
# иніціалізуюча строка

str = "timetostop"


# закодировать Python.Engineering с помощью encode()
# затем отправить SHA256()

result = hashlib.sha256 ( str .encode ())


# Выводит эквивалентное шестнадцатеричное значение.

print ( "Шістнадцятирічний еквівалент SHA256:" )

print ( result.hexdigest())

print ( "" )

