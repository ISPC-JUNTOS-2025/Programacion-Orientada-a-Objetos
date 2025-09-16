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

-- Tabla Usuarios_Domicilios
CREATE TABLE Usuarios_Domicilios (
    id_domicilio INT,
    email_usuario VARCHAR(100),
    FOREIGN KEY (id_domicilio) REFERENCES Domicilios(id_domicilio) ON DELETE CASCADE,
    FOREIGN KEY (email_usuario) REFERENCES Usuarios(email) ON DELETE CASCADE
);
GO

-- Tabla ubicaciones_casa
CREATE TABLE Ubicaciones_casa (
    id_ubicacion_casa INT IDENTITY(1,1) PRIMARY KEY,
    id_domicilio INT NOT NULL,
    nombre_ubicacion VARCHAR(50),
    FOREIGN KEY (id_domicilio) REFERENCES Domicilios(id_domicilio)

    );
GO

-- Tabla automatizaciones
CREATE TABLE Automatizaciones (
    id_automatizacion INT IDENTITY(1,1) PRIMARY KEY,
    id_ubicacion_casa INT,
    descripcion_automatizacion VARCHAR(120),
    regla_automatizacion VARCHAR(50),
    condicion_automatizacion VARCHAR(50),
    accion VARCHAR(50),
    estado BIT DEFAULT 1,
    nombre_automatizacion VARCHAR(50),
    FOREIGN KEY (id_ubicacion_casa) REFERENCES Ubicaciones_casa(id_ubicacion_casa )
    );
GO

-- Tabla dispositivos
CREATE TABLE Dispositivos(
    id_dispositivo INT IDENTITY(1,1) PRIMARY KEY,
    id_ubicacion_casa INT,
    nombre_dispositivo VARCHAR(50),
    estado BIT,
    descripcion VARCHAR(100),
    tipo_dispositivo VARCHAR(50),
    fecha_creacion DATETIME,
    FOREIGN KEY (id_ubicacion_casa) REFERENCES Ubicaciones_casa(id_ubicacion_casa)
    );
GO

-- Tabla automatizaciones_dispositivos
CREATE TABLE Automatizaciones_dispositivos(
    id_automatizacion INT,
    id_dispositivo INT,
    PRIMARY KEY (id_automatizacion, id_dispositivo),
    FOREIGN KEY (id_automatizacion) REFERENCES Automatizaciones(id_automatizacion),
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivos(id_dispositivo)
    );
GO