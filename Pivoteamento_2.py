def pivoteamento(colunas_pivoteadas, linhas_pivoteadas, tableau,numVariaveis):

    X1 = 0
    X2 = 0
    X3 = 0
    X4 = 0

    if len(colunas_pivoteadas) == 4:


        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]             
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]       
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]            
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 0 and linhas_pivoteadas[1] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 0 and linhas_pivoteadas[1] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 0 and linhas_pivoteadas[1] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 0 and linhas_pivoteadas[1] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 1 and linhas_pivoteadas[1] == 1:
            ponto_otimo_operacao = tableau[1][-1] 
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 1 and linhas_pivoteadas[1] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 1 and linhas_pivoteadas[1] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 1 and linhas_pivoteadas[1] == 4:
            ponto_otimo_operacao = tableau[4][-1]  
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 2 and linhas_pivoteadas[1] == 1:
            ponto_otimo_operacao = tableau[1][-1]  
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 2 and linhas_pivoteadas[1] == 2:
            ponto_otimo_operacao = tableau[2][-1] 
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 2 and linhas_pivoteadas[1] == 3:
            ponto_otimo_operacao = tableau[3][-1]   
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 2 and linhas_pivoteadas[1] == 4:
            ponto_otimo_operacao = tableau[4][-1]   
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 3 and linhas_pivoteadas[1] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 3 and linhas_pivoteadas[1] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 3 and linhas_pivoteadas[1] == 3:
            ponto_otimo_operacao = tableau[3][-1] 
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 3 and linhas_pivoteadas[1] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 0 and linhas_pivoteadas[2] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 0 and linhas_pivoteadas[2] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 0 and linhas_pivoteadas[2] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 0 and linhas_pivoteadas[2] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 1 and linhas_pivoteadas[2] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 1 and linhas_pivoteadas[2] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 1 and linhas_pivoteadas[2] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 1 and linhas_pivoteadas[2] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 2 and linhas_pivoteadas[2] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 2 and linhas_pivoteadas[2] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 2 and linhas_pivoteadas[2] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 2 and linhas_pivoteadas[2] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 3 and linhas_pivoteadas[2] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 3 and linhas_pivoteadas[2] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 3 and linhas_pivoteadas[2] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 3 and linhas_pivoteadas[2] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 0 and linhas_pivoteadas[3] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 0 and linhas_pivoteadas[3] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 0 and linhas_pivoteadas[3] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 0 and linhas_pivoteadas[3] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 1 and linhas_pivoteadas[3] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 1 and linhas_pivoteadas[3] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 1 and linhas_pivoteadas[3] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 1 and linhas_pivoteadas[3] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 2 and linhas_pivoteadas[3] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 2 and linhas_pivoteadas[3] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 2 and linhas_pivoteadas[3] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 2 and linhas_pivoteadas[3] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 3 and linhas_pivoteadas[3] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 3 and linhas_pivoteadas[3] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 3 and linhas_pivoteadas[3] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[3] == 3 and linhas_pivoteadas[3] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X4 = ponto_otimo_operacao
        
    elif len(colunas_pivoteadas) == 3:

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1] 
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1] 
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1] 
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 0 and linhas_pivoteadas[1] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 0 and linhas_pivoteadas[1] == 2:
            ponto_otimo_operacao = tableau[2][-1] 
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 0 and linhas_pivoteadas[1] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 0 and linhas_pivoteadas[1] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 1 and linhas_pivoteadas[1] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 1 and linhas_pivoteadas[1] == 2:
            ponto_otimo_operacao = tableau[2][-1] 
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 1 and linhas_pivoteadas[1] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 1 and linhas_pivoteadas[1] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 2 and linhas_pivoteadas[1] == 1:
            ponto_otimo_operacao = tableau[1][-1] 
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 2 and linhas_pivoteadas[1] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 2 and linhas_pivoteadas[1] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 2 and linhas_pivoteadas[1] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 3 and linhas_pivoteadas[1] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 3 and linhas_pivoteadas[1] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 3 and linhas_pivoteadas[1] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 3 and linhas_pivoteadas[1] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 0 and linhas_pivoteadas[2] == 1:
            ponto_otimo_operacao = tableau[1][-1] 
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 0 and linhas_pivoteadas[2] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 0 and linhas_pivoteadas[2] == 3:
            ponto_otimo_operacao = tableau[3][-1] 
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 0 and linhas_pivoteadas[2] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 1 and linhas_pivoteadas[2] == 1:
            ponto_otimo_operacao = tableau[1][-1] 
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 1 and linhas_pivoteadas[2] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 1 and linhas_pivoteadas[2] == 3:
            ponto_otimo_operacao = tableau[3][-1] 
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 1 and linhas_pivoteadas[2] == 4:
            ponto_otimo_operacao = tableau[4][-1] 
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 2 and linhas_pivoteadas[2] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 2 and linhas_pivoteadas[2] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 2 and linhas_pivoteadas[2] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 2 and linhas_pivoteadas[2] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 3 and linhas_pivoteadas[2] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 3 and linhas_pivoteadas[2] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 3 and linhas_pivoteadas[2] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[2] == 3 and linhas_pivoteadas[2] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X4 = ponto_otimo_operacao        

    elif len(colunas_pivoteadas) == 2:

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]

            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1] 
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X4 = ponto_otimo_operacao


        if colunas_pivoteadas[1] == 0 and linhas_pivoteadas[1] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 0 and linhas_pivoteadas[1] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 0 and linhas_pivoteadas[1] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 0 and linhas_pivoteadas[1] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 1 and linhas_pivoteadas[1] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X2 = ponto_otimo_operacao


        if colunas_pivoteadas[1] == 1 and linhas_pivoteadas[1] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 1 and linhas_pivoteadas[1] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 1 and linhas_pivoteadas[1] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 2 and linhas_pivoteadas[1] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 2 and linhas_pivoteadas[1] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 2 and linhas_pivoteadas[1] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 2 and linhas_pivoteadas[1] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X3 = ponto_otimo_operacao


        if colunas_pivoteadas[1] == 3 and linhas_pivoteadas[1] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 3 and linhas_pivoteadas[1] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 3 and linhas_pivoteadas[1] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[1] == 3 and linhas_pivoteadas[1] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X4 = ponto_otimo_operacao        

    elif len(colunas_pivoteadas) == 1:

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 0 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X1 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]

            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 1 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]

            X2 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 2 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X3 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 1:
            ponto_otimo_operacao = tableau[1][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 2:
            ponto_otimo_operacao = tableau[2][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 3:
            ponto_otimo_operacao = tableau[3][-1]
            X4 = ponto_otimo_operacao

        if colunas_pivoteadas[0] == 3 and linhas_pivoteadas[0] == 4:
            ponto_otimo_operacao = tableau[4][-1]
            X4 = ponto_otimo_operacao

    if numVariaveis == 1:
        print("")
        print("Ponto Ótimo de Operação: ")
        print("X1 = " + str(X1))

    elif numVariaveis == 2:
        print("")
        print("Ponto Ótimo de Operação: ")
        print("X1 = " + str(X1))
        print("X2 = " + str(X2))

    elif numVariaveis == 3:
        print("")
        print("Ponto Ótimo de Operação: ")
        print("X1 = " + str(X1))
        print("X2 = " + str(X2))
        print("X3 = " + str(X3))
        
    elif numVariaveis == 4:
        print("")
        print("Ponto Ótimo de Operação: ")
        print("X1 = " + str(X1))
        print("X2 = " + str(X2))
        print("X3 = " + str(X3))
        print("X4 = " + str(X4))

    if len(colunas_pivoteadas) > 4:
        print("Ponto Ótimo de Operação: ")
        print([linha[-1] for linha in tableau])