docker build -f .\src\retriever\Dockerfile   -t retriever .
docker build -f .\src\export\Dockerfile   -t export .

docker compose up -d
docker cp ./data/ retriever:/app/data/