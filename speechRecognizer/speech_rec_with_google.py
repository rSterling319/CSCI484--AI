#!/usr/bin/env python3

#speech recognition out sourced to google
#not much ai programming involved.

import speech_recognition as sr



def get_text_fromSpeech(recognizer, microphone):

    #check recognizer/mic are correct type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError('recognizer must be Recognizer')
    if not isinstance(microphone, sr.Microphone):
        raise TypeError('microphone must be Microphone')

    #adjust recognizer sensitivity and adjust for ambient noise
    #record audio
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    #set up the response
    response = {
        "success": True,
        "error":None,
        "transcription":None
    }

    #try recognizing the speech
    #if any errors respond accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        #API was unreachable or unresponsive
        response["success"]=False
        response["error"]="API  unavailable"
    except sr.UnknownValueError:
        #speech was unintelligable
        response["error"]="Unable to recognize speech"

    return response




if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Speak into microphone")
    text = get_text_fromSpeech(recognizer, microphone)

    if text["error"]:
        print("Error {}".format(text["error"]))
    if text["transcription"]:
        print("Transcription: {}".format(text["transcription"]))

    print(text)


