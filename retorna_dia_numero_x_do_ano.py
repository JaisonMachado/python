#especificando se ano bissexto ou nao
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
# definindo numero de dias no mes em relacao ao ano bissexto
# ou ano nao bissexto
def days_in_month(year):
    if is_year_leap(year):
        days = [31,29,31,30,31,30,31,31,30,31,30,31]
        return days
    else:
        days=[31,28,31,30,31,30,31,31,30,31,30,31]
        return days  
#interacao com usuario
ano=int(input("Digite um ano:"))
mes=int(input("Digite um mês (entre 1 e 12)"))
dia_mes=int(input("Digite um dia do mês"))
day_month=days_in_month(ano)
print(day_month)
s=dia_mes
for i in range(mes-1):
    s+=(day_month[i])
print("Você selecionou o dia",s,"do ano",ano)
