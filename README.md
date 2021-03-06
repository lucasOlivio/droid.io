[![Build Status](https://travis-ci.com/lucasOlivio/droid.io.svg?branch=master)](https://travis-ci.com/github/lucasOlivio/droid.io)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)
[![License](https://img.shields.io/npm/l/react-native-smart-badge.svg)](https://github.com/lucasOlivio/droidio/blob/master/LICENSE)

Long live the Empire!

Droid.io is a project to help our allies in the best way we know, with a microservice to manage droids parts demands!
Only authenticated users can access and are able to create, edit, list and delete all his demands with ease.

------------------------------------------------------------------------------------------------------------------------
# SERVER

# Prerequisites

- [Docker Windows](https://docs.docker.com/docker-for-windows/install/)
- [Docker Linux](https://docs.docker.com/engine/install/)
- [Docker Mac](https://docs.docker.com/docker-for-mac/install/)

- [Docker-compose](https://docs.docker.com/compose/install/)

- [Pre-commit](https://pre-commit.com/#install)

# Local Development

- Create a folder named "local" inside the .envs and set the same variables as the .envs/test files

Start the dev server for local development:
```bash
docker-compose -f docker-compose.local.yml up
```

Run tests and tests coverage in container:

```bash
docker-compose -f docker-compose.local.yml run --rm server coverage run -m pytest
```

Run any command inside the docker container:

```bash
docker-compose -f docker-compose.local.yml run --rm server [command]
```

- First local run will create initial users
    - An administrator user:
        - username: admin
        - password: admin
    - And an advertiser user:
        - username: test
        - password: test
