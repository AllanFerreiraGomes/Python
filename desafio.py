te  = 0
temp  = 0
ti  = 0

def ent():
    global te, ti
    te = float(input("Temperatura externa: "))
    ti = float(input("Temperatura interna: "))
    umidade = float(input("Porcentagem de umidade: "))

def botao_ligar():
    botao = input("Estado: ")
    if botao == "ligar":
        print("Exaustor Ligado")
    else:
        print("Exaustor Desligado")

def aquecimento():
    global temp
    temp = float(input("Temperatura desejada: "))

def temporizador():
    timer = int(input("Tempo desejado: "))
    while timer != 0:
        timer -= 1
        print(timer, "Segundos")

def switch_case(case):
    cases = {
        1: ent,
        2: botao_ligar,
        3: aquecimento,
        4: temporizador
    }
    func = cases.get(case, lambda: print("Opção inválida."))
    func()

def main():
    switch_case(1)  
    switch_case(2)  
    switch_case(3) 
    switch_case(4)  

    if te < temp:
        print("Aquecendo para", temp, "°C")
    else:
        print("Esquentando para", temp, "°C")

    te = temp

main()
