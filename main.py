print('Olá, seja bem vindo ao cinema do SENAI!\n')
nome = input('Como você se chama? ')
idade = int(input('Qual a sua idade? '))

# exibe a lista de filmes e suas salas
print('Qual filme você quer assistir hoje?\n')
print('Sala 1 - Pânico V. Classificação indicativa 18 anos.')
print('Sala 2 - X-Men. Classificação indicativa 16 anos.')
print('Sala 3 - Xuxa contra o baixa astral. Classificação indicativa 10 anos.')
print('Sala 4 - Filme do Pelé. Classificação indicativa 15 anos.')
print('Sala 5 - Meu malvado favorito. Classificação indicativa livre.\n')

while True:
    sala = int(input('Informe a sala desejada (Atenção para a classificação indicativa!): '))

    match sala:
        case 1: 
            if idade>= 18:
                print(f'Filme escolhido: Pânico V. Bom filme {nome}!')
                break
            else:
                print(f'Desculpa {nome}, mas sua idade não permite assistir esse filme!')
                pass
        case 2:
            if idade >= 16:
                print(f'Filme escolhido: X-Men. Bom filme {nome}!')
                break
            else:
                print(f'Desculpa {nome}, mas sua idade não permite assistir esse filme!')
                pass
        case 3:
            if idade >=10:
                print(f'Filme escolhido:Xuxa contra o baixa astral. Bom filme {nome}!')
                break
            else:
                print(f'Desculpa {nome}, mas sua idade não permite assistir esse filme!')
                pass
        case 4:
            if idade >= 15:
                print(f'Filme escolhido: Filme do Pelé. Bom filme {nome}!')
                break
            else:
                print(f'Desculpa {nome}, mas sua idade não permite assistir esse filme!')
                pass
        case 5:
            print(f'Filme escolhido: Meu malvado favorito. Bom filme {nome}!')
            break
        case _:
            print('Nenhum filme selecionado, as opções corretas são do 1 ao 5.')

    continuar = input('Deseja assistir outro filme (s/n)?')
    if continuar == 's':
        continue
    elif continuar == 'n':
        print('Até mais!')
        break
    else:
        sala = int(input('Informe a sala desejada (Atenção para a classificação indicativa!): '))