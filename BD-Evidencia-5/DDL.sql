USE SmartHomeDB;
GO

-- Tabla Usuarios
CREATE TABLE Usuarios(
    email VARCHAR(100) PRIMARY KEY,
    apellido VARCHAR(50) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    contrasena VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    rol VARCHAR(20) CHECK (rol IN ('Admin','Usuario')), -- simulando ENUM
    fecha_nacimiento DATE,
    fecha_creacion DATETIME DEFAULT GETDATE()
);
GO

-- Tabla Domicilios
CREATE TABLE Domicilios (
    id_domicilio INT IDENTITY(1,1) PRIMARY KEY,
    calle VARCHAR(100) NOT NULL,
    numero VARCHAR(10),
    barrio VARCHAR(50),
    ciudad VARCHAR(50),
    pais VARCHAR(30),
	codigo_postal VARCHAR(20)
);
GO