from datetime import datetime, date, timedelta

today = date.today()
print(today)
print(type(today))

time = datetime.now()
print(time)

print(time.year)
print(today.day)

tomorrow = today + timedelta(days=1)
print(tomorrow)

formated_data = datetime.now().strftime("%d/%m/%y")
print(formated_data)
####################################
print(30 * "#")
####################################
formated_time = datetime.now().strftime("%H:%M")
print(formated_time)
print(formated_time.removeprefix("0"))
print(30 * "#")
####################################
object_datetime = datetime.now().strptime("16/04/25","%d/%m/%y")
print(object_datetime)
print(type(object_datetime))
####################################
print(40 * "#")
####################################
products=[
    {"sku":1,"exp_date":today,"price":200},
    {"sku":2,"exp_date":today,"price":100},
    {"sku":3,"exp_date":tomorrow,"price":250.00},
    {"sku":4,"exp_date":today,"price":75.99},
    {"sku":5,"exp_date":today,"price":199},
]
for product in products:
    # print(product)
    # print(product["exp_date"])
    if product["exp_date"] != today:
        continue
    product["price"] *= 0.8
    print("Zmiana ceny")
    print(f"""
Price for sku {product["sku"]}
is now {product["price"]}""")
print(30 * "#")
#####################################
