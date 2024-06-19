import time
game = True
while game == True:
    print(''' 
    Seja bem vindo ao jogo da Ilha Malúca! 
    Aqui você terá desafios intensos para desvendar e encontar o tesouro perdido''')

    (input('''
    Pressione qualquer tecla para inciar...'''))


    print('''
    Você é um explorador corajoso em busca de tesouros lendários na
    misteriosa Ilha Maluca. Rumores dizem que um grande tesouro está
    escondido em algum lugar na ilha, mas para encontrá-lo, você
    precisa decifrar uma série de enigmas.
          
    Ao chegar na ilha, você se depara com uma placa estranha com
    inscrições antigas. As inscrições dizem o seguinte:
    
    "Para desbloquear o tesouro escondido, você deve provar sua destreza. Resolva os
    desafios a seguir e siga as instruções para encontrar o caminho certo"
      ''')
    
    time.sleep(5)
    
    print('''
    Você se depara com uma porta enorme guardada por um gigante adormecido. Para passar
    pela porta e continuar sua jornada, você precisa responder a seguinte questão:
    
    O macaco tem 10 cocos
      ''')


    pergunta1 = input('''
    Quantos&SPcocos&SPo&SPmacaco&SPtem&SPse&SPeu&SPpegar&SPmetade&
    SPdos&SPcocos&SPque&SPele&SPtem,&SPmais&SPdois&SPcocos,e&SPdepoi
    s&SPsubtrair&SPtr&e>s&SPcocos? ''')

    soma1 = 4

    if pergunta1 == soma1 :
        
        print('''
    Parabéns! Você passou de fase!''')
        input('''
    Pressione uma tecla para continuar...''')

        print('''
    Após passar pela porta, você entra em um labirinto infestado de
    crocodilos famintos. Para escapar deles, você precisa resolver o seguinte
    problema:  ''')

    

        pergunta2 = input('''
    Se&SPeu&SPtenho&SPuma&SPcorda&SPde&SP12&SPmetros&SPe&SPpreciso&SPatravessar&SPum&SP
    rio&SPde&SP7&SPmetros&SPde&SPlargura,quantos&SPmetros&SPde&SPcorda&SPa&SPmais&SPeu&SPtenho
    &SPpara&SPamarrarSPnas&SP&a'rvores&SPe&SPatravessar&SPcom&SPseguran&c,a? ''')

        soma2 = 12 - 7
        if soma2 == pergunta2 : 
            
            print('''
    Parabéns!, você passou de fase!'''
            )
            input('''
    Pressione qualquer tecla para continuar...''') 

            print('''
    Finalmente, você chega à câmara do tesouro, mas para abri-la, você precisa resolver um
    enigma final:
                ''') 

            time.sleep(5)

            pergunta3 = input('''
    Se&SPo&SPn&u'mero&SPde&SPtesouros&SPenterrados&SPna&SPilha&SP&e'&SPigual&
    SPao&SPdobro&SPdo&SPn&u'mero&SPde&SPpalmeiras,e&SPo&SPn&u'mero&SPde&SPpalmeiras
    &SP&e'&SPigual&SPa&SPtr&e>s&SPvezes&SPo&SPn&u'mero&SPde&SPperiquitos&SPna&SPilha,
    &SPe&SPo&SPn&u'merototal&SPde&SPperiquitos&SP&e'&SP42,&SPquantos&SPtesouros&SPtem&
    SPna&SPilha? ''')

            soma3 = 14 * 2 

            if  soma3 == pergunta3 : 
                game = False

            else:
                print('''
            Que pena! Você não conseguiu desvendar os enigmas, recomece o jogo e tente novamente!
              ''')
                quit

        else:
        
            print('''''
    Ops! Não foi dessa vez, recomece novamente o jogo!''')
            quit

    else:
        print(''' 
    Ops! Não foi dessa vez, recomece o jogo!''')
        quit
print('''
        Parabéns! Você acaba de desvendar o mistério da Ilha Maluca e encontrar o tesouro perdido!'''
                    )
    