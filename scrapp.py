from cgi import print_arguments
import string
from bs4 import BeautifulSoup
import requests

#####################################################################################
############################ FUNCION DE EXTRAER #####################################
#####################################################################################
def extract(url, cont):
    cap=[]
    html = BeautifulSoup(requests.get(url+cont).text, 'html.parser')

    divs = html.find_all('span', class_='align-left')
    #print(divs)
    for container in divs:
        topic = container.find('span')
        if not topic :
            print(container)
        #print(topic.text)
        versi=str(len(cap)+1)+" "
        cap.append(topic)
    
    return cap

#####################################################################################
######################## ZONA DE INGRESAR DATOS #####################################
#####################################################################################
libro="Mateo"
url_ay="https://live.bible.is/bible/aymbsb/mat/"
url_en="https://live.bible.is/bible/engesv/mat/"
cantidad_capitulos=28

#####################################################################################
######################## ZONA DE EJECUCION DE FUNCION ###############################
#####################################################################################

capitulo_ay=[]
capitulo_en=[]
capitulo_en_ay=[]
for i in range(cantidad_capitulos):
    print("################################################################################################### = ",i+1)
    cont=str(i+1)
    capitulo_ay=capitulo_ay+(extract(url_ay,cont))
    capitulo_en=capitulo_en+(extract(url_en,cont))

print(len(capitulo_ay), len(capitulo_en))

capitulo_en_ay.append(capitulo_en)
capitulo_en_ay.append(capitulo_ay)
#print(capitulo_en_ay)

import csv
from itertools import zip_longest
transposed_signals = list(zip_longest(*capitulo_en_ay, fillvalue=''))
with open(libro+'.csv', 'w', encoding="utf-8", newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(('sound_' + str(i + 1) for i in range(2)))
    wr.writerows(transposed_signals)