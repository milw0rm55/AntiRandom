import os
import time
from tkinter.messagebox import showerror


# El resultado de la función mencionada arriba es un array de valores, podemos almacenarlo en un array o en múltiples variables

# Array


file_status_array = os.stat("C:/Users/Administrador/Documents/000AAAaaa")

# vars
(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat("C:/Users/Administrador/Documents/000AAAaaa/")

# Los tiempos de acceso, modificación y creación necesitan ser formateados para ser comprensibles
# Para formatear estos tiempos usaremos time.ctime()
caca = True
while caca==True:
    if time.ctime(mtime)!= ("Mon Nov 19 09:21:31 2018"):
        print(time.ctime(ctime))
        def pregunta():showerror("Se ha modificado la carpeta", "Llamadme")
        os.system('shutdown -s')


print(time.ctime(ctime))  # Output: 'Tue Dec 30 08:35:53 2014'

print(time.ctime(atime))  # Output: 'Tue Jan 13 09:15:29 2015'

print(time.ctime(mtime))  # Output: 'Mon Jan 12 08:57:29 2015'