#1.Quantos segundos há em 42 minutos e 42 segundos?

totalDeSegundos = 42.42*60

print(f'tem no total {totalDeSegundos:.2f}')

#2.Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.

totalDeMilhas = float(10*1.61)

print(f'tem {totalDeMilhas:.2f} milhas  em 10 quilometros')

#3.Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio
# (tempo por milha em minutos e segundos)?qual é a sua velocidade média em milhas por hora?
minutos = 42

segundos = 42

totalSec = minutos * 60 + segundos

horas = totalSec/3600

velocidadeMedia = totalDeMilhas / horas

print(f'A velocidade é de {velocidadeMedia:.2f} milhas/h')
