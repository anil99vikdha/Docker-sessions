# Infra creation in AWS for Swarm setup
- Create VPC
- Subnets 
- Internet Gateway creation and attach to VPC
- Route Table with name Public and add route to IGW (Internet Gateway) and assoicate subnets with name public
- NAT-Gateway creation
- Route Table with name Private and add route to NGW (NAT-Gateway Gateway) and assoicate subnets with name Private
- Jumpbox ec2 and make sure port 22 opened for SSH access
- Create 3 Managed nodes
- Create 3 worker nodes

Security group ports:
Inbound rule:
Custom TCP -2377 - VPC CIDR
Custom TCP - 7946 - VPC CIDR
Custom UDP - 7946 - VPC CIDR
Custom UDP - 4789 - VPC CIDR