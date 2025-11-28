a. Construir imagen:
docker build -t tienda-online:latest .

b. Ejecutar:
docker run --rm tienda-online:latest
docker run --rm -p 8000:8000 tienda-online:latest

c. Variables de entorno:
-e APP_ENV=development
-e PORT=8000
-e DATABASE_URL="..."

d. Pruebas:
Ver output en consola
http://localhost:8000/ en navegador/Postman
