# Install docker on all managed nodes
sudo yum update -y

sudo yum install -y yum-utils device-mapper-persistent-data lvm2

sudo yum install -y docker

sudo systemctl start docker
sudo systemctl enable docker

docker --version


# Create a docker swarm cluster
1. Initialize Swarm on the First Manager Node 
docker swarm init --advertise-addr <MANAGER1-IP>

2. To join other managed nodes to the cluster
sudo docker swarm join-token manager
docker swarm join --token <MANAGER_JOIN_TOKEN> <MANAGER1-IP>:2377

3.  Verify the Swarm Cluster on the First Manager
sudo docker node ls


## Add worker nodes
docker swarm join --token <WORKER_JOIN_TOKEN> <MANAGER1-IP>:2377


````Example section```
[ec2-user@ip-10-10-4-130 ~]$ sudo docker swarm init --advertise-addr 10.10.4.130
Swarm initialized: current node (vcxp4kwcyd5z5ezv9lkvv1l2x) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-1zsfy0owkc514a5thl2kzizso4irvbuinc7gh5m4smj0z5awhj-ei2mx2xuzzffruqnda5kkw6ie 10.10.4.130:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

[ec2-user@ip-10-10-4-130 ~]$ sudo docker swarm join-token manager
To add a manager to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-1zsfy0owkc514a5thl2kzizso4irvbuinc7gh5m4smj0z5awhj-7p5kd90zbgzi8zgkp43gtwok7 10.10.4.130:2377
``` Example```


# These tokens can be used for future addition of managed and worker nodes. Incase if you think tokens might compromised or to follow security best practice. Rotate tokens by using follow commands. 
**Note**: Existing nodes not affected with token change

docker swarm join-token --rotate worker
docker swarm join-token --rotate manager



# Deploy greetapp with redis in docker swarm
docker stack deploy -c docker-stack.yml mystack

## To remove deployed stack
docker stack rm mystack

## To list running services
docker service ls

## To scale greetapp
docker service scale mystack_greetapp=5

## Access application using any of the node ip
http://<MANAGER or Worker-IP>:8080

