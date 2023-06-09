import sqlite3

# Nos conectamos a la base de datos (si no existe la crea)
conexion = sqlite3.connect("base_prueba.db")
# Creamos (si no existe) una tabla creada alumnos con sus campos
conexion.execute("""create table if not exists alumnos(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    edad integer
                    )""")
conexion.close()

conexion = sqlite3.connect("base_prueba.db")

# Insertamos dos alumnos
conexion.execute("Insert into alumnos(nombre,edad) values(?,?)", ("Ligia", 27))
conexion.execute("Insert into alumnos(nombre,edad) values(?,?)", ("Juan", 32))
conexion.execute("Insert into alumnos(nombre,edad) values(?,?)", ("adrian", 50))
# Este es necesario para que se ejecuten lñas consultas anteriores
conexion.commit()
# Recuperamos un elementos de la tabla alumnos y lo imprimimos
alumno = conexion.execute("select * from alumnos where nombre = 'Ligia'")
alumno2 = conexion.execute("select * from alumnos where nombre = 'Juan'")
alumno3 = conexion.execute("select * from alumnos where nombre = 'adrian'")
# Esto es para solamente traer el primero o bien para traer uno
fila = alumno.fetchone()
fila2 = alumno2.fetchone()
fila3 = alumno3.fetchone()
#imprimimos la fila (el alumno)
print(fila)
print(fila2)
print(fila3)

# Cerramos la conexión con SQLITE
conexion.close()