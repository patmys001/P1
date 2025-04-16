# jasno zad1
# dane typu klucz-wartość
import json

person_dict = {'name': 'patryk', 'age': 32, "czy_pali": None}
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4)
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)

with open('nasze_dane.json', "r") as f:
    data = json.load(f)
print(data)

print(data['name'])
jsno_text = json.dumps(data)
print(jsno_text)
print(type(jsno_text))
dict_json = json.loads(jsno_text)
print(dict_json)
print(type(dict_json))

