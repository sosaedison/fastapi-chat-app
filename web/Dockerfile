FROM node:latest
EXPOSE 3000
WORKDIR /app
COPY chatappweb/package.json ./
RUN yarn install
COPY ./chatappweb .
CMD ["npm", "start"]