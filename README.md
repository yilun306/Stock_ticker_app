# Financial_Portfolio_Calc

## Pulling private images from Docker Hub on GCP

1. pull docker image from the DockerHub:

```bash
docker pull yilun306/financial_portfolio_calculator:latest
```
2. Run the container using the following command:

```bash
docker run -it yilun306/financial_portfolio_calculator
```

## Pushing images to Docker Hub from GCP

```bash
gcloud builds submit --config cloudbuild.yaml .
```
