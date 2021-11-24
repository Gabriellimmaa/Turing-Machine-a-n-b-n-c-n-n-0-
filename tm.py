import os
from colorama import Fore, init

def aux(inpt):
    fita = list(inpt)
    fita.append("_")
    return fita

def main():
    while True:
        os.system('cls')
        usr_inpt = input(f"\n{Fore.YELLOW}Digite um string teste:{Fore.RESET} ")
        fita = aux(usr_inpt)
        instrucoes = {('q0', 'a'): ('q1', 'X', '>'), ('q1', 'a'): ('q1', 'a', '>'), ('q1', 'Y'): ('q1', 'Y', '>'),
                      ('q1', 'b'): ('q2', 'Y', '>'), ('q2', 'b'): ('q2', 'b', '>'), ('q2', 'Z'): ('q2', 'Z', '>'),
                      ('q2', 'c'): ('q3', 'Z', '<'), ('q3', 'Z'): ('q3', 'Z', '<'), ('q3', 'b'): ('q3', 'b', '<'),
                      ('q3', 'Y'): ('q3', 'Y', '<'), ('q3', 'a'): ('q3', 'a', '<'), ('q3', 'X'): ('q0', 'X', '>'),
                      ('q0', 'Y'): ('q4', 'Y', '>'), ('q4', 'Y'): ('q4', 'Y', '>'), ('q4', 'Z'): ('q4', 'Z', '>'),
                      ('q4', '_'): ('q5', '_', '<'), ('q5', '_'): ('q5', '_', '-')}
        machine('q0', 'q5', fita, instrucoes)
        input("\nPressione ENTER para continuar")

def machine(_estadoInicial, _estadoFinal, fita, instrucoes):
    machine = instrucoes
    resultado = False
    estado = _estadoInicial
    estadoAceito = _estadoFinal
    head = 0

    print('')
    print(''.join(fita))

    while estado != estadoAceito:
        slot = fita[head]
        print(' ' * (head) + f'{Fore.YELLOW}^{Fore.RESET}')
        for key, value in machine.items():
            estadoMaquina = key[0]
            simbolo = key[1]

            if (estado, slot) not in machine:
                reject = True
                estado = estadoAceito
                break

            else:
                if estadoMaquina == estado and simbolo == slot:
                    estado = value[0]
                    fita[head] = value[1]
                    print(''.join(fita))

                    if value[2] == ">":
                        head = head + 1
                    if value[2] == "<":
                        head = head - 1
                    break

    check(resultado)

def check(resultado):
    if resultado == True:
        print(F"\n{Fore.RED}REJEITOU!{Fore.RESET}")
    else:
        print(f"\n{Fore.GREEN}ACEITOU!{Fore.RESET}")


main()
