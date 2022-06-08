import socket as s
website = input("ingresa la url del sitio web: ")
print("la ip del sitio web es : ", s.gethostbyname(website))
