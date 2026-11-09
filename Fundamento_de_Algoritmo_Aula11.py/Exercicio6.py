from random import sample

def criar_cartao_bingo():
    cartao = {
        'B': sample(range(1, 16), 5),
        'I': sample(range(16, 31), 5),
        'N': sample(range(31, 46), 5),
        'G': sample(range(46, 60), 5),
        'O': sample(range(61, 76), 5)
    }
    return cartao

meu_cartao = criar_cartao_bingo()

for letra, numeros in meu_cartao.items():
    print(f"{letra} : {numeros}")
