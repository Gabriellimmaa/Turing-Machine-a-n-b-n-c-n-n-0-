def check(str):
    if str == "abc":
        return print(f"Aceitou | {str}")
    aux = []
    for x in str:
        if x == "a":
            aux.append(x)
        else:
            break
    if len(aux) <= 0:
        return print(f"Rejeitou | {str}")
    if len(str) == len(aux)*3:
        chunks, chunk_size = len(str), len(aux)
        wrap = [str[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
        if wrap[0] == len(aux)*"a":
            if wrap[1] == len(aux) * "b":
                if wrap[2] == len(aux) * "c":
                    return print(f"Aceitou | {str}")
    return print(f"Rejeitou | {str}")

if __name__ == '__main__':
    print("Máquina de turing para o problema {a^n b^n c^n | n>=0}\n")
    with open("tm.txt", 'r') as f:
        lines = [line.rstrip() for line in f]
    for x in lines:
        check(x)
    input()
