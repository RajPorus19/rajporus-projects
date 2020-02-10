*****Instruction pour cette alamre*****

Pour définir la sonnerie que vous souhaitez uttiliser :
-Veuillez le télécharger en format mp3 et le glisse dans le dossier "PROJET"
-Ensuite ouvrez le fichier "settings.txt", vous verrez un texte de la sorte:
defaultTime=5
defaultAlarm=alarmSound.mp3
offday=5,6
playerName=vlc.exe
-Il vous faut changer la valeur de "defaultAlarm", après le signe "=", entrez le nom de votre fichier audio suivi de l'extension ".mp3"
-Comme par exemple:
defaultTime=5
defaultAlarm=danseLesSardines.mp3 <== ici on vient de changer la sonnerie
offday=5,6
playerName=vlc.exe
------------------------------------------------------------------------------------------------------------------------------------

Pour définir la durée de la sonnerie:
-Veuillez ouvrir le fichier "settings.txt", vous verrez un texte de la sorte:
defaultTime=5
defaultAlarm=alarmSound.mp3
offday=5,6
playerName=vlc.exe
-Il vous faut changer la valeur de "defaultTime", après le signe "=", entrez la durée en secondes
-Comme par exemple:
defaultTime=30 <== ici on a changé la durée de la sonnerie
defaultAlarm=alarmSound.mp3
offday=5,6
playerName=vlc.exe

------------------------------------------------------------------------------------------------------------------------------------

Pour définir les jours fermés:
-Veuillez ouvrir le fichier "settings.txt", vous verrez un texte de la sorte:
defaultTime=5
defaultAlarm=alarmSound.mp3
offday=5,6
playerName=vlc.exe
-Il vous faut changer la valeur de "offday", après le signe "=", les chiffres correspondant au jours souhaité:
0:Lundi
1:Mardi
2:Mercredi
3:Jeudi
4:Vendredi
5:Samedi
6:Dimanche
-Comme par exemple:
defaultTime=5 
defaultAlarm=alarmSound.mp3
offday=2,5,6<== ici on a ajouté mercredi
playerName=vlc.exe

------------------------------------------------------------------------------------------------------------------------------------

Veuillez définir le player qui ouvre votre fichier mp3 sur settings:
defaultTime=5
defaultAlarm=alarmSound.mp3
offday=5,6
playerName=vlc.exe <== Si vous n'utilisez pas vlc renseingner votre player.

