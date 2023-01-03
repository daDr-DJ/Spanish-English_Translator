from bidict import bidict
import Langtect 
import fileinput,sys


# you can open the text document to see all the available words and add your own

File = "SpanishWords.txt"
def read_word(WD):
    Dictionary = {}
    with open(File) as file:
        for line in file:
            (key, value) = line.split()
            Dictionary[str(key)] = str(value)
    
    wd = bidict(Dictionary)
    
    try:
        language = Langtect.detect(WD)
            
        if language == 'en':
            wd = wd.inverse
            print(wd[WD],'\n\n')

        elif language == 'es':
            print(wd[WD],'\n\n')

        #print("The language you typed is",language,end='\n\n')
            
    except:
        language = Langtect.detect(WD)
                          
        if language == 'en' and WD != "":
            sw = Langtect.translate(WD,'es')
            ew = WD
            ew = ew.split()
            ew = '-'.join(ew)
            ew = ew.capitalize()
            print(sw,'\n\n')
            sw = sw.split()
            sw = '-'.join(sw)
            sw = sw.capitalize()

            with open(File) as Read, open(File, 'a') as Wrt:
                for line in Read:
                    span,eng = line.split()
                    if span == sw or eng == ew:
                        return

                    elif span == sw and eng == ew:
                        return

                save = ["",(f'{sw} {ew}')]
                Wrt.write('\n'.join(save))
                

        elif language == 'es' and WD != "":
            ew = Langtect.translate(WD,'en')
            sw = WD
            sw = sw.split()
            sw = '-'.join(sw)
            sw = sw.capitalize()
            print(ew,'\n\n')
            ew = ew.split()
            ew = '-'.join(ew)
            ew = ew.capitalize()

            with open(File) as Read, open(File, 'a') as Wrt:
                for line in Read:
                    span,eng = line.split()
                    if span == sw or eng == ew:
                        return

                    elif span == sw and eng == ew:
                        return

                   

                save = ["",(f'{sw} {ew}')]
                Wrt.write('\n'.join(save))

        else:    
            msg= "I do not RECOGNIZE this word"
            print(msg.center(80,'*'),'\n\n')
        
        

running = True
while running:    
    prompt = input("Enter your spanish or english word:")#human input
    print("",'\n')#space

    word = str(prompt)#input as readable str

    if word == 'N' or word == 'n':
        running = False

    elif word == 'ACT#1':
        ACT_a = input("Enter the word you want to store(Spanish English):") #1
        print('\n')#space
        neword = ["",str(ACT_a)]

        if neword[1].islower() or neword[1] == "":
            msg1 = "Try Again this time FIX FORMAT(Spanish English)"
            print( msg1.center(80,'*'),'\n\n')
            

        else:
            with open(File,'a') as doc:
                doc.write('\n'.join(neword))
                print("saved!!",'\n\n')
            
            

    elif word == 'ACT#2':
        ACT_b = input("Enter the word you want to remove:") #2
        print("",'\n')#space
        delword = str(ACT_b)
        
        notin = False
        
        with open(File) as file:
            for line in file:
                if delword != line:
                    notin = True                   

            msg5 = "WORD NOT FOUND"        
            print( msg5.center(80,'*'),'\n\n')

        if delword == "" and delword.islower():
            msg2 = "NO-BLANKS & USE CORRECT-FORMAT "
            print( msg2.center(80,'*'),'\n\n')   

        elif notin == False: 
            for line in fileinput.input(File, inplace=1):
               line = line.replace(delword, "")
               sys.stdout.write(line)

            with open(File) as reader, open(File, 'r+') as writer:
                for line in reader:
                    if line.strip():
                        writer.write(line)
                    writer.truncate()
                print("Word Removed!!",'\n\n')


    elif word == 'ACT#3':
        ACT_c = input("Enter the word you want to replace:") #3
        ACT_c1 = input("Enter the new Word:")
        print("",'\n')#space
        repdword = str(ACT_c)
        repword = str(ACT_c1)

        notin = False
        
        with open(File) as file:
            for line in file:
                if repdword != line:
                    notin = True             
                    
            msg5 = "WORD NOT FOUND"        
            print( msg5.center(80,'*'),'\n\n')
                    

        if repword == "" and repword.islower():
            msg3 = "NO-BLANKS & USE CORRECT-FORMAT"
            print( msg3.center(80,'*'),'\n\n')
            

        elif notin == False:
            for line in fileinput.input(File, inplace=1):
               line = line.replace(repdword, repword)
               sys.stdout.write(line)

            print("Word Replaced!!",'\n\n')
          
                
    else:
        read_word(word)# str put into def
