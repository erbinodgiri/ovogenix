FROM node:18

WORKDIR /app

COPY package.json .
RUN npm install --force

COPY . .

EXPOSE 5173

ENV ROLLUP_NO_PREBUILT=true 
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]