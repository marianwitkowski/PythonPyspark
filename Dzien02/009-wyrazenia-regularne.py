

# Wyrażenia regularne
import re
"""
M...k

^[0-9]{2}-[0-9]{3}$

[0-9] to samo co \d
[^0-9] inne znaki niż z zakresu 0-9 , to jes to samo co \D
\s - znaki białe
\S - inne niż znaki białe
\w - [0-9A-Za-z_]
\W - [^0-9A-Za-z_]
"""

txt = "Mały Marek machał makatką,trzymając trzy piwa"
result = re.findall("ma", txt.lower())
print(result)

zip_code = "12-345"
result = re.match(r"^[0-9]{2}-[0-9]{3}$", zip_code)
print(result)

txt = "kwota 123.45, termin 7 dni"
result = re.findall(r"\d", txt)
print(result)

txt = "kwota 123 termin 7 dni, oprocentowanie 44"
result = re.findall(r"\d+", txt)
print(result)

txt = "\r\nMały   Marek machał \t makatką,\ntrzymając \t trzy piwa"
print(txt)
result = re.sub(r"\s", "*", txt, 3)
print(result)