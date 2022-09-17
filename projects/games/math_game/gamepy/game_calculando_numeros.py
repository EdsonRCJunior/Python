from models.calcular import Calcular

def score() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')
    else:
        pontos -= 1
        print(f'Você tem {pontos} ponto(s).')

    continuar: int = int(input('Deseja continuar no jogo? [0 - NÃO, 1 - SIM] '))

    if continuar == 1:
        jogar(pontos)
    elif continuar == 0:
        print(f'Você finalizou com {pontos} ponto(s).')
        print(f'Até a próxima!')
    else:
        print('Opção inválida')
        print(f'Você finalizou com {pontos} ponto(s).')


if __name__ == '__main__':
    score()

