#  Proyecto Base de Datos - SmartHomeDB

Este proyecto contiene el diseño y carga de datos de la base de datos **SmartHomeDB**, desarrollada para la materia de Programación/BD.

## Contenido de la carpeta

- **Query_DDL_SmartHome.sql** → Script de creación de la base de datos y sus tablas (DDL).
- **Query_DML_SmartHome.sql** → Script de inserción de datos y ejemplos de consultas (DML).
- **README.md** → Instrucciones de ejecución.

---

## Motor de Base de Datos utilizado

El proyecto fue desarrollado en **SQL Server**.  
Para ejecutar los scripts de forma online (sin instalar nada), recomendamos usar:

--> [OneCompiler - SQL Server](https://onecompiler.com/sqlserver)

---

## Pasos para ejecutar los scripts

1. Acceder a [OneCompiler - SQL Server](https://onecompiler.com/sqlserver).
2. En la ventana de edición:
   - Copiar y pegar el contenido de `Query_DDL_SmartHome.sql`.
   - Ejecutar el script (Run).  
   Esto creará la base de datos y todas sus tablas.
3. Una vez creadas las tablas:
   - Copiar y pegar el contenido de `Query_DML_SmartHome.sql`.
   - Ejecutar nuevamente (Run).  
   Esto insertará **30 registros de prueba** en las distintas tablas.
4.  Ya se puede consultar y manipular los datos cargados.

---

## Notas importantes

- Los scripts usan:
  - `IDENTITY(1,1)` para autoincrementar claves primarias.
  - `GETDATE()` para registrar la fecha actual.
  - `GO` como separador de lotes (propio de SQL Server).
- Estos comandos no funcionan en otros motores como MySQL o PostgreSQL sin modificaciones.


---

## Autores

Trabajo realizado como parte de la **Evidencia N°5 - Base de Datos**.  
