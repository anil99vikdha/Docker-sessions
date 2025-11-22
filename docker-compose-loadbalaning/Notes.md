# Command to scale up greetapp. Compose will not support to define the number of replicas in compose yaml file
`docker compose up -d --scale greetapp=2`

- When running docker compose up -d --scale greetapp=2 with a docker-compose.yml that defines a ports section (e.g., - "8080:8080"), you will encounter a host port conflict error. This happens because:

- The ports section maps a container port to a specific host port.

- Only one container can bind to a specific host port at a time.

- Scaling the service to multiple replicas means multiple containers try to bind the same host port (8080), causing a conflict.

- Host port binding is exclusive: Only one container can listen on a given host port.

- When you scale replicas using docker compose --scale, all replicas try to bind the ports defined in the Compose file by default.

## This results in the error: Bind for 0.0.0.0:8080 failed: port is already allocated.

- To run multiple replicas without conflict, remove the ports section from the Compose YAML.

- Without ports, containers expose the ports internally within the Docker network only.


## To handle loadbalancing
Use a reverse proxy use nginx to expose a single host port and distribute traffic among greetapp replicas.

Alternatively, running multiple replicas with separate host ports (e.g., mapping different host ports manually or using port ranges) can prevent conflicts, but is not scalable or elegant.


# How can we check DNS resolution of greetapp (to find the containers mapped to this). Run a busybox which has utilities like nslookup, ping, wget in same network
docker run --rm -it --network docker-compose-loadbalaning_default busybox sh

Once inside container of busybox
# Run nslookup to find the containers mapped to this greetapp
nslookup greetapp
