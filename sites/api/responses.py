import requests
from datetime import datetime
import re

def get_content(url,regex=''):
    """
    Effettua una richiesta HTTP GET ad una URL data in input. 
    Restituisce: 
    - la data e l'orario della richiesta
    - lo status code del response
    - il tempo di risposta
    - l'eventuale match con l'espressione data in input.
    """

    # Effettua la richiesta GET all'url dato in input, ottiene lo status code e il tempo di risposta e salva il risultato del response
    response = requests.get(url)
    data = response.text
    status = response.status_code
    time = response.elapsed.total_seconds() 

    # Se è presente l'espressione regolare effettua il controllo del match
    if (regex != ''):
        pattern = re.compile(regex)  
        match = re.findall(pattern, data) 
        if (match !=[]):
            is_match = True
        else:
            is_match = False

        result = dict(get_time = datetime.now(), url = url, regex=regex, status_code = status, time_elapsed = time, is_match_regex = is_match)
    else:
        result = dict(get_time = datetime.now(), url = url, status_code = status, time_elapsed = time)
    
    return result