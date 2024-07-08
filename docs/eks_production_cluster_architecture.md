# EKS Production Cluster Architecture Overview

This diagram represents the architecture of a production-grade Kubernetes cluster named "demo-prod" deployed within an AWS environment.

## Components:

- **VPC (Virtual Private Cloud):** Acts as the backbone of the cluster's network, providing isolation from other networks on AWS. It is the primary layer within which all other components reside, ensuring controlled network access and resource allocation.
- **Public Subnets:** Hosts the Elastic Load Balancer (ELB), which is the entry point for external traffic. The ELB efficiently distributes incoming traffic among the worker nodes located in the private subnets, ensuring high availability and fault tolerance.
- **Private Subnets:** Contains the worker nodes of the Kubernetes cluster. These EC2 instances are designated as "Worker Node 1", "Worker Node 2", and "Worker Node 3". Being in private subnets, these nodes are shielded from direct access from the internet, enhancing the security posture of the cluster. The nodes are responsible for running the containerized applications and handling the computational tasks of the cluster.
- **Load Balancer to Nodes Communication:** The diagram illustrates the flow of traffic from the ELB to the worker nodes. This setup ensures that external traffic can reach the applications running on the cluster, while keeping the compute resources in a secure network zone.

## Security and Accessibility:

- The use of public and private subnets within the VPC is a key security feature, ensuring that only the load balancer is exposed to the internet. This setup minimizes the attack surface by keeping the worker nodes in private subnets, thus not directly accessible from the outside world.
- The load balancer acts as the single point of entry for external traffic, distributing it across the worker nodes based on configured rules. This not only enhances security but also ensures efficient load handling and fault tolerance.

## Integration with ArgoCD for Continuous Deployment

This Production Cluster Architecture is also designed to facilitate the deployment of the ArgoCD application, a declarative, GitOps continuous delivery tool for Kubernetes. ArgoCD automates the deployment of applications to various environments, including production, by synchronizing application definitions with their desired state in a version control repository. The architecture's design, with its emphasis on security and scalability within the AWS environment, makes it an ideal foundation for implementing GitOps workflows with ArgoCD. For more details on deploying ArgoCD within this cluster and leveraging GitOps principles for continuous deployment, please refer to the dedicated GitHub repository: [ArgoCD Deployment on Amazon EKS with Terraform](https://github.com/DimitryZH/argo-cd-app-terraform).
