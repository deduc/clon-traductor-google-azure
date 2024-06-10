from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, SpeechSynthesizer, AudioConfig
import azure.cognitiveservices.speech as speech_sdk


class Voz:
    api_key = "785a935cb404462aa5cf94d0b04b1808"
    region = "northeurope"
    speech_config = None

    def __init__(self):
        self.speech_config = None
        self.speech_config = SpeechConfig(subscription=self.api_key, region=self.region)

    def texto_a_audio(self, idioma_input="", texto_input=""):
        try:
            response_text = texto_input
            # self.speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
            self.speech_config.speech_synthesis_voice_name = "es-ES-AlvaroNeural"
            speech_synthesizer = SpeechSynthesizer(speech_config=self.speech_config)

            # Synthesize spoken output
            speak = speech_synthesizer.speak_text_async(response_text).get()
            if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
                print(speak.reason)

            # Print the response
            print(response_text)

        except Exception as ex:
            print(ex)

    def audio_a_texto(self, idioma_input="", idioma_output=""):
        command = ''

        # Configure speech recognition
        audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
        speech_recognizer = speech_sdk.SpeechRecognizer(self.speech_config, audio_config)
        print("Grabando audio...")

        # Process speech input
        speech = speech_recognizer.recognize_once_async().get()
        if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
            command = speech.text
            print(command)
        else:
            print(speech.reason)
            if speech.reason == speech_sdk.ResultReason.Canceled:
                cancellation = speech.cancellation_details
                print(cancellation.reason)
                print(cancellation.error_details)

        # Return the command
        return command
