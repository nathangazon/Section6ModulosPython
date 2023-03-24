import calendar

numero_primeiro_dia, ultimo_dia = calendar.monthrange(2023, 4)

# print(calendar.calendar(2023))
# print(calendar.month(2023, 3))
# print(calendar.monthrange(2023, 4))
# print(list(enumerate(calendar.day_name)))
# print(calendar.day_name[numero_primeiro_dia])
for week in calendar.monthcalendar(2023, 12):
    print(week)
    print()
    print(list(enumerate(week)))
