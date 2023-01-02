from googletrans import Translator

def detect(wd):
    LangID = '0'
    translator = Translator()

    eng_ends = ['ing','ly','tion','sion''ate',
                'l','ed','ee']

    span_ends = ['ando','iendo','mente','cion',
                 'Ir','Y','Negro','Hola','Tan','Ya','z','Asi','Aun']

    
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
