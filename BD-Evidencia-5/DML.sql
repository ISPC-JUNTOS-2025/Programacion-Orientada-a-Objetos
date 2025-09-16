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