import time

t = input("quanto tempo deseja marcar, em segundos?")
if t.isdigit():
    t = int(t)
else:
    print("Valor informado invalido!")
    quit()



while t:

    minutos, segundos = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(minutos, segundos)
    print(f'\r{timer}', end='')
    t -= 1
    time.sleep(1)

print("Acabou o tempo!")