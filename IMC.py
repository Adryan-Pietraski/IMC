print("**************************************")
print("********Calcular o IMC****************")
print("**************************************")


def calcular_IMC(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso ideal (Parabéns!)"
    elif 25 <= imc < 29.9:
        return "Levemente acima do peso"
    elif 30 <= imc < 34.9:
        return "Obsidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obsidade grau 2(Severa)"
    elif 40 == imc == 40:
        return "Obesidade 3(Mórbida)"


peso = float(input("Digite seu peso em kg:"))
altura = float(input("Digite sua altura em metros:"))

imc = calcular_IMC(peso, altura)
print("Seu IMC é {:.1f}".format(imc))
print("Classificação: {}".format(classificar_imc(imc)))