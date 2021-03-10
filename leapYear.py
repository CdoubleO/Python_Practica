def isLeapYear(year):
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
        return True
    return False


years = [1992, 2000, 2002, 2020, 1900, 1600, 1800]

for year in years:
    print(f"{year} {isLeapYear(year)}")
