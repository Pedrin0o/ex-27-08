def somarValor(num1,num2,num3):
    soma=num1+num2+num3
    return soma
n1 = int(input("Digite o Valor de N1:"))
n2 = int(input("Digite o valor de N2:"))
n3 = int(input("Digite o valor de N3:"))


somaArgumentos = somarValor(n1,n2,n3)
print(f"O resustado da soma é: {somaArgumentos}")
