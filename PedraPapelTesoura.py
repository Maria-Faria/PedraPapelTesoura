import random

def pedra():
    print("    _______ ")
    print("---'   ____)")
    print("      (_____)")
    print("      (_____)")
    print("      (____)")
    print("---.__(___)")
    print("\n 1- PEDRA")

def papel():
    print("    _______")
    print("---'   ____)____")
    print("          ______) ")
    print("          _______) ")
    print("          _______)")
    print("---.__________)")
    print("\n 2- PAPEL")

def tesoura():
    print("    _______")
    print("---'   ____)____")
    print("          ______)")
    print("       __________)")
    print("      (____)")
    print("---.__(___)")
    print("\n 3- TESOURA")

def vencedor(usuario, pc):

    if (usuario == pc):
        if(usuario == 1):
            print("Escolha do usuário: ")
            pedra()

            print("\nEscolha do computador: ")
            pedra()
        
        elif(usuario == 2):
            print("\nEscolha do usuário: ")
            papel()

            print("\nEscolha do computador: ")
            papel()
        
        else:
            print("\nEscolha do usuário: ")
            tesoura()

            print("\nEscolha do computador: ")
            tesoura()

        print("----------------------------------")
        print("\t\tEmpate!")
        print("----------------------------------")

    elif(usuario == 1):
        if(pc == 2):
            print("\nEscolha do usuário: ")
            pedra()

            print("\nEscolha do computador: ")
            papel()
    
            print("----------------------------------")
            print("\tO computador venceu!")
            print("----------------------------------")
        
        else:
            print("\nEscolha do usuário: ")
            pedra()

            print("\nEscolha do computador: ")
            tesoura()
       
            print("----------------------------------")
            print("\tParabéns, você venceu!")
            print("----------------------------------")
    
    elif(usuario == 2):
        if(pc == 1):
            print("\nEscolha do usuário: ")
            papel()

            print("\nEscolha do computador: ")
            pedra()

            print("----------------------------------")
            print("\tParabéns, você venceu!")
            print("----------------------------------")
        
        else:
            print("\nEscolha do usuário: ")
            papel()

            print("\nEscolha do computador: ")
            tesoura()
            
            print("----------------------------------")
            print("\tO computador venceu!")
            print("----------------------------------")

    elif(usuario == 3):
        if(pc == 1):
            print("\nEscolha do usuário: ")
            tesoura()

            print("\nEscolha do computador: ")
            pedra()
            
            print("----------------------------------")
            print("\tO computador venceu!")
            print("----------------------------------")

        else:
            print("\nEscolha do usuário: ")
            tesoura()

            print("\nEscolha do computador: ")
            papel()

            print("----------------------------------")
            print("\tParabéns, você venceu!")
            print("----------------------------------")

#####################################################################

resp = "s"

while(resp == "s"):
    print("\n---------- Seja bem vindo ----------\n")

    print("    _______ \t      _______\t              _______")
    print("---'   ____)\t  ---'   ____)____\t  ---'   ____)____")
    print("      (_____)\t            ______)\t            ______)")
    print("      (_____)\t            _______)\t         __________)")
    print("      (____)\t            _______)\t        (____)") 
    print("---.__(___)\t   ---.__________)\t  ---.__(___)")
    print("\n 1- PEDRA\t   2- PAPEL\t          3- TESOURA")
    print("-------------------------------------------------------------------")
    print("Escolha uma opção (informe o número correspondente): ")

    usuario = int(input("\nInforme sua opção aqui: "))

    pc = random.randint(1, 3)

    vencedor(usuario, pc)

    resp = input("Deseja jogar novamente? (s/n): ")
