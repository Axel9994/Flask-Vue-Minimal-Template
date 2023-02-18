# Usa una imagen base de Node.js
FROM node:14-alpine

# Crea el directorio de trabajo y establece el directorio de trabajo actual
WORKDIR /app

# Copia el archivo package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia todo el código fuente de la aplicación
COPY . .

# Compila y empaqueta la aplicación para producción
RUN npm run build

# Expone el puerto 8080 para que pueda ser accesible desde fuera del contenedor
EXPOSE 8080

# Inicia la aplicación
CMD [ "npm", "run", "serve" ]