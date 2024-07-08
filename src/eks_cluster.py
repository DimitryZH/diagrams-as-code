from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import VPC, PrivateSubnet, PublicSubnet, ELB

with Diagram("Development Cluster", show=False, direction="TB"):
    with Cluster("demo-dev"):
        with Cluster("VPC"):
            with Cluster("Public Subnets"):
                lb = ELB("Load Balancer")
            with Cluster("Private Subnets"):
                nodes = [EC2("Worker Node 1"),
                         EC2("Worker Node 2"),
                         EC2("Worker Node 3")]

            lb >> nodes

with Diagram("Production Cluster", show=False, direction="TB"):
    with Cluster("demo-prod"):
        with Cluster("VPC"):
            with Cluster("Public Subnets"):
                lb = ELB("Load Balancer")
            with Cluster("Private Subnets"):
                nodes = [EC2("Worker Node 1"),
                         EC2("Worker Node 2"),
                         EC2("Worker Node 3")]

            lb >> nodes