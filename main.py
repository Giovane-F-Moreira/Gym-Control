import face_recognition
import json
from Pessoa import Pessoa
from Academia import Academia
import random

# ARQUIVO_AUTORIZACOES = "/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/autorizacoes.json"

def iniciar():
    pass


"""========================== Function ==========================
It loads the image file, finds the face in the image, and then encodes the face into a 128-d vector

    ------------------------ Parameters ------------------------
:param foto_original: The path to the image file containing the face of the person we want to
recognize
==================================================================
"""
def configurar_reconhecedor(foto_original):
    global encoding_foto_original 
    
    # Vai processar os bits e encodar em um formato especifico
    foto = face_recognition.load_image_file(foto_original)
    encoding_foto_original = face_recognition.face_encodings(foto)[0]     



"""========================== Function ==========================
It loads the image file, finds the face in the image, and then compares the face to the known face

------------------------ Parameters ------------------------
:param foto: The path to the image you want to compare

........................ Returns ...........................
:return: A list of True or False
==================================================================
"""
def comparar_com_original(foto, nome):

    global encoding_foto_original
    
    resultado = None
    
    try:
        nova_foto = face_recognition.load_image_file(foto)
        encoding_nova_foto = face_recognition.face_encodings(nova_foto)[0]
        
        resultado = face_recognition.compare_faces([encoding_foto_original], encoding_nova_foto)
    except:
        pass
    
    return resultado
 
def mensalidade_paga(pessoa):
    pass

def dias_treino(pessoa):
    pass 
       
# A way to make sure that the code in the if statement only runs if the module is executed as the main
# program.
if __name__ == '__main__':
    iniciar()
    
    foto_original = "/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Arnaldo_1.png"
    configurar_reconhecedor(foto_original)
    
    fotos = ["/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Arnaldo_1.png",
             "/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Arnaldo_2.png", 
             "/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Arnaldo_3.png",
             
             "/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Ronnie_1.png",
             "/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Ronnie_2.png",
             "/media/gio-ubuntu-20/Arquivos-M2/Linux/Workspace/Gym-Control/faces/photos/Ronnie_3.png"
             ]
    
    # contador = 1
    # while contador <= 10:
    #     print("-------------------",dias_treino)
    #     dias_treino += 1
        
    #     for foto in fotos:
    #         resultado = comparar_com_original(foto)
            
    #         if resultado:
    #            dias_treino
    #            print("")
    #            dias_treino_ronnie = dias_treino_ronnie + 1
            
    #         print("Resultado da comparação", resultado)
    
    
    print("Teste com orientação a objetos")
    
    arlindo = Pessoa('Arlindo', 'photo', bool(random.getrandbits(1)), 0)
    ronnie = Pessoa('Ronnie', 'photo', bool(random.getrandbits(1)), 0)
    graccyane = Pessoa('Graccyane', 'photo', bool(random.getrandbits(1)), 0)

    pessoas = [arlindo,ronnie,graccyane]

    academia = Academia(pessoas)

    i = 0
    while i <= 60:
        print('=========================================',i,'º Dia: =========================================')  
        if i == 30:
            pessoas[0].inadiplente = bool(random.getrandbits(1))
            pessoas[1].inadiplente = bool(random.getrandbits(1))
            pessoas[2].inadiplente = bool(random.getrandbits(1))
            academia.treinar(pessoas)
            
        elif i == 60:
            academia.exibir_informacoes()
        
        else:
            academia.treinar(pessoas)
    
        
        i=i+1
        
