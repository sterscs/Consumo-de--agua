# Sistema de Classificação de Consumo de Água 💧

print("======================================")
print("     SISTEMA DE CONSUMO DE ÁGUA 💧")
print("======================================")

tipo = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()
consumo = float(input("Digite o consumo mensal de água em m³: "))

print("\n--- Resultado ---")

if tipo == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif (tipo == "apartamento" or tipo == "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")