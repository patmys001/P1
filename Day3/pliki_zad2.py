import chardet
#pip install chardet - w CLI
#rb
with open("test.log", "rb") as f:
    raw_data= f.read()
print(raw_data)

result = chardet.detect(raw_data)
print(result)
encoding = result["encoding"]
print(encoding)
