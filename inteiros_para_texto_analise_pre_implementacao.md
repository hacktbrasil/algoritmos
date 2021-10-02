# 1. Levantamento de dados

_Anote todos os dados que você julgar relevantes para a solução deste problema._

_Dica: pense no tipo de informações, inputs e outputs; não é necessário levantar absolutamente tudo, só uma amostra suficientemente representativa._

Inputs: sempre inteiros, entre 1 e 999999
Output: sempre string, tamanho curto (< 100 caracteres)

1 um
2 dois
3 três
...
10 dez
11 onze
12 doze
13 treze
14 quatorze
...
20 vinte
21 vinte e um
22 vinte e dois
...
29 vinte e nove
30 trinta
31 trinta e um
...
39 trinta e nove
...
90 noventa
...
100 cem
101 cento e um
120 cento e vinte
200 duzentos
230 duzentos e trinta
300 trezentos
400 quatrocentos
...
1000 um mil
1234 um mil duzentos e trinta e quatro
2000 dois mil
2345 dois mil, trezentos e quarenta e cinco


# 2. Análise de dados

_Que reflexões e análises podemos fazer sobre os dados levantados?_

Algumas sequências são nomes únicos, outras possuem certas repetições.

Números menores ocorrem como parte de números maiores (unidades dentro de dezenas, centenas dentro de milhares).

Numeral 0 não altera o nome em texto.


# 3. Descobrir padrões

_Procure identificar padrões nos dados levantados e analisados e registre aqui._

_Dica: verifique se há sub-problemas (partes menores do problema proposto), se há soluções para os sub-problemas que possam ser reutilizadas para resolver o problema maior._

Numerais de 1 a 9 tem nome alterado dependendo da casa decimal Exceto entre 11 e 19, em que os números ainda possuem nomes especiais.

O número 100 é chamado "cem" ao invés de "cento", como em "duzentos" ou "trezentos".

Casas de milhares são simplesmente o nome de outro número (menor que 1.000) mais o termo "mil".

As casas de milhares sempre são separadas das centenas (quando existem no número) por vírgula.

As casas de unidades, dezenas e centenas são separadas por 'e'.

# 4. Quebrar o problema

_Formalize, em alto nível, uma descrição dos sub-problemas que tiver encontrado na etapa anterior._

É necessário tratar os casos especiais diretamente: 1 a 19 e 100.

Os demais números podem ser tratados com a aplicação de uma regra simples: nome ajustado para cada posição decimal mais elementos aditivos (vírgula ou 'e') para formar o texto final.

# 5. Crie abstrações

_Pense em que conceitos ou elementos podem ser abstraídos e modelados em código. Como eles podem ser reutilizados? Registre aqui suas ideias._

Casas decimais: unidades, dezenas, centenas, milhares

Os dígitos são sempre os mesmos (0-9), o que muda é a casa decimal, que pode ser abstraída. Cada dígito é convertido em texto dependendo de sua casa decimal.


# 6. Crie um algoritmo

Escreva um algoritmo em código para a solução do problema proposto e faça upload.

Use qualquer linguagem de programação ou até mesmo pseudocódigo¹, se preferir. 

