from http.client import responses

import requests

# pip install requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/usd/"

response = requests.get(url)
print(response)
# 200 it is ok
# 3xx - przekierowanie
# 4xx- błąd usera
# 5xx - błąd servera

print(response.text)
data = response.json()
print(type(data))
print(data)

# def kantor(waluta):
#     def usd(kwota):
#         print(f"Wymieniam dolary {3.77 * kwota}")
#
#     def eur(kwota):
#         print(f"Wymieniam deuro {4.28 * kwota}")
#
#     if waluta == "USD":
#         return usd
#     else:
#         return eur
#
#
# kantor_eur = kantor("eur")
# kantor_eur(1000)
# kantor_eur(13000)
#
# kantor_usd=kantor("USD")
# kantor_usd(1000)
# kantor_usd(13000)

print(data.keys())
print(data['rates'])
print(data.get('rates'))
#print(data['rates'[0]])
print(data['rates'][0]['mid'])
