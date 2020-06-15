# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import district.central_street.house1.room1 as central_street_house_1_room_1
import district.central_street.house1.room2 as central_street_house_1_room_2
import district.central_street.house2.room1 as central_street_house_2_room_1
import district.central_street.house2.room2 as central_street_house_2_room_2
import district.soviet_street.house1.room1 as soviet_street_house_1_room_1
import district.soviet_street.house1.room2 as soviet_street_house_1_room_2
import district.soviet_street.house2.room1 as soviet_street_house_2_room_1
import district.soviet_street.house2.room2 as soviet_street_house_2_room_2

total_people_in_street = ""

if central_street_house_1_room_1.folks:
    total_people_in_street += " ,".join(central_street_house_1_room_1.folks) + ", "

if central_street_house_1_room_2.folks:
    total_people_in_street += " ,".join(central_street_house_1_room_2.folks) + ", "

if central_street_house_2_room_1.folks:
    total_people_in_street += " ,".join(central_street_house_2_room_1.folks) + ", "

if central_street_house_2_room_2.folks:
    total_people_in_street += " ,".join(central_street_house_2_room_2.folks) + ", "

if soviet_street_house_1_room_1.folks:
    total_people_in_street += " ,".join(soviet_street_house_1_room_1.folks) + ", "

if soviet_street_house_1_room_2.folks:
    total_people_in_street += " ,".join(soviet_street_house_1_room_2.folks) + ", "

if soviet_street_house_2_room_1.folks:
    total_people_in_street += " ,".join(soviet_street_house_2_room_1.folks) + ", "

if soviet_street_house_2_room_2.folks:
    total_people_in_street += " ,".join(soviet_street_house_2_room_2.folks) + ". "

print(total_people_in_street)




