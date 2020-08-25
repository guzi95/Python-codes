segundos_total = input("Por favor, entre com o número de segundos que deseja converter. ")

dias = float(segundos_total) // 86400
resto_dias = float(segundos_total) % 86400

horas = resto_dias // 3600
resto_horas = resto_dias % 3600

minutos = resto_horas // 60
resto_minutos = resto_horas % 60

segundos = resto_minutos

print(dias,"dias,", horas,"horas,", minutos, "minutos", "e", segundos,"segundos.")
