Problèmes Identifiés :

Le présent rapport vise à documenter les problèmes identifiés au cours du développement du projet ainsi que les impacts qui nous ont ralenti dans le développement du projet.<br>
Ces informations sont cruciales pour assurer la transparence de notre processus de développement et la résolution rapide des problèmes rencontrés.

1.	Architecture de la pyramide :

•	Problème : La structure pyramidale a créé des défis d'intégration et de communication entre les différents niveaux du projet.<br>
•	Impact : Retards dans le développement et la coordination entre les modules.<br>

2.	Inscription : Problèmes liés à l’ajout et au stockage des données des utilisateurs :

•	Problème : Difficultés lors de l'ajout et du stockage des données des utilisateurs dans le fichier JSON servant de « base de donnée ».<br>
•	Impact : Dysfonctionnement des fonctionnalités d'inscription et erreurs de stocker les informations des utilisateurs dans le fichier JSON.<br>

3.	Messagerie : Problèmes de stockage des messages et de duplication lors de l'actualisation :

•	Problème : Les messages des utilisateurs ne se sont pas stockés, et des duplications apparaissaient lors de l'actualisation de la fenêtre de messagerie.<br>
•	Impact : Fiabilité du système de messagerie compromise, avec des erreurs d'affichage et une expérience utilisateur dégradée.<br>

4.	Interdiction d'envoyer un même message en doublon :

•	Problème : La fonctionnalité d’envoi de chat ne permettait pas l’envoi d'un même message en doublon.<br>
•	Impact : On ne pouvait pas envoyer le même message 2 fois. Par exemple, on ne pouvait pas dire Bonjour à une personne 2 fois.<br>

5.	Inversion de l'ordre des messages stockés (du plus récent au plus ancien) :

•	Problème : L'ordre des messages stockés n'était pas correct, les messages plus récents n'apparaissaient pas en premier.<br>
•	Impact : Altération de l'expérience utilisateur, avec des attentes non satisfaites quant à l'ordre chronologique des messages. L’utilisateur devait défiler l’ensemble des messages stockés pour lire le dernier message.<br>

