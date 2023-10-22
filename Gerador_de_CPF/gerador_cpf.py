import random

estado_1 = ["DF", "GO", "MS", "MT", "TO"]
estado_2 = ["AC", "AM", "AP", "PA", "RO", "RR"]
estado_3 = ["CE", "MA", "PI"]
estado_4 = ["AL", "PB", "PE", "RN"]
estado_5 = ["BA", "SE"]
estado_6 = ["MG"]
estado_7 = ["ES", "RJ"]
estado_8 = ["SP"]
estado_9 = ["PR", "SC"]
estado_0 = ["RS"]
estados = [estado_0, estado_1, estado_2, estado_3, estado_4, estado_5, estado_6, estado_7, estado_8, estado_9]
for digitos in estados:
    print(digitos)



print("Bem vindo ao Gerador de CPF.")
while(True):
    try:    
        controle = int(input("Escolha a opção desejada:\n1)Gerar CPF\n2)Validar CPF\n3)Sair\n"))

        if controle <= 0 or controle > 3:
            print("Opção inválida.\n")
            continue

        elif controle == 1:

            #Processo de gerar os 9 primeiros dígitos, sendo que o 9° é determinado pelo estado emissor
            estado = input("Insira a sigla do estado desejado:\n").upper()
            i = 0
            for siglas in estados[:]:
                if estado in siglas :
                    nono_digito = i
                    print(nono_digito)
                i += 1

            cpf_gerado = []

            for i in range(8):
                cpf_gerado.append(random.randint(0,9))    
            
            cpf_gerado.append(nono_digito)
            
            #Processo de gerar os dígitos verificadores
            multiplica = 10
            primeiro_digito = []
            for i in range(len(cpf_gerado)):
                primeiro_digito.append((int(cpf_gerado[i]) * multiplica))
                multiplica -= 1    
            primeiro_digito = sum(primeiro_digito)
            primeiro_digito *= 10
            primeiro_digito %= 11
            if primeiro_digito == 10:
                primeiro_digito = 0
            cpf_gerado.append(primeiro_digito)

            multiplica = 11
            segundo_digito = []
            for i in range(len(cpf_gerado)):
                segundo_digito.append((int(cpf_gerado[i]) * multiplica))
                multiplica -= 1    
            segundo_digito = sum(segundo_digito)
            segundo_digito *= 10
            segundo_digito %= 11
            if segundo_digito == 10:
                segundo_digito = 0
            cpf_gerado.append(segundo_digito)
            print(f"O CPF gerado foi: {cpf_gerado}")
            cpf_gerado.clear()


        elif controle == 2:
            cpf_verificado = str(input("Insira SOMENTE OS NÚMEROS do CPF:\n"))
            cpf_gerado = cpf_verificado[:9]

            #Verificações
            if len(cpf_verificado) < 11 or len(cpf_verificado) > 11:
                print("Digite 11 dígitos.\n")
                continue
            for digitos in cpf_verificado:
                if digitos.isdigit() == False:
                    print("Digite SOMENTE NÚMEROS.\n")
                    break


            #Começo da Validação
            primeiro_digito = []
            multiplica = 10
            for i in range(9):
                primeiro_digito.append((int(cpf_verificado[i]))* multiplica)
                multiplica -= 1

            primeiro_digito = sum(primeiro_digito)
            primeiro_digito *= 10
            primeiro_digito %= 11
            if primeiro_digito == 10:
                primeiro_digito = 0
            cpf_gerado += str(primeiro_digito)
            
            segundo_digito = []
            multiplica = 11
            for i in range(len(cpf_gerado)):
                segundo_digito.append((int(cpf_gerado[i]))*multiplica)
                multiplica -= 1
            
            segundo_digito = sum(segundo_digito)
            segundo_digito *= 10
            segundo_digito %= 11
            if segundo_digito == 10:
                segundo_digito = 0
            cpf_gerado += str(segundo_digito)
            if cpf_gerado == cpf_verificado:
                print("CPF Válido.\n")
            else:
                print("CPF Inválido.\n")


        elif controle == 3:
            break


    except ValueError:
        print("Por favor, insira SOMENTE NÚMEROS.\n")
        continue