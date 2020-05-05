import speech_recognition

escutar = speech_recognition.Recognizer()

with speech_recognition.Microphone() as caminho:
    audio = escutar.listen(caminho)

    with open('gravacao.wav', 'wb') as grava:
        grava.write(audio.get_wav_data())

