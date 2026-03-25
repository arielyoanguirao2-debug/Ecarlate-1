# Ecarlate-1
#  Web-Uptime-Monitor

Un script Python léger et efficace pour surveiller la disponibilité d'un site web en temps réel. Idéal pour débuter en automatisation et comprendre les interactions HTTP.

## Fonctionnalités
- **Analyse en temps réel** : Vérification automatique toutes les 5 secondes.
- **Gestion des statuts HTTP** : Détecte si le site est en ligne (200), introuvable (404) ou si l'accès est refusé (403).
- **Sécurité** : Intègre un *timeout* pour éviter que le script ne reste bloqué si le serveur ne répond pas.

## Installation

1. Clonez ce dépôt ou téléchargez le fichier `.py`.
2. Assurez-vous d'avoir Python installé.
3. Installez la bibliothèque nécessaire :
   ```bash
   pip install requests
   
