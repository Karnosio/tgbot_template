read -p "Enter name of migration: " message
docker compose exec bot aerich migrate --name "$message"