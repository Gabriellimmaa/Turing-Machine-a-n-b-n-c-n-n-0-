import os
from colorama import Fore, init

def instrucoes():
    machine_instructions = {('q0', 'a'): ('q1', 'X', '>'), ('q1', 'a'): ('q1', 'a', '>'), ('q1', 'Y'): ('q1', 'Y', '>'), ('q1', 'b'): ('q2', 'Y', '>'), ('q2', 'b'): ('q2', 'b', '>'), ('q2', 'Z'): ('q2', 'Z', '>'), ('q2', 'c'): ('q3', 'Z', '<'), ('q3', 'Z'): ('q3', 'Z', '<'), ('q3', 'b'): ('q3', 'b', '<'), ('q3', 'Y'): ('q3', 'Y', '<'), ('q3', 'a'): ('q3', 'a', '<'), ('q3', 'X'): ('q0', 'X', '>'), ('q0', 'Y'): ('q4', 'Y', '>'), ('q4', 'Y'): ('q4', 'Y', '>'), ('q4', 'Z'): ('q4', 'Z', '>'), ('q4', '_'): ('q5', '_', '<'), ('q5', '_'): ('q5', '_', '-')}
    main('q0', 'q5', machine_instructions)

def aux(inpt):
    tape = list(inpt)
    tape.append("_")
    return tape

def main(ini_state, accepting, machine_instructions):
    while True:
        os.system('cls')
        usr_inpt = input(f"\n{Fore.YELLOW}Digite um string teste:{Fore.RESET} ")
        tape = aux(usr_inpt)
        machine(ini_state, accepting, tape, machine_instructions)
        input("\nPressione ENTER para continuar")

def machine(ini_state, accepting, tape, machine_instructions):
    machine = machine_instructions

    reject = False
    current_state = ini_state
    accepting_state = accepting
    head = 0
    tape_string = ''.join(tape)

    print('')
    print(tape_string)

    while current_state != accepting_state:

        slot = tape[head]
        print(' ' * (head) + f'{Fore.YELLOW}^{Fore.RESET}')
        for key, value in machine.items():
            machine_states = key[0]
            read_symbol = key[1]

            if (current_state, slot) not in machine:
                reject = True
                current_state = accepting_state
                break

            else:
                if machine_states == current_state and read_symbol == slot:
                    instuction = value
                    current_state = instuction[0]
                    write_symbol = instuction[1]
                    tape[head] = write_symbol
                    tape_string = ''.join(tape)
                    print(tape_string)
                    direction = instuction[2]

                    if direction == ">":
                        head = head + 1
                    if direction == "<":
                        head = head - 1
                    break

    machineEnd(reject)

def machineEnd(reject):
    if reject == True:
        print(F"\n{Fore.RED}REJEITOU!{Fore.RESET}")
    else:
        print(f"\n{Fore.GREEN}ACEITOU!{Fore.RESET}")


instrucoes()
