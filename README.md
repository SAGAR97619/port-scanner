# port-scanner
# Port Scanner API

## Run locally
docker build -t port-scanner .
docker run -p 5000:5000 port-scanner

## API

### Health
GET /health

### Scan
POST /scan
{
  "target": "scanme.nmap.org",
  "start": 20,
  "end": 100
}
