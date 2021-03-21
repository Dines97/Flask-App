# Simple Flask app
This app was created for bestcloud academy case study.
## Build
### Docker
```bash
sudo docker build -t <IMAGE NAME> .
```

## Run
### Docker
```bash
sudo docker run --name <CONTAINER NAME> --env WEBHOOK_URL=<WEBHOOK URL> -p <DESIRED PORT>:3000 -d <IMAGE NAME>
```
## Usage
### POST request

```bash
curl --X POST --header "Content-Type: application/json" --data '<JSON DATA TO POST>' http://localhost:<DESIRED PORT>/alert
```