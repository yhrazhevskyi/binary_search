# q1 = 6 + 3 * 5
# q2 = 12 / 2 - 4
# q3 = 9 + 14 * 2 - 6
# q4 = (6 + 2) * 3
# q5 = 14 / (11 - 4)
# q6 = 9 + 12 * (8 - 3)
#
# print(q1, q2, q3, q4, q5, q6, sep='\n')
#
# print(format(987654.129, ',.2f'))
#
# DISCOUNT = 0.1
# price = 90
# print(price * (1 - DISCOUNT))

# height = float(input("Введите ваш рост: "))
# print("Ваш рост =", height, "см")

# color = input("Введите ваш color: ")
# print("color =", color)

# b = a + 2
# a = b * 4
# b = a / 3.14
# a = b - 8

# w = 5; x = 4; y = 8; z = 2
# print("result = ", x + y)
# print("result = ", z * 2)
# print("result = ", y / z)
# print("result = ", y - z)
# print("result = ", w / z)

# total = 10 + 14

# due = total - down_payment

# total = subtotal * 0.15

# sales = 10.23456
# print(format(sales, ".2f"))

# number = 1234567.5
# print(format(number, ","))

# print ('Джордж', 'Джон' , 'Пол', 'Ринго' , sep='@')

# start_value = float(input("Введите плановый объем продаж: "))
# per_prof = 0.23
# profit = start_value * per_prof
# print("Прибыль =", profit)

# start_value = float(input("Введите кол-во кв. метров : "))
# acr = start_value / 4047
# print("кол-во акров = ", format(acr, ".4f"))

# item_1 = float(input("Введите стоимость 1 товара: "))
# item_2 = float(input("Введите стоимость 2 товара: "))
# item_3 = float(input("Введите стоимость 3 товара: "))
# item_4 = float(input("Введите стоимость 4 товара: "))
# item_5 = float(input("Введите стоимость 5 товара: "))
# tax = 0.07
#
# total_price = item_1 + item_2 + item_3 + item_4 + item_5
# total_price_tax = total_price * tax
#
# print("Сумма: ", total_price)
# print("Налоги: ", total_price_tax)
# print("К оплате: ", total_price + total_price_tax)

# time = float(input("Введите кол-во часов: "))
# distance = time * 70 # 70 - это расстояние которое проезжает автомоби
# print(f"За {time} часов автомобиль пройдет: {distance}")

# price = float(input("Введите сумму покупки: "))
# reg_tax = 0.025
# fed_tax = 0.05
#
# print(f"Сумма: {price}, федеральный налог:{price * fed_tax}, региональный налог: {price * reg_tax}, "
#       f"общий налог: {price * fed_tax + price * reg_tax}, общая сумма: {price + price * fed_tax + price * reg_tax}")

# distance = float(input("Введите кол-во пройденных км: "))
# consumption = float(input("Введите кол-во топлива необходимого на 1 км: "))
# result = distance / consumption
# print("Расход:100", result)

# dish = float(input("Введите стоимость еды: "))
# tips = dish * 0.18  # 0.18 - процент чаевых
# tax = dish * 0.07  # 0.7 - процент налога
# total = dish + tips + tax
# print("Блюдо:", dish, "Чаевые:", tips, "Налоги:", tax, "К оплате:", total)

# temperature = float(input("Введите температуру по шкале Цельсия: "))
# f_temperature = 9 * temperature / 5 + 32
# print("Введенная температура по Цельсию соответствует", f_temperature, "градусам по Фарингейту")

# bun_number = int(input("Введите желаемое кол-во булочек: "))
#
# sugar = (1.5 / 48.0) * bun_number
# butter = (1 / 48.0) * bun_number
# flour = (2.75 / 48.0) * bun_number
#
# print("Для выпекания {0} булочек необходимо: {1} стаканов сахара {2} стаканов масла {3} стаканов муки".format(
#     bun_number, sugar, butter, flour))

# students_male = float(input("Введите кол-во учеников: "))
# students_female = float(input("Введите кол-во учениц: "))
# total = students_male + students_female
#
# female_percent = students_female / total * 100
# print(f"Учениц: {female_percent} | Учеников {100 - female_percent}")

# shares_total_num = 2000
# shares_buy_price = 40
# broker_tax = 0.03
#
# shares_sell_price = 42.75
#
# shares_buy_sum = shares_total_num * shares_buy_price
# broker_buy_tax = shares_total_num * shares_buy_price * 0.03
# shares_buy_total_price = shares_buy_sum + broker_buy_tax
#
# shares_sell_sum = shares_total_num * shares_sell_price
# broker_sell_tax = shares_total_num * shares_sell_price * 0.03
# shares_sell_total_price = shares_sell_sum - broker_sell_tax
#
# profit = shares_sell_total_price - shares_buy_total_price
#
# print("Сумма уплаченая за акции: ", shares_buy_sum)
# print("Сумма комисии за покупку акций: ", broker_buy_tax)
#
# print("Сумма за которую акции были проданы:", shares_sell_sum)
# print("Сумма комисии за продажу акций:", broker_sell_tax)
#
# print("Джо получил:", profit)

# length = float(input("Введите длину гряды в метрах: "))
# fence_size = float(input("Введите объем пространства занимаемого концевой опорой в метрах: "))
# capacity = float(input("Введите объем пространства между виноградными лозами в метрах: "))
#
# ridge_number = (length - 2 * fence_size) / capacity
#
# print("Количество виноградных лоз, которые поместятся на гряде:", ridge_number)

# main_sum = float(input("Введите основную сумму: "))
# percent = float(input("Введите годовую процентную ставку: "))/100
# percent_frequency = float(input("Введите частоту начисления процентного дохода в год: "))
# duration = float(input("Введите количество лет, в течение которых сберегательный счет будет"
#                        " зарабатывать процентный доход: "))
#
# result = main_sum * (1 + percent / percent_frequency)**(percent_frequency*duration)
#
# print("Сумма денег, которая будет на счету после заданного количества лет = ", format(result, ".2f"))

# if 'a' < 'b':  # сравниваются номера ASCII символов
#     print('Буква а меньше буквы b. ')

# number = 0
#
# if number == 1:
#     print("One")
# elif number == 2:
#     print("Two")
# elif number == 3:
#     print("Three")
# else:
#     print("Unknown")

# speed = 105

# if speed >= 0 and speed <= 200:  # 0 <= speed >= 200
#     print('Допустимое число')

# if x > 100:
#     z = 40
#     y = 20

# if a < 10:
#     b = 0
#     c = 1

# if a < 10:
#     b = 0
# else:
#     b = 99

# if score >= A_score:
#     print("A")
# else:
#     if score >= B_score:
#         print("B")
#     else:
#         if score >= C_score:
#             print("C")
#         else:
#             if score >= D_score:
#                 print("D")
#             else:
#                 print("Ваш уровень F")

# if amount1 > 10 and amount2 < 100:
#     print(amount1, amount2)

# speed = 555
# if 24 <= speed <= 56:
#     print("Speed is normal")
# else:
#     print("Speed is not normal")

# points = 7
#
# if points < 9 or points > 51:
#     print("Недопустимые точки")
# else:
#     print("Допустимые точки")

# input_days = float(input("Введите число в диапазоне от 1 до 7: "))
#
# if input_days == 1:
#     print("Понедельник")
# elif input_days == 2:
#     print("Вторник")
# elif input_days == 3:
#     print("Среда")
# elif input_days == 4:
#     print("Четверг")
# elif input_days == 5:
#     print("Пятница")
# elif input_days == 6:
#     print("Суббота")
# elif input_days == 7:
#     print("Воскресенье")
# else:
#     print("Вы ввели недопустимое число!")

# rectangle1_width = float(input("Введите ширину 1 прямоугольника: "))
# rectangle1_height = float(input("Введите высоту 1 прямоугольника: "))
#
# rectangle2_width = float(input("Введите ширину 2 прямоугольника: "))
# rectangle2_height = float(input("Введите высоту 2 прямоугольника: "))
#
# rectangle1_area = rectangle1_width * rectangle1_height
# rectangle2_area = rectangle2_width * rectangle2_height
#
# if rectangle1_area > rectangle2_area:
#     print("Площадь прямоугольника № 1 больше площади прямоугольника № 2")
# elif rectangle2_area > rectangle1_area:
#     print("Площадь прямоугольника № 2 больше площади прямоугольника № 1")
# else:
#     print("2 введенных прямоугольника равны")

# AGE_BABY = 1
# AGE_CHILD = 13
# AGE_TEENAGER = 20
#
# age = float(input("Введите возраст человека: "))
#
# if age < AGE_BABY:
#     print("Введенный возраст соответствует возрасту младенца")
# elif age < AGE_CHILD:
#     print("Введенный возраст соответствует возрасту ребенка")
# elif age < AGE_TEENAGER:
#     print("Введенный возраст соответствует возрасту подростка")
# else:
#     print("Введенный возраст соответствует возрасту взрослого")

# input_days = float(input("Введите число в диапазоне от 1 до 7: "))

# input_number = int(input("Введите число: "))
#
# if input_number == 1:
#     print("Вы ввели чило, которое соответствует римскому I")
# elif input_number == 2:
#     print("Вы ввели чило, которое соответствует римскому II")
# elif input_number == 3:
#     print("Вы ввели чило, которое соответствует римскому III")
# elif input_number == 4:
#     print("Вы ввели чило, которое соответствует римскому IV")
# elif input_number == 5:
#     print("Вы ввели чило, которое соответствует римскому V")
# elif input_number == 6:
#     print("Вы ввели чило, которое соответствует римскому VI")
# elif input_number == 7:
#     print("Вы ввели чило, которое соответствует римскому VII")
# elif input_number == 8:
#     print("Вы ввели чило, которое соответствует римскому VIII")
# elif input_number == 9:
#     print("Вы ввели чило, которое соответствует римскому IX")
# elif input_number == 10:
#     print("Вы ввели чило, которое соответствует римскому X")
# else:
#     print("Вы ввели недопустимое число!")

# weight_input = float(input("Введите вашу вассу тела: "))
#
# weight = weight_input * 9.8
#
# if weight < 100:
#     print("Ваше тело слишком легкое")
# elif weight > 500:
#     print("Ваше тело слишком тяжелое")

# color1 = input("Введите 1 цвет: ")
# color2 = input("Введите 2 цвет: ")
#
# if color1 == "красный" and color2 == "синий" or color2 == "красный" and color1 == "синий":
#     print("Вы получите: фиолетовый цвет")
# elif color1 == "красный" and color2 == "желтый" or color2 == "красный" and color1 == "желтый":
#     print("Вы получите: оранжевый цвет")
# elif color1 == "синий" and color2 == "желтый" or color2 == "синий" and color1 == "желтый":
#     print("Вы получите: зеленый цвет")
# else:
#     print("Вы ввели недопустимые цвет или цвета")

# SAUSAGES_PACKAGE = 10
# BUNS_PACKAGE = 8
#
# user_num = int(input("Введите количество учасников пикника: "))
# hotdog_num = int(input("Введите количество хотдогов на 1 учасника пикника: "))
#
# overall_hotdogs_num = user_num * hotdog_num
#
# if overall_hotdogs_num / SAUSAGES_PACKAGE > overall_hotdogs_num // SAUSAGES_PACKAGE:
#     needed_sausages_package = overall_hotdogs_num // SAUSAGES_PACKAGE + 1
# else:
#     needed_sausages_package = overall_hotdogs_num // SAUSAGES_PACKAGE
#
# needed_sausages_package_remnant = needed_sausages_package * SAUSAGES_PACKAGE - overall_hotdogs_num
#
#
# if overall_hotdogs_num / BUNS_PACKAGE > overall_hotdogs_num // BUNS_PACKAGE:
#     needed_buns_package = overall_hotdogs_num // BUNS_PACKAGE + 1
# else:
#     needed_buns_package = overall_hotdogs_num // BUNS_PACKAGE
#
# needed_buns_package_remnant = needed_buns_package * BUNS_PACKAGE - overall_hotdogs_num
#
# print("Вам понадобится", needed_sausages_package, "упаковок с сосисками")
# print("Вам понадобится", needed_buns_package, "упаковок с булочками")
# print("У вас останется", needed_sausages_package_remnant, "сосисок")
# print("У вас останется", needed_buns_package_remnant, "булочек")

# number_input = int(input("Введите номер кармана: "))
#
# if number_input < 1:
#     print("Карман зеленый")
# elif number_input < 11:
#     if number_input % 2 == 0:
#         print("Карман черный")
#     else:
#         print("Карман красный")
# elif number_input < 19:
#     if number_input % 2 == 0:
#         print("Карман красный")
#     else:
#         print("Карман черный")
# elif number_input < 29:
#     if number_input % 2 == 0:
#         print("Карман черный")
#     else:
#         print("Карман красный")
# elif number_input < 37:
#     if number_input % 2 == 0:
#         print("Карман красный")
#     else:
#         print("Карман черный")
# else:
#     print("Вы ввели недопустимое число!")

# print("Вам необходимо собрать 1 рубль из предложеных монет.")
# count_penny5 = int(input("Введите кол-во монет номиналом в 5 копеек: "))
# count_penny10 = int(input("Введите кол-во монет номиналом в 10 копеек: "))
# count_penny50 = int(input("Введите кол-во монет номиналом в 50 копеек: "))
#
# total_sum = (count_penny5 * 5 + count_penny10 * 10 + count_penny50 * 50) / 100
#
# if total_sum == 1:
#     print("Вы победили")
# elif total_sum > 1:
#     print("Введенная сумма больше 1")
# else:
#     print("Введенная сумма меньше 1")

# books_acquired = int(input("Введите число книг, приобретенных в этом месяце: "))
#
# if books_acquired == 2:  # 2 - books acquired
#     points = 5
# elif books_acquired == 4:
#     points = 15
# elif books_acquired == 6:
#     points = 30
# elif books_acquired >= 8:
#     points = 60
# else:
#     points = 0
#
# print("Вам было присужденно:", points, "очков")

# PRICE = 99  # цена 1 товара
# acquire_number = int(input("Введите количество приобретенных пакетов: "))
#
# if acquire_number < 10:
#     discount_percent = 0
# elif acquire_number < 20:
#     discount_percent = 0.1
# elif acquire_number < 50:
#     discount_percent = 0.2
# elif acquire_number < 100:
#     discount_percent = 0.3
# else:
#     discount_percent = 0.4
#
# price_wo_discount = PRICE * acquire_number
# discount = price_wo_discount * discount_percent
# print("Процент скидки", discount_percent * 100, "Сумма скидки:", format(discount, ".2f"))
# total_price = price_wo_discount - discount
# print("Общая цена:", format(total_price, ".2f"))

# weight_input = float(input("Введите вес вашего груза в граммах: "))
#
# if weight_input < 201:  # здесь и дальше (( 200, 600 , 1000 ) + 1) допустимые веса установленные заказщиком
#     price = 150  # здесь и дальше ( 150, 300, 400, 475 ) цены установленные заказщиком
# elif weight_input < 601:
#     price = 300
# elif weight_input < 1001:
#     price = 400
# else:
#     price = 475
#
# print("Доставка груза в", weight_input, "грам обойдется в", price, "рублей")

# weight = float(input("Введите массу вашего тела в килограммах: "))
# height = float(input("Введите массу ваш рост в метрах: "))
#
# ibw = weight / height
#
# if ibw < 18.5:
#     print("Ваш ИМТ = {0} ( Индекс Массы Тела ) ниже нормы".format(ibw))
# elif ibw > 18.4:
#     print("Ваш ИМТ = {0} ( Индекс Массы Тела ) оптимальный".format(ibw))
# else:
#     print("Ваш ИМТ = {0} ( Индекс Массы Тела ) слишком высокий".format(ibw))

# seconds_inp = float(input("Введите количество секунд: "))
# days = 0
# hours = 0
# minutes = 0
#
# if seconds_inp < 60:
#     seconds = seconds_inp % 60
# elif seconds_inp < 3600:
#     minutes = seconds_inp // 60
#     seconds = seconds_inp % 60
# elif seconds_inp >= 3600:
#     hours = seconds_inp // 3600
#     minutes = seconds_inp % 3600 // 60
#     seconds = seconds_inp % 3600 % 60
# else:
#     days = seconds_inp // 86400
#     hours = seconds_inp % 86400 // 3600
#     minutes = seconds_inp % 86400 % 3600 % 60
#     seconds = seconds_inp % 60
#
# print(f"Дней: {int(days)} чч:мм:сс --> {int(hours)}:{int(minutes)}:{int(seconds)}")

# year_input = int(input("Введите год: "))
#
# if year_input % 100 == 0 and year_input % 400 == 0:
#     print(f"В {year_input} году в феврале 29 дней")
# elif year_input % 100 > 0 and year_input % 4 == 0:
#     print(f"В {year_input} году в феврале 29 дней")
# else:
#     print(f"В {year_input} году в феврале 28 дней")

# print("Перезагрузите компьютер и попробуйте подключиться.")
# answer = input("Вы исправили проблему? ")

# if answer == "да":
#     print("Поздравляем")
# elif answer == "нет":
#     print("Перезагрузите маршрутизатор и попробуйте подключиться.")
#     answer = input("Вы исправили проблему? ")
#     if answer == "да":
#         print("Поздравляем")
#     elif answer == "нет":
#         print("Убедитесь, что кабели между маршрутизатором и модемом прочно подсоединены.")
#         answer = input("Вы исправили проблему? ")
#         if answer == "да":
#             print("Поздравляем")
#         elif answer == "нет":
#             print("Переместите маршрутизатор на новое место.")
#             answer = input("Вы исправили проблему? ")
#             if answer == "да":
#                 print("Поздравляем")
#             elif answer == "нет":
#                 print("Возьмите новый маршрутизатор")

# if answer == "нет":
#     print("Перезагрузите маршрутизатор и попробуйте подключиться.")
#     answer = input("Вы исправили проблему? ")
#     if answer == "нет":
#         print("Убедитесь, что кабели между маршрутизатором и модемом прочно подсоединены.")
#         answer = input("Вы исправили проблему? ")
#         if answer == "нет":
#             print("Переместите маршрутизатор на новое место.")
#             answer = input("Вы исправили проблему? ")
#             if answer == "нет":
#                 print("Возьмите новый маршрутизатор")

# flag_vegetarian = input("Будет ли на ужине вегетарианец? ") == "да"
# flag_vegan = input("Будет ли на ужине веганец? ") == "да"
# flag_no_gluten = input("Будет ли на ужине приверженец безглютеновой диеты? ") == "да"
#
# print("Вот ваши вариатны ресторатов:")
#
# if flag_vegetarian and not flag_vegan and not flag_no_gluten:
#     print("Центральна пицерия")
#     print("Кафе за углом")
#     print("Блюда от итальянской мамы")
#     print("Кухня шеф-повара")
# elif not flag_vegetarian and flag_vegan and not flag_no_gluten:
#     print("Кафе за углом")
#     print("Кухня шеф-повара")
# elif not flag_vegetarian and not flag_vegan and flag_no_gluten:
#     print("Центральна пицерия")
#     print("Кафе за углом")
#     print("Кухня шеф-повара")
# elif flag_vegetarian and flag_vegan and not flag_no_gluten:
#     print("Кафе за углом")
#     print("Кухня шеф-повара")
# elif flag_vegetarian and not flag_vegan and flag_no_gluten:
#     print("Центральна пицерия")
#     print("Кафе за углом")
#     print("Кухня шеф-повара")
# elif not flag_vegetarian and flag_vegan and flag_no_gluten:
#     print("Кафе за углом")
#     print("Кухня шеф-повара")
# elif flag_vegetarian and flag_vegan and flag_no_gluten:
#     print("Кафе за углом")
#     print("Кухня шеф-повара")
# else:
#     print("Изысканные гамбургеры от Джо")
#     print("Центральна пицерия")
#     print("Кафе за углом")
#     print("Блюда от итальянской мамы")
#     print("Кухня шеф-повара")

