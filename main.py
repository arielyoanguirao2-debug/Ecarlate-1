import requests
import time
print("bonjour")

def test():
   url=input("entrez l'URL a tester : ")
   while True:
    requete = requests.get(url, timeout=10)
    if requete.status_code==200:
       print("le site est en ligne ")
       print()
    elif requete.status_code!=200:
       if requete.status_code==404:
           print("le site est hors ligne")
           print()
           print("le site est introuvable ")
       elif requete.status_code==403:
           print("le serveur est en ligne")
           print()
           print("mais refuse de repondre")
    time.sleep(5)
    
try :
    test()           
except ValueError:
   print("entrez un adresse valide")
   print("relancer le programme et recommencer ")
   
   
   
    
