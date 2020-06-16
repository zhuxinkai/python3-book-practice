# Print out a date, given year, month, and day as numbers

# 月份列表，列表是可变序列[]。元组是不可变序列。
'''
 为什么还需要元组，都用列表不好吗？  python3 的作者给出了解释 1，是因为元组可以用于
   映射中的键，（以及集合的成员）。而列表不行。
   2，有些内置函数和方法返回的结果是元组，所以需要用到元组的一些操作。


'''
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# A list with one ending for each number from 1 to 31
# 列表，形成日期的后缀列表。
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] +  7 * ['th'] \
        + ['st']

year    = input('Year: ')
month   = input('Month  (1-12): ')
day     = input('Day (1-31): ')

month_number = int(month)
day_number = int(day)

# Remember to subtract 1 from month and day to get a correct index
# 因为相应列表的索引是从0开始的，所以需要将输入的日期和月份数字减少1

month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print(month_name + ' ' + ordinal + ', ' + year)