import requests
import time
def test_unique():
     url=input("entrez l'URL a tester : ")
     requete = requests.get(url,timeout=10)
     
     if requete.status_code==200:
         print("le site est en ligne")
         
     elif requete.status_code!=200:
        
        if requete.status_code==404:
           
           print("le site est hors ligne")
           print()
           print("le site est introuvable ")
           
        elif requete.status_code==403:
           print("le serveur est en ligne")
           print()
           print("mais refuse de repondre")

def test_multiple():
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



print("1-verification unique")
print("2-verification continue")
print("")
choix=int(input("entrez votre choix : "))
if choix==1:
    try :
       test_unique()      
    except ValueError:
       print("entrez un adresse valide")
       print("relancer le programme et recommencer ")
    except requests.exceptions.RequestException:
       print("vous êtes hors ligne")
       print("connecter vous et ressayer")

elif choix==2:
 try :
    test_multiple()           
 except ValueError:
   print("entrez un adresse valide")
   print("relancer le programme et recommencer ")
 except requests.exceptions.RequestException:
   print("vous êtes hors ligne")
   print("connecter vous et ressayer")
       
else:
    print("relancer le programme et suivez les indications ")


   
    
   
   
   
    
