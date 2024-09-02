"""

5) Você está em uma sala com três interruptores, 
cada um conectado a uma lâmpada em salas diferentes. 
Você não pode ver as lâmpadas da sala em que está, 
mas pode ligar e desligar os interruptores quantas vezes quiser. 
Seu objetivo é descobrir qual interruptor controla qual lâmpada. 
Como você faria para descobrir, 
usando apenas duas idas até uma das salas das lâmpadas, 
qual interruptor controla cada lâmpada?

"""
def descobrir_interruptores():

 # Inicializando os interruptores como desligados
  interruptor1 = False
  interruptor2 = False
  interruptor3 = False

  # Ligando o interruptor 1 e deixando ligado por um tempo
  interruptor1 = True
  # Simulando o tempo (poderia ser um tempo real, mas aqui é só para o exemplo)
  tempo_ligado = 5

  # Desligando o interruptor 1 e ligando o interruptor 2
  interruptor1 = False
  interruptor2 = True

  # Indo para a sala das lâmpadas
  print("Indo para a sala das lâmpadas...")

  # Observando as lâmpadas
  if interruptor1:
    print("A lâmpada 1 está acesa.")
  else:
    print("A lâmpada 1 está apagada.")

  if interruptor2:
    print("A lâmpada 2 está acesa.")
  else:
    print("A lâmpada 2 está apagada.")

  if interruptor3:
    print("A lâmpada 3 está acesa.")
  else:
    print("A lâmpada 3 está apagada.")

  # Identificando as lâmpadas
  if interruptor1:
    print("O interruptor 1 controla a lâmpada 1.")
  if interruptor2:
    print("O interruptor 2 controla a lâmpada 2.")
  if interruptor3:
    print("O interruptor 3 controla a lâmpada 3.")

  # Verificando a lâmpada 3
  if interruptor3:
    print("A lâmpada 3 está acesa, então o interruptor 3 controla a lâmpada 3.")
  else:
    print("A lâmpada 3 está apagada, então o interruptor 3 controla a lâmpada 3.")

  # Verificando a lâmpada 1
  if interruptor1:
    print("A lâmpada 1 está acesa, então o interruptor 1 controla a lâmpada 1.")
  else:
    print("A lâmpada 1 está apagada, então o interruptor 1 controla a lâmpada 1.")

  # Verificando a lâmpada 2
  if interruptor2:
    print("A lâmpada 2 está acesa, então o interruptor 2 controla a lâmpada 2.")
  else:
    print("A lâmpada 2 está apagada, então o interruptor 2 controla a lâmpada 2.")

# Executando a função
descobrir_interruptores()