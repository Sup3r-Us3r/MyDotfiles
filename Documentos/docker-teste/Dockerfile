FROM node:latest-alpine

ENV HOME=/home/app

WORKDIR $HOME/fullstackapp

COPY package*.json .
RUN npm install --silent --progress=false
RUN npm install -g nodemon --silent --progress=false

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
