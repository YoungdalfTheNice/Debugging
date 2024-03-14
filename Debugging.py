import logging
import re

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def check_email(input_email):
    '''
    Die Funktion checkt, ob der String input_email eine valide Adresse darstellt und liefert entweder den String oder eine Fehlermeldung zurück.
    
    Parameters: input_email (str) 
    Returns:    str
    
    '''
    logging.debug(f"Eingegebene Email ist {input_email}")
    logging.info(f"Funktion ’check_email’ wurde aufgerufen.")
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' ## Finde das mit Regex so etwas schöner, daher habe ich mir eine passende gesucht.
    assert re.match(pattern, input_email), f"Bitte gib eine korrekte Mail-Adresse an!"

def check_age(input_age):
    '''
    Die Funktion checkt, ob der String input_age ein valides Alter darstellt und liefert entweder die Zahl oder eine Fehlermeldung zurück.

    
    Parameters: input_age (str)
    Returns:    int

    '''
    logging.debug(f"Eingegebenes Alter ist {input_age}")
    logging.info(f"Funktion ’check_age’ wurde aufgerufen.")
    
    try:
        assert int(input_age) in range(10,100), f"Bitte gib ein korrektes Alter an!"
    except ValueError:
        print("ValueError: Du hast keine Zahl angegeben!")

def main():
    logging.info("Starte Programm.")
    aktiv = True
    while aktiv:
        prime=input(f"Drücke ’?’ um Hilfe zu bekommen.\n Drücke ’q’ um die App zu verlassen.\n Drücke ’w’ um weiterzumachen.")
        if prime == "q":
            aktiv = False
            logging.info("Beende Programm.")
        elif prime == "?":
            print(check_email.__doc__)
            print(check_age.__doc__)
        elif prime == "w":            
            input_email = ""
            input_age = ""

            while not input_email:
                input_email = input("Bitte gib deine Mail-Adresse an: ")
                logging.debug("Beginne Debugging.")
                try:
                    check_email(input_email)
                except AssertionError as e:
                    logging.warning(e)
                    input_email = ""

            while not input_age:
                input_age = input("Bitte gib dein Alter an: ")
                logging.debug("Beginne Debugging.")
                try:
                    check_age(input_age)
                except AssertionError as e:
                    logging.critical(e)
                    input_age = ""
        else:
            assert False, f"Du hast weder '?' noch 'q' noch 'w' eingegeben."
            logging.error('Bitte gib einen korrekten Input ein!')
            
main()