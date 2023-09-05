FROM ubuntu:latest

COPY . .

RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y x11vnc xvfb
RUN apt install ./google-chrome-stable_current_amd64.deb -y
RUN echo ". ./run.sh" > ~/.xinitrc && chmod +x ~/.xinitrc
CMD ["x11vnc", "-create", "-forever"]