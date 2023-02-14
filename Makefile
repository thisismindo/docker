#up
up:
	docker compose up

#down
down:
	docker compose down

#reset
reset:
	docker compose down --rmi all --remove-orphans
	docker volume prune
	docker image prune
