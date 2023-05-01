whitelist = set('абвгдѓежзѕијклљмнњопрстќуфхцчџшАБВГДЃЕЖЗЅИЈКЛЉМНЊОПРСТЌУФХЦЧЏШ')
result_file = open("originalen_tekst.txt", "r", encoding="utf-8")
tekst = result_file.read()
result_file.close()
tekst = tekst.upper()
finalen_tekst = ''.join(filter(whitelist.__contains__, tekst))
with open("formatiran_tekst.txt", "w", encoding="utf-8") as f:
    f.write(str(finalen_tekst))
    f.close()

print(finalen_tekst)