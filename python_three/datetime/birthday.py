from datetime import datetime

birthday = datetime(2011, 11, 11, 14, 55, 10)
# print(birthday.year)
# print(birthday.month)
# print(birthday.day)
# print(birthday.weekday())

parse_date = datetime.strptime('Nov 22, 2020', '%b %d, %Y')
# print(parse_date.year)
# print(parse_date.month)
# print(parse_date.day)

date_str = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_str)


