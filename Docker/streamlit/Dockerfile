FROM ubuntu

# RUN apk add --update --no-cache python3
# RUN apk add ffmpeg
# RUN apk add --update py-pip



RUN apt-get update
RUN apt-get install -y python3.10 ffmpeg
RUN pip install --upgrade pip



WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80

ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]
