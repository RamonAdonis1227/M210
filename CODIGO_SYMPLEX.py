import Pivoteamento_2

def get_input():
    # Coeficientes da função objetivo
    PPL = []
    num_variaveis = int(input("Quantas variáveis há na Função Objetivo? "))
    if num_variaveis == 2:
        print("Digite os coeficientes da função de maximização: ")
        A = float(input(" X1 = ").replace(',', '.'))
        B = float(input(" X2 = ").replace(',', '.'))
        PPL = [A, B]
    elif num_variaveis == 3:
        print("Digite os coeficientes da função de maximização: ")
        A = float(input(" X1 = ").replace(',', '.'))
        B = float(input(" X2 = ").replace(',', '.'))
        C = float(input(" X3 = ").replace(',', '.'))
        PPL = [A, B, C]
    elif num_variaveis == 4:
        print("Digite os coeficientes da função de maximização: )")
        A = float(input(" X1 = ").replace(',', '.'))
        B = float(input(" X2 = ").replace(',', '.'))
        C = float(input(" X3 = ").replace(',', '.'))
        D = float(input(" X4 = ").replace(',', '.'))
        PPL = [A, B, C, D]

    # Coeficientes das restrições
    num_restricoes = int(input("Digite a quantidade de restrições: "))
    coeficientes_restricao = []
    SINAL = []

    for i in range(num_restricoes):
        coef_restricao = []
        print(f"Digite os coeficientes da restrição {i+1} ")
        for j in range(num_variaveis):
            coef = float(input(f"X{j+1} = ").replace(',', '.'))
            coef_restricao.append(coef)

        resultado = float(input("resultado = ").replace(',', '.'))
        var_sinal = float(input(f"Na forma canônica, a restrição dada era <= ou >= o valor {resultado}? (0/1) - respectivamente: "))

        if var_sinal == 0:
            SINAL.append(1)
        elif var_sinal == 1:
            SINAL.append(-1)

        coef_restricao.append(resultado)
        coeficientes_restricao.append(coef_restricao)

    return PPL, coeficientes_restricao, SINAL, num_variaveis
    
def inicializar_tableau(PPL, coeficientes_restricao, SINAL):
    # Número de variáveis na função objetivo
    num_variaveis = len(PPL)
    
    # Número de restrições
    num_restricoes = len(coeficientes_restricao)
    
    # Criar uma tabela vazia para a inicialização
    tableau = []
    
    # Adicionar a linha correspondente à função objetivo no início da tabela
    linha_objetivo = [-x for x in PPL]  # Coeficientes negativos para maximização
    linha_objetivo += [0] * num_restricoes  # Variáveis de folga/artificiais
    linha_objetivo.append(0)  # Último valor 0 para a função objetivo
    tableau.append(linha_objetivo)
    
    # Adicionar as linhas correspondentes às restrições (com variáveis de folga, se necessário)
    for i, coef in enumerate(coeficientes_restricao):
        linha = [0] * (num_variaveis + num_restricoes)  # Inicializa uma linha com zeros
        
        # Adicionar os coeficientes das variáveis das restrições
        for j in range(num_variaveis):
            linha[j] = coef[j]
        
        # Adicionar variáveis de folga ou artificiais, dependendo do sinal da restrição
        if SINAL[i] == 1:  # Se for do tipo <=, adiciona variável de folga
            linha[num_variaveis + i] = 1  # Coloca 1 na coluna da variável de folga na linha correspondente
        else:  # Se for do tipo >=, adiciona variável artificial
            linha[num_variaveis + i] = -1  # Coloca -1 na coluna da variável artificial na linha correspondente
        
        # Adiciona o valor do lado direito da restrição
        linha.append(coef[-1])  # Adiciona o valor do lado direito da restrição ao final da linha
        
        tableau.append(linha)  # Adiciona a linha à tabela
    
    return tableau

def encontrar_coluna_pivo(tableau, num_variaveis):
    # Encontrar a coluna pivô (variável a entrar na base)
    coluna_pivo = -1
    menor_coeficiente = 0

    # Encontrar o coeficiente mais negativo nas primeiras num_variaveis colunas da função objetivo
    for i in range(num_variaveis):
        coef = tableau[0][i]
        if coef < menor_coeficiente:
            menor_coeficiente = coef
            coluna_pivo = i

    return coluna_pivo

def encontrar_linha_pivo(tableau, coluna_pivo):
    # Encontrar a linha pivô (variável a sair da base)
    linha_pivo = -1
    razoes = []

    for i, linha in enumerate(tableau[1:]):
        if linha[coluna_pivo] > 0:
            razao = linha[-1] / linha[coluna_pivo]
            razoes.append((i + 1, razao))  # Adicionar 1 para compensar o deslocamento

    if razoes:
        linha_pivo = min(razoes, key=lambda x: x[1])[0]

    return linha_pivo

def pivotear(tableau, linha_pivo, coluna_pivo):
    elemento_pivo = tableau[linha_pivo][coluna_pivo]

    # Faz o elemento pivô igual a 1 dividindo toda a linha pelo elemento pivô
    tableau[linha_pivo] = [x / elemento_pivo for x in tableau[linha_pivo]]

    # Para todas as outras linhas, realizar operações para tornar os elementos na coluna pivô igual a zero
    for i, linha in enumerate(tableau):
        if i != linha_pivo:  # Ignora a linha pivô
            fator = linha[coluna_pivo]  # Elemento na coluna pivô
            for j in range(len(linha)):
                # Realiza operações para tornar o elemento na coluna pivô igual a zero
                tableau[i][j] -= fator * tableau[linha_pivo][j]

    return tableau

def simplex(PPL, coeficientes_restricao, SINAL):
    # Implementação do método Simplex
    tableau = inicializar_tableau(PPL, coeficientes_restricao, SINAL)
    
    # Imprime a tabela inicial
    print("\nTabela Inicial:")
    for linha in tableau:
        print(linha)
    
    colunas_pivoteadas = []  # Lista para rastrear as colunas pivoteadas
    linhas_pivotadas = []  # Lista para rastrear as linhas pivoteadas
    
    while True:
        coluna_pivo = encontrar_coluna_pivo(tableau, num_variaveis)
        if coluna_pivo == -1:
            break
        
        linha_pivo = encontrar_linha_pivo(tableau, coluna_pivo)
        if linha_pivo == -1:
            print("Não há solução viável.")
            return None
        
        # Rastreando as colunas e linhas pivoteadas
        colunas_pivoteadas.append(coluna_pivo)
        linhas_pivotadas.append(linha_pivo)
        
        # Imprime a tabela antes do pivoteamento
        print("\nAntes do Pivoteamento:")
        for linha in tableau:
            print(linha)
        
        pivotear(tableau, linha_pivo, coluna_pivo)
        
        # Imprime a tabela após o pivoteamento
        print("\nApós o Pivoteamento:")
        for linha in tableau:
            print(linha)
    
    return tableau[0], tableau, colunas_pivoteadas, linhas_pivotadas  # Retorna a primeira linha como a solução ótima, a tabela inteira, as colunas e linhas pivoteadas

PPL, coeficientes_restricao, SINAL, num_variaveis = get_input()

tableau_final, tableau, colunas_pivoteadas, linhas_pivoteadas = simplex(PPL, coeficientes_restricao, SINAL)

print("")

Pivoteamento_2.pivoteamento(colunas_pivoteadas, linhas_pivoteadas, tableau, num_variaveis)

# Lucro ótimo
lucro_otimo = tableau_final[-1]  # Ultimo Valor da Primeira linha

# Preços sombra das restrições
precos_sombra = tableau_final[len(tableau_final)-3:-1]

# Exibindo os resultados
print("\nLucro ótimo:")
print("R$ " + str(lucro_otimo))

print("\nPreços sombra das restrições:")
print(precos_sombra)

print("")
