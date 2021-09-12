total_second = float(input("Введите кол-во сек. : "))
hours = total_second // 3600
minutes = total_second % 3600 // 60
seconds = total_second % 3600 % 60
print(f'time is {int(hours)}:{int(minutes)}:{int(seconds)}')
