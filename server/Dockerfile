# docker build -t mdserver:latest .
# docker run -it --rm --name md mdserver /bin/bash
# docker run -d -p 3000:3000 mdserver:latest
# docker images
# docker ps
# docker logs -f <CONTAINER_ID>
# docker kill <CONTAINER_ID>
# http :3000/basic/1
FROM python:3.8.5-buster

EXPOSE 3000

WORKDIR /usr/src/app

# copy all not-ignored files to container
COPY . .

# create fresh conda env
# conda create --name mathdrill python=3.8
# pip freeze > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# start the web service
CMD ["./prod.sh"]
