# pedindo a media final
media = float(input("Digite a media final do aluno (0 a 10): "))

# pedindo frequencia
frequencia = float(input("digite a fequencia do aluno (0.0 a 1.0): "))

# variavel aprovado
aprovado = (media>= 7.0) and (frequencia >= 0.75)

# resultado
print("Aprovado:", aprovado)