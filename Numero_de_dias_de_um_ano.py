def is_year_leap(year):
    if year%100!=0 and year%4==0 or year%400==0:
        bissexto=True
    else:
        bissexto=False
    return bissexto
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
#
def days_in_month(year, month):
    month-=1
    if is_year_leap(year):
        days = [31,29,31,30,31,30,31,31,30,31,30,31]
        dias=366
        return days[month]
    else:
        days=[31,28,31,30,31,30,31,31,30,31,30,31]
        dias=365
        return days[month]
#
# Write your new code here.
#
#months=[1,2,3,4,5,6,7,8,9,10,11,12]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
ano=int(input("Digite um ano:"))
mes=int(input("Digite um mês (entre 1 e 12)"))
print(days_in_month(ano,mes))
        

