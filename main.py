#!/usr/bin/python
# -*- coding: utf-8 -*-

normalna_azbuka = ['А', 'Б', 'В', 'Г', 'Д', 'Ѓ', 'Е', 'Ж', 'З', 'Ѕ', 'И', 'Ј', 'К', 'Л', 'Љ', 'М', 'Н', 'Њ', 'О', 'П',
                   'Р', 'С', 'Т', 'Ќ', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Џ', 'Ш']
izmesana_azbuka = ['Х', 'Е', 'Ѕ', 'Љ', 'К', 'Л', 'О', 'Н', 'Д', 'П', 'У', 'Ш', 'Ч', 'Ж', 'Ј', 'С', 'М', 'Г', 'Ѓ', 'Џ',
                   'З', 'А', 'Ќ', 'В', 'Р', 'Ф', 'Б', 'Њ', 'Ц', 'Т', 'И']

result_file=open("formatiran_tekst.txt", "r", encoding="utf-8")
tekst=result_file.read()
result_file.close()

def encrypt(text):
    result = ""
    for item in text:
        index = normalna_azbuka.index(item)
        result += izmesana_azbuka[index]
    return result


"""def decrypt(text):
    result = ""
    for item in text:
        index = izmesana_azbuka.index(item)
        result += normalna_azbuka[index]
    return result
    //Проверка """


enkriptiran = encrypt(tekst)

final_res=open("enkriptiran_tekst.txt", "w", encoding="utf-8")
final_res.write(enkriptiran)
final_res.close()
