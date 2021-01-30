import re

kody = ['01-456', '23-b34', '00-000', '12345', '34-554', 'brak', 'xx-xxx']

wzorzec = re.compile('[0-9]{2}-[0-9]{3}')

for kod in kody:
    x = wzorzec.match(kod)
    print(kod, x)
    if x:
        print("OK")
    else:
        print("Nie ok")

