FROM node:16.6.1-slim
WORKDIR /app/frontend
COPY package.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]