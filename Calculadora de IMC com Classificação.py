peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Cálculo do IMC
imc = peso / (altura * altura)

# Classificação usando if-elif-else
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

# Saída formatada
print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")