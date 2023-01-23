import pyttsx3
import os


def convert_tts(sentence:str, number:int) -> str:
    '''Converts a sentence into an audio file. \n
        Returns the path of the audio file'''
    
    # Initialize TTS engine
    engine = pyttsx3.init()
    
    # Make split_audio directory if it doesn't exist
    try:
        os.mkdir("split_audio")
    except:
        pass
    
    # Create command to save audio to file
    output_path = f"split_audio/output{number}.mp3"
    engine.save_to_file(sentence, output_path)

    # Run the engine
    engine.runAndWait()
    
    return output_path