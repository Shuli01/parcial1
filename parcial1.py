#Crear una aplicación de línea de comandos que permita registro, búsqueda, edición y eliminación de artículos dentro de un sistema de inventario.

import sqlite3

conn = sqlite3.connect('inv.db')

while True:
   print("\n====INVENTARIO=====")
   print("1. Eliminar")
   print("2. Crear")
   print("3. Buscar")
   print("4. Edicion")
   print("5. Salir")
   print("0. Crear Base de Datos")
   
   try:
      opcion = int(input("\nOpcion: "))
   except:
      opcion = 1000

   if opcion == 1:
      print("\nEliminar")
      while True:
         print("\n1. Eliminar articulo")
         print("\n2. Regresar al menu principal")
         try:
            opcion = int(input("\nOpcion: "))
         except:
            opcion = 0
         
         if opcion == 1:
            cursor = conn.execute("SELECT ID, NOMBRE FROM ARTICULO")
            for row in cursor:
               print(str(row[0])+". "+str(row[1]))
            try:
               por_eliminar = int(input("Inserte ID del ARTICULO a borrar... "))
            except:
               por_eliminar = 999999
            conn.execute("DELETE FROM ARTICULO WHERE ID = " + str(por_eliminar ))
            conn.commit()
         elif opcion == 2:
            print("Regresando al menú principal🤷")
            break
         else:
            print("ERR::Opcion no valida")
   elif opcion == 2:
      print("\nCrear")
      while True:
         print("\n1. Crear artculo")
         print("2. Regresar al menu principal")
         try:
            opcion = int(input("\nOpcion: "))
         except:
            opcion = 0
         if opcion == 1:
            id = input("ID?")
            nombre = input("Nombre?")
            tipo = input("Tipo?")
            cantidad = input("Cuantos?")
            conn.execute("INSERT INTO ARTICULO(ID, NOMBRE, TIPO, CANTIDAD) VALUES("+id+", \""+nombre+"\", \""+tipo+"\", \""+cantidad+"\")")
            conn.commit()
         elif opcion == 2:
            print("Regresando al menú principal🤷")
            break
         else:
            print("ERR::Opcion no valida")
   elif opcion == 3:
      print("\nBuscar")
      while True:
         print("\n1. Buscar articulo")
         print("2. Regresar al menu principal")
         try:
            opcion = int(input("\nOpcion: "))
         except:
            opcion = 0
         if opcion == 1:
            cursor = conn.execute("SELECT NOMBRE FROM ARTICULO")
            #for row in cursor:
            #   print(str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3]))
            for row in cursor:
                print(str(row[0]))
         elif opcion == 2:
            print("Regresando al menú principal🤷")
            break
         else:
            print("ERR::Opcion no valida")
   elif opcion == 4:
      print("\nActualizar")
      while True:
         print("\n1. Actualizar articulo")
         print("2. Regresar al menu principal")
         try:
            opcion = int(input("\nOpcion: "))
         except:
            opcion = 0
         if opcion == 1:
            cursor = conn.execute("SELECT ID, NOMBRE FROM ARTICULO")
            for row in cursor:
               print(str(row[0])+". "+str(row[1]))
            por_actualizar = input("Inserte ID del ARTICULO por actualizar... ")
            nuevo_nombre = input("Inserte el nuevo nombre del ARTICULO... ")
            conn.execute('UPDATE ARTICULO SET NOMBRE = "' + nuevo_nombre + '" WHERE ID = ' + por_actualizar)
            conn.commit()
         elif opcion == 2:
            print("Regresando al menú principal🤷")
            break
         else:
            print("ERR::Opcion no valida")
   elif opcion == 5:
      break
   elif opcion == 0:
      print("\nCrear estructura de base de datos")
      conn.execute('''CREATE TABLE IF NOT EXISTS PROVEEDORES
                   (ID INT PRIMARY KEY NOT NULL,
                    NOMBRE TEXT NOT NULL,
                    UBICACION CHAR(50),
                    CLASIFICACION TEXT);''')
      conn.execute('''CREATE TABLE IF NOT EXISTS PRODUCTO
                   (ID INT PRIMARY KEY NOT NULL,
                    NOMBRE TEXT NOT NULL,
                    TIPO TEXT,
                    CANTIDAD INT);''')
      conn.execute('''CREATE TABLE IF NOT EXISTS DISTRIBUIDORES
                   (ID INT PRIMARY KEY NOT NULL,
                    NOMBRE TEXT NOT NULL,
                    UBICACION TEXT,
                    CLASIFICACION TEXT);''')

   else:
      print("ERR::Opcion no valida")
