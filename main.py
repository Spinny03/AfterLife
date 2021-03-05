importa  speech_recognition  come  sr
importa  pyttsx3
import  pywhatkit
import  datetime
importa  wikipedia
importa  pyjokes

ascoltatore  =  sr . Riconoscitore ()
motore  =  pyttsx3 . init ()
voci  =  motore . getProperty ( 'voci' )
motore . setProperty ( 'voice' , voices [ 1 ]. id )


def  talk ( testo ):
    motore . dire ( testo )
    motore . runAndWait ()


def  take_command ():
    prova :
        con  sr . Microfono () come  sorgente :
            print ( 'ascolto ...' )
            voce  =  ascoltatore . ascolta ( fonte )
            comando  =  ascoltatore . riconoscere_google ( voce )
            comando  =  comando . inferiore ()
            se  'alexa'  al  comando :
                comando  =  comando . sostituire ( 'alexa' , '' )
                print ( comando )
    eccetto :
        passaggio
     comando di ritorno


def  run_alexa ():
    comando  =  take_command ()
    print ( comando )
    se  "riproduci"  al  comando :
        canzone  =  comando . sostituire ( 'play' , '' )
        parlare ( 'suonare'  +  canzone )
        pywhatkit . playonyt ( canzone )
    elif  'time'  al  comando :
        time  =  datetime . datetime . ora (). strftime ( '% I:% M% p' )
        talk ( "L'ora corrente è"  + l'  ora )
    elif  'chi diavolo è'  al  comando :
        persona  =  comando . sostituire ( 'chi diavolo è' , '' )
        info  =  wikipedia . riepilogo ( persona , 1 )
        stampa ( info )
        parlare ( info )
    elif  'date'  nel  comando :
        parlare ( "scusa, ho mal di testa" )
    elif  'sei single'  al  comando :
        talk ( 'Ho una relazione con il wifi' )
    elif  'scherzo'  al  comando :
        talk ( pyjokes . get_joke ())
    altro :
        talk ( "Pronuncia di nuovo il comando." )


mentre  True :
    run_alexa ()
