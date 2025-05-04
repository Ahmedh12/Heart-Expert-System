docker build -t heart-expert-system .
docker run --rm -v "$PWD/data:/app/data" heart-expert-system
