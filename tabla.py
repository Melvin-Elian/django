import sqlite3
conexion =sqlite3.connect("Destinos.bd")
consulta= conexion.cursor()
sql="""
CREATE TABLE IF NOT EXISTS Destinos(
    id INTEGER PRYMARI KEY AUTOINCREMENT NOT NULL,
    NombreCiudad VARCHAR(40) NOT NULL,
    DescripcionCiudad VARCHAR(50) NOT NULL,
    PrecioTour FLOAT NOT NULL,
    OfertaTour BOOLEAN NOT NULL,
    ImagenCiudad VARCHAR(70) NOT NULL
    """
    if(consulta.execute(sql)):print("TABLA CREADA")
    else: print("ERROR EN TABLA")
    consuta.close()
    conexion.commit()
    conexion.close()