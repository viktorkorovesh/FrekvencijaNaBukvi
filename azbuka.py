#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

normalna_azbuka = ['А', 'Б', 'В', 'Г', 'Д', 'Ѓ', 'Е', 'Ж', 'З', 'Ѕ', 'И', 'Ј', 'К', 'Л', 'Љ', 'М', 'Н', 'Њ', 'О', 'П',
                   'Р', 'С', 'Т', 'Ќ', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Џ', 'Ш']
izmesana_azbuka = normalna_azbuka.copy()
random.shuffle(izmesana_azbuka)
with open("izmeshana_azbuka.txt", "w", encoding="utf-8") as f:
    f.write(str(izmesana_azbuka))
    f.close()


