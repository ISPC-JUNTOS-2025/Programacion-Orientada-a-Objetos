USE SmartHomeDB;
GO



-- ---- Tabla Domicilios ----
INSERT INTO Domicilios (calle, numero, barrio, ciudad, pais, codigo_postal)
VALUES
('Calle Falsa','123','Centro','Buenos Aires','Argentina', '5000'),
('Av. Libertador','456','Palermo','Buenos Aires','Argentina','5001'),
('Calle Siempre Viva','742','Belgrano','Buenos Aires','Argentina','5002'),
('Calle Independencia','321','Recoleta','Buenos Aires','Argentina', '5006'),
('Av. Corrientes','987','San Telmo','Buenos Aires','Argentina', '5015'),
('Calle Fenix','111','Villa Crespo','Buenos Aires','Argentina', '6580'),
('Av. San Martin','222','Caballito','Buenos Aires','Argentina', '5611'),
('Calle Luna','333','Palermo','Buenos Aires','Argentina', '5630'),
('Av. Rivadavia','444','Recoleta','Buenos Aires','Argentina', '5153'),
('Calle Sol','555','Belgrano','Buenos Aires','Argentina', '5650'),
('Calle Robles','10','Palermo','Buenos Aires','Argentina', '5690'),
('Av. Las Heras','20','Recoleta','Buenos Aires','Argentina', '6500'),
('Calle Pampa','30','Belgrano','Buenos Aires','Argentina', '1300'),
('Calle Serrano','40','Palermo','Buenos Aires','Argentina', '6511'),
('Av. Santa Fe','50','Recoleta','Buenos Aires','Argentina', '5610'),
('Calle Honduras','60','Palermo','Buenos Aires','Argentina', '5560'),
('Calle Fitz Roy','70','Palermo','Buenos Aires','Argentina','5300'),
('Av. Cordoba','80','Balvanera','Buenos Aires','Argentina', '3000'),
('Calle Thames','90','Palermo','Buenos Aires','Argentina', '9000'),
('Calle Salguero','100','Palermo','Buenos Aires','Argentina', '6800'),
('Calle Malabia','200','Palermo','Buenos Aires','Argentina', '6200'),
('Calle Armenia','210','Palermo','Buenos Aires','Argentina', '8200'),
('Calle Cabrera','220','Palermo','Buenos Aires','Argentina', '3560'),
('Calle Gurruchaga','230','Palermo','Buenos Aires','Argentina', '6512'),
('Av. Dorrego','240','Palermo','Buenos Aires','Argentina', '1235'),
('Calle Humboldt','250','Palermo','Buenos Aires','Argentina', '6590'),
('Calle Guatemala','260','Palermo','Buenos Aires','Argentina', '3159'),
('Calle Bonpland','270','Palermo','Buenos Aires','Argentina', '5321'),
('Calle Jorge Luis Borges','280','Palermo','Buenos Aires','Argentina', '6310'),
('Calle El Salvador','290','Palermo','Buenos Aires','Argentina', '3256');
GO

SELECT * FROM Domicilios

-- ---- Tabla Usuarios ----
INSERT INTO Usuarios (email, apellido, nombre, contrasena, telefono, rol, fecha_nacimiento)
VALUES
('juan.perez@email.com','Perez','Juan','pass123','1111111111','Admin','1985-05-10'),
('maria.gomez@email.com','Gomez','Maria','pass456','2222222222','Usuario','1990-08-20'),
('carlos.rodriguez@email.com','Rodriguez','Carlos','pass789','3333333333','Usuario','1992-12-05'),
('laura.martinez@email.com','Martinez','Laura','passabc','4444444444','Admin','1988-03-15'),
('andres.lopez@email.com','Lopez','Andres','passxyz','5555555555','Usuario','1995-07-30'),
('sofia.ramirez@email.com','Ramirez','Sofia','pass001','6666666666','Usuario','1993-02-14'),
('diego.torres@email.com','Torres','Diego','pass002','7777777777','Admin','1987-09-25'),
('valentina.sanchez@email.com','Sanchez','Valentina','pass003','8888888888','Usuario','1991-11-11'),
('martin.morales@email.com','Morales','Martin','pass004','9999999999','Usuario','1989-06-05'),
('carolina.garcia@email.com','Garcia','Carolina','pass005','1010101010','Admin','1994-08-18'),
('nicolas.rojas@email.com','Rojas','Nicolas','pass101','1111111111','Usuario','1990-01-10'),
('ana.flores@email.com','Flores','Ana','pass102','2222222222','Admin','1988-02-20'),
('fernando.mena@email.com','Mena','Fernando','pass103','3333333333','Usuario','1992-03-15'),
('julieta.vega@email.com','Vega','Julieta','pass104','4444444444','Usuario','1991-04-12'),
('pablo.ramos@email.com','Ramos','Pablo','pass105','5555555555','Admin','1985-05-18'),
('isabella.toro@email.com','Toro','Isabella','pass106','6666666666','Usuario','1993-06-23'),
('lucas.ortiz@email.com','Ortiz','Lucas','pass107','7777777777','Usuario','1989-07-30'),
('sofia.castillo@email.com','Castillo','Sofia','pass108','8888888888','Admin','1994-08-05'),
('martin.castro@email.com','Castro','Martin','pass109','9999999999','Usuario','1995-09-09'),
('carla.molina@email.com','Molina','Carla','pass110','1010101010','Usuario','1992-10-14'),
('gonzalo.mendez@email.com','Mendez','Gonzalo','pass111','1111111111','Usuario','1987-03-12'),
('paula.diaz@email.com','Diaz','Paula','pass112','2222222222','Admin','1991-09-19'),
('jorge.fuentes@email.com','Fuentes','Jorge','pass113','3333333333','Usuario','1986-11-22'),
('marta.caballero@email.com','Caballero','Marta','pass114','4444444444','Usuario','1990-05-16'),
('roberto.martin@email.com','Martin','Roberto','pass115','5555555555','Admin','1985-08-08'),
('andrea.vargas@email.com','Vargas','Andrea','pass116','6666666666','Usuario','1992-12-30'),
('federico.soto@email.com','Soto','Federico','pass117','7777777777','Usuario','1989-07-17'),
('camila.rios@email.com','Rios','Camila','pass118','8888888888','Admin','1994-03-21'),
('daniel.moreno@email.com','Moreno','Daniel','pass119','9999999999','Usuario','1995-10-05'),
('soledad.alvarez@email.com','Alvarez','Soledad','pass120','1010101010','Usuario','1993-06-11');
GO

SELECT * FROM Usuarios

-- ---- Tabla Usuarios_Domicilios ----
INSERT INTO Usuarios_Domicilios (id_domicilio, email_usuario)
VALUES
(1,'juan.perez@email.com'),
(2,'maria.gomez@email.com'),
(3,'carlos.rodriguez@email.com'),
(4,'laura.martinez@email.com'),
(5,'andres.lopez@email.com'),
(6,'sofia.ramirez@email.com'),
(7,'diego.torres@email.com'),
(8,'valentina.sanchez@email.com'),
(9,'martin.morales@email.com'),
(10,'carolina.garcia@email.com'),
(11,'nicolas.rojas@email.com'),
(12,'ana.flores@email.com'),
(13,'fernando.mena@email.com'),
(14,'julieta.vega@email.com'),
(15,'pablo.ramos@email.com'),
(16,'isabella.toro@email.com'),
(17,'lucas.ortiz@email.com'),
(18,'sofia.castillo@email.com'),
(19,'martin.castro@email.com'),
(20,'carla.molina@email.com'),
(21,'gonzalo.mendez@email.com'),
(22,'paula.diaz@email.com'),
(23,'jorge.fuentes@email.com'),
(24,'marta.caballero@email.com'),
(25,'roberto.martin@email.com'),
(26,'andrea.vargas@email.com'),
(27,'federico.soto@email.com'),
(28,'camila.rios@email.com'),
(29,'daniel.moreno@email.com'),
(30,'soledad.alvarez@email.com');
GO
SELECT * FROM Usuarios_Domicilios

-- ---- Tabla Ubicaciones_casa ----
INSERT INTO Ubicaciones_casa (id_domicilio, nombre_ubicacion)
VALUES
(1,'Living'),
(1,'Cocina'),
(2,'Dormitorio'),
(2,'Baño'),
(3,'Garage'),
(3,'Living'),
(4,'Cocina'),
(4,'Dormitorio'),
(5,'Baño'),
(5,'Living'),
(6,'Cocina'),
(6,'Dormitorio'),
(7,'Baño'),
(7,'Living'),
(8,'Cocina'),
(8,'Dormitorio'),
(9,'Baño'),
(9,'Living'),
(10,'Cocina'),
(10,'Dormitorio'),
(11,'Living'),
(12,'Cocina'),
(13,'Dormitorio'),
(14,'Baño'),
(15,'Living'),
(16,'Cocina'),
(17,'Dormitorio'),
(18,'Baño'),
(19,'Living'),
(20,'Cocina');
GO

SELECT * FROM Ubicaciones_casa

-- ---- Tabla Dispositivos ----
INSERT INTO Dispositivos (id_ubicacion_casa, nombre_dispositivo, estado, descripcion, tipo_dispositivo, fecha_creacion)
VALUES
(1,'Luz Living',1,'Luz principal del living','Luz',GETDATE()),
(2,'Sensor Cocina',0,'Sensor de movimiento en cocina','Sensor',GETDATE()),
(3,'Cámara Garage',1,'Cámara de seguridad','Cámara',GETDATE()),
(4,'Termostato Dormitorio',1,'Control de temperatura','Termostato',GETDATE()),
(5,'Ventilador Baño',0,'Ventilador automático','Ventilador',GETDATE()),
(6,'Luz Cocina',1,'Luz cocina principal','Luz',GETDATE()),
(7,'Sensor Dormitorio',0,'Sensor de presencia','Sensor',GETDATE()),
(8,'Cámara Dormitorio',1,'Cámara seguridad','Cámara',GETDATE()),
(9,'Termostato Baño',1,'Control temperatura baño','Termostato',GETDATE()),
(10,'Ventilador Living',0,'Ventilador living','Ventilador',GETDATE()),
(11,'Luz Garage',1,'Luz exterior garage','Luz',GETDATE()),
(12,'Sensor Cocina 2',0,'Sensor adicional cocina','Sensor',GETDATE()),
(13,'Cámara Dormitorio 2',1,'Cámara dormitorio 2','Cámara',GETDATE()),
(14,'Termostato Dormitorio 2',1,'Control de temperatura dormitorio 2','Termostato',GETDATE()),
(15,'Ventilador Baño 2',0,'Ventilador baño 2','Ventilador',GETDATE()),
(16,'Luz Dormitorio',1,'Luz principal dormitorio','Luz',GETDATE()),
(17,'Sensor Living',0,'Sensor de presencia living','Sensor',GETDATE()),
(18,'Cámara Cocina',1,'Cámara cocina','Cámara',GETDATE()),
(19,'Termostato Living',1,'Control temperatura living','Termostato',GETDATE()),
(20,'Ventilador Dormitorio',0,'Ventilador dormitorio','Ventilador',GETDATE()),
(21,'Luz Baño',1,'Luz baño','Luz',GETDATE()),
(22,'Sensor Garage',0,'Sensor de garage','Sensor',GETDATE()),
(23,'Cámara Cocina 2',1,'Cámara cocina 2','Cámara',GETDATE()),
(24,'Termostato Garage',1,'Control temperatura garage','Termostato',GETDATE()),
(25,'Ventilador Dormitorio 2',0,'Ventilador dormitorio 2','Ventilador',GETDATE()),
(26,'Luz Dormitorio 2',1,'Luz dormitorio 2','Luz',GETDATE()),
(27,'Sensor Baño',0,'Sensor de baño','Sensor',GETDATE()),
(28,'Cámara Living',1,'Cámara living','Cámara',GETDATE()),
(29,'Termostato Cocina',1,'Control temperatura cocina','Termostato',GETDATE()),
(30,'Ventilador Living 2',0,'Ventilador living 2','Ventilador',GETDATE());
GO

SELECT * FROM Dispositivos

-- ---- Tabla Automatizaciones ----
INSERT INTO Automatizaciones (id_ubicacion_casa, descripcion_automatizacion, regla_automatizacion, condicion_automatizacion, accion, nombre_automatizacion)
VALUES
(1,'Encender luces al anochecer','Tiempo','19:00','Encender Luz','Luces Living'),
(2,'Apagar luces si no hay movimiento','Sensor','No movimiento','Apagar Luz','Cocina Off'),
(3,'Activar alarma al abrir puerta','Sensor','Puerta abierta','Activar Alarma','Alarma Garage'),
(4,'Encender calefacción','Tiempo','06:00','Encender Calefacción','Calefacción Dormitorio'),
(5,'Apagar ventilador automáticamente','Tiempo','22:00','Apagar Ventilador','Ventilador Baño'),
(6,'Encender luces automáticamente','Tiempo','19:30','Encender Luz','Luces Cocina'),
(7,'Apagar luces si no hay movimiento','Sensor','No movimiento','Apagar Luz','Dormitorio Off'),
(8,'Activar alarma al abrir ventana','Sensor','Ventana abierta','Activar Alarma','Alarma Dormitorio'),
(9,'Encender calefacción','Tiempo','07:00','Encender Calefacción','Calefacción Baño'),
(10,'Apagar ventilador automáticamente','Tiempo','23:00','Apagar Ventilador','Ventilador Living'),
(11,'Encender luces externas','Tiempo','20:00','Encender Luz','Garage Luz'),
(12,'Sensor adicional cocina','Sensor','No movimiento','Alerta','Alerta Cocina'),
(13,'Cámara vigilancia dormitorio','Sensor','Movimiento detectado','Activar Alarma','Cámara Dormitorio 2'),
(14,'Termostato control dormitorio 2','Tiempo','06:30','Encender Calefacción','Termostato Dormitorio 2'),
(15,'Ventilador baño 2','Tiempo','22:00','Apagar Ventilador','Ventilador Baño 2'),
(16,'Encender luz dormitorio','Tiempo','18:30','Encender Luz','Luz Dormitorio'),
(17,'Sensor living','Sensor','No movimiento','Apagar Luz','Sensor Living Off'),
(18,'Cámara cocina','Sensor','Movimiento detectado','Activar Alarma','Cámara Cocina'),
(19,'Control temperatura living','Tiempo','07:00','Encender Calefacción','Termostato Living'),
(20,'Ventilador dormitorio','Tiempo','22:30','Apagar Ventilador','Ventilador Dormitorio'),
(21,'Encender luz baño','Tiempo','19:00','Encender Luz','Luz Baño'),
(22,'Sensor garage','Sensor','No movimiento','Alerta','Sensor Garage'),
(23,'Cámara cocina 2','Sensor','Movimiento detectado','Activar Alarma','Cámara Cocina 2'),
(24,'Control temperatura garage','Tiempo','06:00','Encender Calefacción','Termostato Garage'),
(25,'Ventilador dormitorio 2','Tiempo','23:00','Apagar Ventilador','Ventilador Dormitorio 2'),
(26,'Encender luz dormitorio 2','Tiempo','18:45','Encender Luz','Luz Dormitorio 2'),
(27,'Sensor baño','Sensor','No movimiento','Apagar Luz','Sensor Baño Off'),
(28,'Cámara living','Sensor','Movimiento detectado','Activar Alarma','Cámara Living'),
(29,'Control temperatura cocina','Tiempo','07:15','Encender Calefacción','Termostato Cocina'),
(30,'Ventilador living 2','Tiempo','23:15','Apagar Ventilador','Ventilador Living 2');
GO

SELECT * FROM Automatizaciones

-- ---- Tabla Automatizaciones_dispositivos ----
INSERT INTO Automatizaciones_dispositivos (id_automatizacion, id_dispositivo)
VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(9,9),
(10,10),
(11,11),
(12,12),
(13,13),
(14,14),
(15,15),
(16,16),
(17,17),
(18,18),
(19,19),
(20,20),
(21,21),
(22,22),
(23,23),
(24,24),
(25,25),
(26,26),
(27,27),
(28,28),
(29,29),
(30,30);
GO

SELECT * FROM Automatizaciones_dispositivos