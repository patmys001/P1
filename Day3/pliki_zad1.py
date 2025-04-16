# działania z plikami
# filehandler - rura do pliku
# context manager - pomaga w pracy z plikami
# with - context manager w python
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
# with open("test.log","w") as fh:
#      fh.write("Powitanie\n")
#      fh.write("Kolejny\n")
#      fh.write("Cos jeszcze?\n")
with open("test.log", "w", encoding="utf-8") as fh:
    fh.write("nowe\n")
    fh.write("nowsdfsdf\n")
    fh.write("nowsdfsdf\n")
    fh.write("now8568567sdfsdf\n")
    fh.write("nowsdfsdf\n")
    fh.write("nowesdfewdsv\n")
with open("test.log", "a", encoding="utf-8") as fh:
    fh.write("LOL\n")
    fh.write("LOL\n")
    fh.write("LOL\n")
    fh.write("LŚŚŚL\n")
    fh.write("LŚŚŚL\n")
    fh.write("LŚŚŚL\n")
    fh.write("LŚŚŚL\n")
with open("test.log", "r", encoding="utf-8") as file:
    lines = file.read()
print(lines)
