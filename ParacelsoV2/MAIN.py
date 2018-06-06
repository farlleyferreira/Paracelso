
from Speech.paracelso_spech import paracelso_recognition
from Brain.bot.bot_engine import bot_brain_engine
from Vision.init_process import ProccessVision
from threading import Thread

psr = paracelso_recognition()
bet = bot_brain_engine()

def ProccessVoice():
    while defaut:
        text = psr.speech_totext()
        print(text)
        if(text is not None):
            value = bet.Conversation(text)
            psr.text_to_speech(value)

def ProcessVisionStart():
    ProccessVision()


defaut = True
paracelso_recognition().text_to_speech('Iniciando sistema Paracelso')
paracelso_recognition().text_to_speech('preparando algoritmos de dominação global')
paracelso_recognition().text_to_speech('carregando módulos')

Thread(target = ProcessVisionStart).start()

paracelso_recognition().text_to_speech('iniciando contagem regressiva')
paracelso_recognition().text_to_speech('corram para as colinas')
for i in range(5):
    paracelso_recognition().text_to_speech(5 - i)
paracelso_recognition().text_to_speech('sistema Paracelso iniciado com sucesso!')
paracelso_recognition().text_to_speech('bem vindo ao sistema de controle de terminais baseado em inteligencia artificial')
paracelso_recognition().text_to_speech('por onde podemos começar?')

Thread(target = ProccessVoice).start()



#defaut = False