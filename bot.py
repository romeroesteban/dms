#    __ __ __ __           _ _ _             __ __ __          _ _ _     
#  /_ _      __ /|     ."         " .       /  _--_  \    . "         " . 
# |_ _/    / |__|/   /      _ _      \     /      ___/   /      _ _      \ 
#    /    / /       |    (  _ _  )    |   /   /\  \ _|  |    (  _ _  )    |        
#   /_ _ / /         \               /   /__ |  \__\     \               / 
#   |_ _ |/             "  _ _ _  "      |__|/  |__|        "  _ _ _  "     


from instabot import Bot
import time
import multiprocessing

dm_bot = Bot()    #Instanciación de un objeto de la clase Bot


#login
dm_bot.login(username="naniacup", password="@Genesis322", use_cookie=False)

contacto = "-"

while contacto != "":
  try: 
    contacto = input(str("Ingresa el contacto a quien quieres enviar un mensaje: "))
  except Exception:
    print("¡Nombre de usuario inválido tontuelo!")

  mensaje = "¡Hola " + contacto + "!" + " te invito este fin, Sábado 26 de Noviembre, traemos el concierto de @MEZERG en vivo.\n\nPor primera vez en Guadalajara.\n\nEs una collab de @off_studios x @baramericas, va a estar fino. Ojalá puedas caerle.\n\nNos ayudarías a subir a tus historias este flyer con el link como “Enlace” y etiquetando @off_studios y @mezerg ?\n\nhttps://ticketin.com.mx/buy/101\n\nConfírmame si te late, para ponerte en la lista y eso!"
  dm_bot.send_message(mensaje, contacto)

  
