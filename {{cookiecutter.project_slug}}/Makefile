dev-build:
	docker-compose run --name {{cookiecutter.project_slug}}_app_cleanup --rm app bash -c "rm -rf ~/.venvs/{{cookiecutter.project_slug}}venv" && \
	docker-compose build

update-time:
	docker-machine ssh default "sudo ntpclient -s -h pool.ntp.org"

bootstrap:
	touch production.env && \
	make dev-build

run:
	echo "Server will be coming up at http://`docker-machine ip`/" && \
	docker-compose up

shell:
	docker-compose run --name {{cookiecutter.project_slug}}_app_shell --rm app bash -c 'source ~/.venvs/{{cookiecutter.project_slug}}venv/bin/activate && python3 -ic "import {{cookiecutter.project_slug}}"'

test:
	docker-compose run --name {{cookiecutter.project_slug}}_app_tests --rm app bash -c 'source ~/.venvs/{{cookiecutter.project_slug}}venv/bin/activate && py.test --strict $${TEST_ARGS:-"tests/"}'

zappa:
	make update-time && \
	docker-compose run --name {{cookiecutter.project_slug}}_app_zappa --rm app bash -c 'source ~/.venvs/{{cookiecutter.project_slug}}venv/bin/activate && zappa ${ZAPPA_CMD}'
