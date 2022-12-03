import face_recognition
from Pessoa import Pessoa
from Academia import Academia
import random

# ARQUIVO_AUTORIZACOES = "/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/autorizacoes.json"

cache_de_imagens = {}

def cadastro():
    arlindo =   Pessoa('Arlindo',   
                       'Youtuber conhecido por utilizar esteroides anabolizantes',
                       False,
                       '/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Arnaldo_1.png',  
                       True, 
                       0)
    
    ronnie =    Pessoa('Ronnie',    
                       'Foi campeão no Mr. Olympia',
                       True,
                       '/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Ronnie_1.png',
                       True, 
                       0)
    
    graccyane = Pessoa('Graccyane', 
                       'É modelo, fisiculturista e já foi dançarina',
                       True,
                       '/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Gracyanne_1.png',
                       True, 
                       0)
    
    return [arlindo,ronnie,graccyane]

def configurar():
    autorizados, suspeitos = [], [] 

    pessoas = cadastro()
    
    autorizados = [pessoas[1],pessoas[2]]
    suspeitos = [pessoas[0]]    
           
    for contador, autorizado in enumerate(autorizados):
        print(f"Codificando características faciais de {contador} autorizados")

        foto = face_recognition.load_image_file(autorizado.foto)
        autorizado.caracteristicas_faciais = face_recognition.face_encodings(foto)[0]

    for contador, suspeito in enumerate(suspeitos):
        print(f"Codificando características faciais de {contador} suspeitos")

        foto = face_recognition.load_image_file(suspeito.foto)
        suspeito.caracteristicas_faciais = face_recognition.face_encodings(foto)[0]

    return autorizados, suspeitos


def processar_caracteristicas_de_visitantes(foto_visitantes):
    caracteristicas = None

    if foto_visitantes in cache_de_imagens:
        caracteristicas = cache_de_imagens[foto_visitantes]
    else:
        foto = face_recognition.load_image_file(foto_visitantes)
        caracteristicas = face_recognition.face_encodings(foto)

        cache_de_imagens[foto_visitantes] = caracteristicas

    return caracteristicas

def autorizar(autorizados, visitantes):
    acessos_permitidos = []
    global pessoas
    pessoas = []
    global academia 

    caracteristicas_dos_visitantes = processar_caracteristicas_de_visitantes(visitantes)

    # 1. percorrer toda a lista de pessoas autorizadas
    for autorizado in autorizados:
        # 2. testar se a foto da pessoa autorizada está entre os visitantes
        acesso_permitido = True in face_recognition.compare_faces(
            caracteristicas_dos_visitantes, autorizado.caracteristicas_faciais)
        # 3. se a foto for reconhecida, permitir o acesso e retornar as informacoes de nome e biografia
        if acesso_permitido:
            acessos_permitidos.append(autorizado)
        
        pessoas.append(autorizado)     
      
    return len(acessos_permitidos) > 0, acessos_permitidos

def detectar_suspeitos(suspeitos, visitantes):
    suspeitos_detectados = []

    caracteristicas_dos_visitantes = processar_caracteristicas_de_visitantes(visitantes)

    # 1. percorrer toda a lista de pessoas autorizadas
    for suspeito in suspeitos:
        # 2. testar se a foto da pessoa suspeita está entre os visitantes
        suspeito_detectado = True in face_recognition.compare_faces(
            caracteristicas_dos_visitantes, suspeito.caracteristicas_faciais)
        # 3. se a foto for reconhecida, avisar que suspeito foi reconhecido
        if suspeito_detectado:
            suspeitos_detectados.append(suspeito)

    return len(suspeitos_detectados) > 0, suspeitos_detectados


if __name__ == '__main__':
    autorizados, suspeitos = configurar()

    capturas = ["/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/grupos/autorizados.png",
                "/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/grupos/suspeitos.png",

                "/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Arnaldo_1.png",
                "/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Arnaldo_2.png",
                "/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Arnaldo_3.png",
                ]
    
    print('**********************************  Reconhecimento Facial  **********************************')
    for captura in capturas:
        print(f"processando captura: {captura}")

        existem_permissoes, acessos_permitidos = autorizar(
            autorizados, captura)
        if existem_permissoes:
            for permissao in acessos_permitidos:                
                print(f"{permissao.nome}, teve a face reconhecida")
        else:
            print(f"nenhuma pessoa permitida")

        existem_suspeitos, suspeitos_detectados = detectar_suspeitos(
            suspeitos, captura)
        if existem_suspeitos:
            for suspeito in suspeitos_detectados:
                print(f"detectado um suspeito: {suspeito.nome}")
        else:
            print(f"nenhum suspeito detectado")

     
    arlindo =   Pessoa('Arlindo',   
                       'Youtuber conhecido por utilizar esteroides anabolizantes. ',
                       False,
                       '/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Arnaldo_1.png',  
                       True, 
                       0)
    
    ronnie =    Pessoa('Ronnie',    
                       'Um fisiculturista norte-americano, detentor do recorde de oito títulos consecutivos de Mr. Olympia. ',
                       True,
                       '/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Ronnie_1.png',
                       True, 
                       0)
    
    graccyane = Pessoa('Graccyane', 
                       'É uma modelo de fisiculturismo, rainha de bateria e ex-dançarina brasileira. ',
                       True,
                       '/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Gracyanne_1.png',
                       True, 
                       0)

    academia = Academia(pessoas)   
    academia.realizar_pagamento(pessoas)
    
    i = 0
    while i < 30:
        print('=========================================',i+1,'º Dia: =========================================')  

        cont = 0
        while cont < len(pessoas):
            if pessoas[cont].inadiplente:
                print(pessoas[cont].nome,'está inadiplente')
                pessoas[cont].inadiplente = bool(random.getrandbits(1))
                if pessoas[cont].inadiplente:
                    print(pessoas[cont].nome, 'efetuou o pagamento da mensalidade, Catraca LIBERADA!')

            else:
                print('A mensalidade de',pessoas[cont].nome,'está paga')
                academia.treinar(pessoas[cont])
            
            cont = cont + 1
            
        if i == 29:
            academia.exibir_informacoes()
           
        i=i+1