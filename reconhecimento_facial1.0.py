import cv2
from deepface import DeepFace
import os
import pyttsx3

webcam = cv2.VideoCapture(0)
engine = pyttsx3.init()
models = [
  "VGG-Face", 
  "Facenet", 
  "Facenet512", 
  "OpenFace", 
  "DeepFace", 
  "DeepID", 
  "ArcFace", 
  "Dlib", 
  "SFace",
  "GhostFaceNet",
]


# Passo 1: abrir o webcam
if webcam.isOpened():
    validacao, frame = webcam.read()

    while validacao or frame is not None:
        validacao, frame = webcam.read()
        
        # Passo 2: Reconhecer o rosto
        resultado = DeepFace.find(img_path=frame, db_path='C:/Users/JOAO/Documents/Reconhecimento_Facial/fotos/Joao Vitor', model_name=models[2], enforce_detection=False)
        dataFrame = resultado[0]
        if not dataFrame.empty:
            identidade = dataFrame.loc[0, 'identity']
            nome = os.path.basename(os.path.dirname(identidade))

            if dataFrame.loc[0, 'distance'] < dataFrame.loc[0, 'threshold']:
                # Passo 3: Falar o nome
                engine.say(f"Seja Bem Vindo, {nome}")
                engine.runAndWait()

                break
            else:
                engine.say("Rosto não consta no Banco de Dados")
                engine.runAndWait()

                os.system("rundll32.exe user32.dll,LockWorkStation")
                
        else:
            engine.say("Rosto não consta no Banco de Dados")
            engine.runAndWait()

            os.system("rundll32.exe user32.dll,LockWorkStation")



webcam.release()
cv2.destroyAllWindows()