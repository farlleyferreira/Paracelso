import cv2
def ProccessVision():
        #Inicia modo de reconhecimento LBPHF
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('Vision/trainer/trainer.yml')

        #Inicia Classificador em cascata
        faceCascade = cv2.CascadeClassifier('Vision/haarcascades/haarcascade_frontalface_default.xml')

        #Instancia a fonte
        font = cv2.FONT_HERSHEY_SIMPLEX

        #Seta id como padrão 0
        id = 0

        #Popula vetor de usuarios
        ''' obs: melhorar isso, substituir por uma consulta a um banco de dados em 0
        utiliza-se None em função de o usuario 0 ser desconhecido '''
        names = ['None', 'farlley']

        #Inicialize e inicia a captura de vídeo em tempo real
        cam = cv2.VideoCapture(0)
        cam.set(3, 740) # set video widht
        cam.set(4, 740) # set video height

        # Define min tamanho minimo da janela para reconhecer uma face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        while True:
            #Realiza a captura do video
            ret, img = cam.read()

            #Ajusta a imagem da camera para a exibição correta
            img = cv2.flip(img, 1)

            #Converte a imagem em escala de cinza
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            #Realiza a detecção da face na imagem
            faces = faceCascade.detectMultiScale(
                                                    gray,
                                                    scaleFactor = 1.2,
                                                    minNeighbors = 5,
                                                    minSize = (int(minW), int(minH)),
                                                )

            for(x,y,w,h) in faces:
                #Desenha um retangulo na face identificada
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

                #Realiza predição do rosto
                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

                #Determina confiança do reconhecimento
                if (confidence <= 100):

                    #Determina a acuracia do reconhecimento
                    accuracy = 100 - confidence

                    #determina quem é o usuario
                    if(accuracy >= 35):
                        id = names[1]
                        confidence = "  {0}%".format(round(100 - confidence))
                    else:
                        id = "unknown"
                        confidence = "  {0}%".format(round(100 - confidence))

                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))

                #Adiciona textos a imagem identificada
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

            #Exibe a imagem
            cv2.imshow('frame', img)

            #Cria função de saida do sistema
            k = cv2.waitKey(10) & 0xff # saida em ESC
            if k == 27:
                break

        #Realiza limpeza da memoria
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()