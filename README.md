# Stock Ticker

[![Docker](https://github.com/yilun306/Stock_ticker_app/actions/workflows/push_dockerhub.yml/badge.svg?branch=main)](https://github.com/yilun306/Stock_ticker_app/actions/workflows/push_dockerhub.yml)

## Pulling private images from Docker Hub on GCP

1. pull docker image from the DockerHub:

```bash
docker pull yilun306/financial_portfolio_calculator:latest
```
2. Run the container using the following command:

```bash
docker run -it yilun306/financial_portfolio_calculator
```

## Pushing images to Docker Hub on GCP

1. Storing Docker credentials in Secret Manager
2. Configure the cloudbuild.yaml file:

```yaml
steps:
 - name: 'gcr.io/cloud-builders/docker'
   entrypoint: 'bash'
   args: ['-c', 'docker login --username=$$USERNAME --password=$$PASSWORD']
   secretEnv: ['USERNAME', 'PASSWORD']
 - name: "gcr.io/cloud-builders/docker"
   entrypoint: 'bash'
   args: ['-c', 'docker run $$USERNAME/REPOSITORY:TAG']
   secretEnv: ['USERNAME']
 availableSecrets:
   secretManager:
   - versionName: projects/PROJECT_ID/secrets/DOCKER_PASSWORD_SECRET_NAME/versions/DOCKER_PASSWORD_SECRET_VERSION
     env: 'PASSWORD'
   - versionName: projects/PROJECT_ID/secrets/DOCKER_USERNAME_SECRET_NAME/versions/DOCKER_USERNAME_SECRET_VERSION
     env: 'USERNAME'
```
3. build and push the container to Dockerhub
```bash
gcloud builds submit --config cloudbuild.yaml .
```

## Run locally using python virtual environment

```bash
virtualenv --python $(which python) venv

source venv/bin/activate

make
```
Note: Make sure to use Python version >= 3.6
