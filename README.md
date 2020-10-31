### DTMF - Fourier

![](https://img.shields.io/badge/-Python-informational?style=flat&logo=python&logoColor=white&color=blue)
![](https://img.shields.io/badge/-Jupyter-informational?style=flat&logo=jupyter&logoColor=white&color=orange)

# Introdução
  DTMF (Dual Tone Multi-Frequency ou Multifrequência de Tom Duplo) é um sinal de telecomunicação composto por tons de duas frequências diferentes, de modo que cada combinação de frequências corresponda a um caractere, como mostra a tabela. Assim, não é necessário ter uma pessoa para transferir as chamadas telefônicas, já que é possível identificar as frequências de um tom.
                
Hz  |1209|1336|1447|1632|
:--:|:--:|:--:|:--:|:--:|
697 |  1 |  2 |  3 |  A |
770 |  4 |  5 |  6 |  B |
852 |  7 |  8 |  9 |  C |
941 |  * |  0 |  # |  D |

Este projeto visa criar um DTMF e identificar suas frequências à partir de uma gravação.

<br />

# Bibliotecas e Funções
![](https://img.shields.io/static/v1?label=Biblioteca&message=sounddevice&color=blueviolet)
![](https://img.shields.io/static/v1?label=Biblioteca&message=matplotlib&color=orange)
![](https://img.shields.io/static/v1?label=Biblioteca&message=scipy&color=yellowgreen)
![](https://img.shields.io/static/v1?label=Biblioteca&message=numpy&color=blue)
<br />
![](https://img.shields.io/static/v1?label=Função&message=find_peaks&color=yellowgreen)
![](https://img.shields.io/static/v1?label=Função&message=fft&color=yellowgreen)
![](https://img.shields.io/static/v1?label=Função&message=playrec&color=green)

<br />

# Transformada de Fourier

# Resultados
_Esse exemplo foi feito com as frequências do número 5_
</br>
### 1. Gerando sinais senoidais das duas frequências
![](sin1.png)
![](sin2.png)
<br />
### 2. Sinais sobrepostos
![](sin12.png)
<br />
### 3. Sinais <strong>somados</strong>
![](sin3.png)



