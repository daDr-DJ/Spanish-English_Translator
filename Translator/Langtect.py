from googletrans import Translator

def detect(wd):
    LangID = '0'
    translator = Translator()

    eng_ends = ['ing','ly','tion','sion''ate',
                'l','ed','ee','mp','p']

    span_ends = ['ando','iendo','mente','cion',
                 'Ir','Y','Negro','Hola','Tan','Ya','z','Asi','Aun','ado','Alto']

    
    language = translator.detect(wd).lang

    if language == 'en':
        for Spendgs in span_ends:
            if wd.endswith(Spendgs):
                return 'es'  

            
        return 'en'


    else:
        for Endgs in eng_ends:
            if wd.endswith(Endgs):
                return 'en'
                

            
        return 'es'

def translate(wd,outputlang):
    translator = Translator()
    output = translator.translate(wd,outputlang)
    translation = output.text
    return translation
