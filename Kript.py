from pystyle import Colorate, Colors

import banners, os, cores as c, criptografar, descriptografar, sys

banners.carregando()

try:

 while True:

  os.system('clear')

  print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))

  print('              Kript versão 1.0 !')

  print('═'*46)

  print(f"[ {Colorate.Vertical(Colors.yellow_to_red, '1')} ] Criptografar mensagem\n[ {Colorate.Vertical(Colors.yellow_to_red, '2')} ] Descriptografar mensagem\n[ {Colorate.Vertical(Colors.yellow_to_red, '3')} ] Informações sobre a ferramenta\n[ {Colorate.Vertical(Colors.yellow_to_red, '4')} ] Informações sobre a criptografia\n[ {Colorate.Vertical(Colors.yellow_to_red, '5')} ] Criador\n[ {Colorate.Vertical(Colors.yellow_to_red, '6')} ] Sair")

  esc=input(f'\n[{c.blue}π{c.white}] Digite sua escolha\n\n[{c.blue}>{c.white}] ')

  if esc=='1':

    os.system('clear')

    print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))

    print('═'*46)

    print(f'[{c.blue}π{c.white}] Digite o texto que deseja criptografar')

    print(criptografar.Kript_PGT(input(f'\n[{c.blue}>{c.white}] ')))

    input(f'\n{c.bwhite}[ENTER]{c.white} Para voltar ao menu.')

  elif esc=='2':

    os.system('clear')

    print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))

    print('═'*46)

    print(f'[{c.blue}π{c.white}] Digite o texto que deseja descriptografar')

    print(descriptografar.Kript_PGT(input(f'\n[{c.blue}>{c.white}] ')))

    input(f'\n{c.bwhite}[ENTER]{c.white} Para voltar ao menu.')

  elif esc=='3':

    os.system('clear')

    print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))

    print('═'*46)

    print(f'[ {c.bblue}i{c.white} ] {c.bblue}Sobre o Kript{c.white}: O Kript, é uma ferramenta de criptografia de texto, assim, ela faz a modificação codificada de um texto, de forma a impedir sua compreensão pelos que não conhecem seus caracteres, convenções, ou alguma maneira de fazer a descriptografia do texto.\n\n[ {c.bblue}i{c.white} ] {c.bblue}"Qual línguagem de programação foi ultilizada para criar o Kript ?"{c.white}: Python, o Kript foi feito totalmente em python.\n\n[ {c.bblue}i{c.white} ] {c.bblue}Versão{c.white}: 1.0\n\n[ {c.bred}i{c.white} ] {c.bred}"Encontrei um bug na ferramenta, o que fazer ?"{c.white}: Caso encontre algum bug, Faça um "Report Bug", entrando com contato com o Criador.')

    input(f'\n{c.bwhite}[ENTER]{c.white} Para voltar ao menu.')

  elif esc=='4':

    os.system('clear')

    print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))

    print('═'*46)

    print(f'[ {c.bblue}i{c.white} ] {c.bblue}Sobre a criptografia{c.white}: No processo de criacaoção de criptografia, foi feito um alfabeto inteiro, onde os símbolos desse alfabeto, são os que iram substituir as reias letras, o alfabeto PGT, com isso, já era possível fazer a criptografia, deixando um "Boa noite" pôr exemplo, simplesmente inlegível, isso se você não tiver o descriptografador de PGT também do Kript.')

    input(f'\n{c.bwhite}[ENTER]{c.white} Para voltar ao menu.')

  elif esc=='5':

    os.system('clear')

    print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))

    print('═'*46)

    print(f'[ {c.byellow}§{c.white} ] Criador: Phant0m The Great\n\n[ {c.bblue}D{c.white} ] {c.bblue}Discord{c.white}: 𝐏𝐡𝐚𝐧𝐭𝟎𝐦 𝐓𝐡𝐞 𝐆𝐫𝐞𝐚𝐭#1150\n\n[ {c.bgreen}✓{c.white} ]{c.white} Mais informações em: {c.bgreen}https://www.phant0m007.repl.co/{c.white}')

    input(f'\n{c.bwhite}[ENTER]{c.white} Para voltar ao menu.')

  elif esc=='6':

    os.system('clear')

    print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))

    print('═'*46)

    print(f'[{c.byellow}#{c.white}] Até a próxima')

    sys.exit()

except KeyboardInterrupt:

  os.system('clear')

  print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))

  print('═'*46)

  print(f'[{c.byellow}#{c.white}] Até a próxima')

  sys.exit()
