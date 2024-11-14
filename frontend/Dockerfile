FROM node:20.18.0-alpine
EXPOSE 5173

WORKDIR /app
COPY ./package*.json ./
RUN npm install
COPY . .

CMD ["npm", "run", "dev", "--", "--host"]