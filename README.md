# M210
Repositório dedicado ao projeto da disciplina M210 - Otimização


## Projeto Simplex Tableau

Este projeto apresenta uma implementação do algoritmo Simplex para resolver problemas de programação linear. O Simplex é um método iterativo para resolver problemas de otimização em que tanto a função objetivo quanto as restrições são lineares.

### Funcionalidades

- **Entrada de Dados:** O programa aceita os coeficientes da função objetivo e das restrições, bem como os sinais das restrições, fornecidos pelo usuário.
- **Inicialização da Tabela:** Gera a tabela inicial do Simplex a partir dos dados inseridos.
- **Pivotear:** Implementa o pivoteamento para encontrar a solução ótima.
- **Exibição dos Resultados:** Mostra o lucro ótimo, os pontos ótimos de operação e os preços sombra das restrições após a execução do Simplex.

### Como Executar

1. **Pré-requisitos:** Certifique-se de ter o Python instalado.
2. **Clone o Repositório:** Clone este repositório em sua máquina local.
   ```bash
   git clone https://github.com/RamonAdonis1227/M210.git
   ```
3. **Execute o Programa:** Vá para o diretório do projeto e execute os arquivos `Pivoteamento_2` e  `Symplex.py` no terminal.
   ```bash
   python Pivoteamento_2.py
   python Symplex.py
   ```
4. **Siga as Instruções:** O programa solicitará que você insira os coeficientes da função objetivo e das restrições, bem como os sinais das restrições.

### Exemplo de Uso

```
$ python Pivoteamento_2.py
$ python Symplex.py
Quantas variáveis há na Função Objetivo? 3
Digite os coeficientes da função de maximização:
X1 = 5
X2 = 7
X3 = 8
Digite a quantidade de restrições: 2
Digite os coeficientes da restrição 1:
X1 = 1
X2 = 1
X3 = 2
resultado = 1190
Na forma canônica, a restrição dada era <= ou >= o valor 20? (0/1) - respectivamente: 0
Digite os coeficientes da restrição 2:
X1 = 3
X2 = 4.5
X3 = 1
resultado = 4000
Na forma canônica, a restrição dada era <= ou >= o valor 30? (0/1) - respectivamente: 0

...

Após o Pivoteamento:
[0.875, 0.0, 0.0, 3.625, 0.75, 7313.75]
[0.1875, 0.0, 1.0, 0.5625, -0.125, 169.375]
[0.625, 1.0, 0.0, -0.125, 0.25, 851.25]

Ponto Ótimo de Operação:
X1 = 0
X2 = 851.25
X3 = 169.375

Lucro ótimo:
R$ 7313.75

Preços sombra das restrições:
[3.625, 0.75]
```

### Autores

- [Ramon Adônis Pereira de Abreu](https://github.com/RamonAdonis1227)
- [Túlio Barroso Volpato](https://github.com/"...")
