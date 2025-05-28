docker build -f Dockerfile-vnc -t snapchat-bot-vnc .
docker run --rm -v $(pwd)/driver_user:/app/driver_user -p 6080:6080 snapchat-bot-vnc