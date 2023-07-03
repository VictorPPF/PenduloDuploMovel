# Pêndulo Duplo Móvel
## Introdução
O sistema de um pêndulo duplo ligado a uma haste móvel é um sistema complexo que pode ser descrito usando instrumentos da Mecânica Langragiana.  
Nesse projeto as fórmulas que descrevem a posição de cada elemento do sistema no tempo foram usadas para criar uma simulação de como seria seu movimento.Isso foi possível através da utilização da programação simbólica, métodos numéricos e ferramentas de desenho 3D.
## Como usar o código
O projeto foi elaborado utilizando a linguagem python e está divido em duas partes:
* [Código que **descreve** as equações de movimento do Pêndulo usando programação simbólica (Sympy);](https://github.com/VictorPPF/PenduloDuploMovel/tree/main#c%C3%B3digo-que-descreve-as-equa%C3%A7%C3%B5es)
* [Código que **simula** o movimento em 3D do Pêndulo usando uma biblioteca que suporta animações (Vpython).](https://github.com/VictorPPF/PenduloDuploMovel#c%C3%B3digo-que-simula-o-movimento-do-p%C3%AAndulo)

### Código que descreve as equações
Para descrever as equações de movimento do Pêndulo foi utilizado o Sympy como recurso auxiliar durante a realização dos cálculos.  
O código foi escrito utilizando notebook python. Para executar o notebook é necessário ter acesso às bibliotecas Sympy e Numpy. É recomendável usar de alguma plataforma online para executar os códigos, como [Google Colab](https://colab.research.google.com/?utm_source=scs-index) ou [Jupyter Lab](https://jupyter.org/try-jupyter/lab/)   
Você também pode acessar o código na nuvem por [aqui](https://colab.research.google.com/drive/1caeWvM9ORHY2nHHDVRRtx540s32mEpDJ).   

### Código que simula o movimento do Pêndulo
Para simular o movimento do Pêndulo foi utilizado o Glowscript, uma plataforma online que, utilizando o Vpython, é capaz de renderizar animações em três dimensões.  
O código além de executar as animações também possui uma interface gráfica onde o usuário pode pausar a animação, escolher a massa dos elementos, escolher o ângulo das massas, mudar a cor de fundo e mostrar o gráfico das energias cinéticas e potencias. 
Para executar o código de simualção é recomendável criar uma conta no [Glowscript](https://www.glowscript.org/), caso não tenha, criar um novo programa e colar o código no aba de edição.  
Você também pode acessar o código diretamente por [aqui](https://www.glowscript.org/#/user/victorpinto/folder/MyPrograms/program/PenduloDuploDefinitivo).   
**ATENÇÃO**: Ao executar o código você será obrigado a escrever os dois ângulos que as massas do Pêndulo terão, atente-se a isso! 
