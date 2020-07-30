# docker build -t mdclient:latest .
# docker run -it --rm --name md mdclient /bin/bash
# docker run -d -p 5000:5000 mdclient:latest
FROM node:buster
EXPOSE 5000
WORKDIR /usr/src/app
COPY . .
RUN npm install
RUN npm run build
CMD ["./prod.sh"]
