# Simple Flask app
This app was created for bestcloud academy case study.

Some commands below require additional changes to work. The place that is intended for change is indicated as follows `<VALUE>`. Below is a list of such changes with detailed descriptions.
* `<IMAGE NAME>` - The name you want to give the image after build.
* `<CONTAINER NAME>` - The name you want to give to the running container.
* `<WEBHOOK URL>` - The Webhook you want to use for /alert.
* `<DESIRED PORT>` - The port you want to use when accessing the API.
* `<JSON DATA TO POST>` - Information that should be in the POST request. Must be valid JSON.

## Build
### Docker
To build a Docker image.
```bash
sudo docker build -t <IMAGE NAME> .
```

## Run
### Docker
If the image was built locally.
```bash
sudo docker run --name <CONTAINER NAME> --env WEBHOOK_URL=<WEBHOOK URL> -p <DESIRED PORT>:3000 -d <IMAGE NAME>
```
Or you can run the image from my docker hub. Which was pushed around with Github Action.
```bash
sudo docker run --name <CONTAINER NAME> --env WEBHOOK_URL=<WEBHOOK URL> -p <DESIRED PORT>:3000 -d dines97/flask-app:tagname
```

## Usage
### POST request
For my tests, I used the following command. Attention, when using in other conditions than mine, you may need to change localhost to something else.
```bash
curl -X POST --header "Content-Type: application/json" --data '<JSON DATA TO POST>' http://localhost:<DESIRED PORT>/alert
```
### GKE and fourth task
For the fourth task, I chose to use Ingress. As far as I know Ingress uses Nginx for its work. Perhaps this is not the right decision, but that was new to me. So I wanted to put it into practice.

For tests, I am using minikube. The API for Ingress in minikube and APi for Ingress in GKE are slightly different. So I have supplied two .yaml files for two different situations. It is possible that when using my project on a different cloud platform, you will need to change the yaml file again.

Also, the WEBHOOK_URL environment variable is specified in the replication-set.yaml file, which may also need to be changed.

In order to deploy my application to GKE, need to execute the following commands.
```bash
kubectl apply -f ./k8s/replication-set.yaml -f ./k8s/load-balancer.yaml -f ./k8s/ingress-gke.yaml
```
In the case of ingress, the connection is made through port 80

### Deployed application
I have deployed the application to GKE. IP address 34.120.21.32. Example usage. http://34.120.21.32/whoami?firstname=Denis&lastname=Kaynar
