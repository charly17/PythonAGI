import pymysql

#Conectar base de datos
conexion = pymysql.connect(host="localhost",
                           user="admin",
                           password="charly1709",
                           database="asterisk")
cursor = conexion.cursor()

#Recuperar registros de la tabla 'usuarios'
registros = "SELECT user,pass FROM vicidial_users;"

#Mostrar registros
cursor.execute(registros)
filas = cursor.fetchall()
for fila in filas:
    print(fila)

#Finalizar
conexion.commit()
conexion.close()