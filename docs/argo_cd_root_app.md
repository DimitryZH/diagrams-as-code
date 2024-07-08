# Argo CD Root Application Manager Diagram

The following Python script generates a diagram for the "Argo CD Root Application Manager" project, illustrating the architecture and workflow using Argo CD for managing Kubernetes applications across different environments. This script utilizes the `diagrams` library to create a visual representation of the system's components, including EKS clusters, Helm charts, Deployments, ELB, Argo CD, and GitHub as the version control system.

The diagram titled "Argo CD Root Application Manager Overview" visually encapsulates the architecture and operational workflow of a GitOps-driven deployment pipeline, utilizing Argo CD for managing Kubernetes applications across different environments. This diagram serves as a comprehensive representation of how various components interact within the system to achieve automated, scalable, and reliable application deployments. Below is an overview of the key features and components illustrated in the diagram:

### Key Features

- **Multi-Environment Deployment**: The diagram illustrates a clear separation between development and production environments, each managed within its own cluster. This setup supports distinct configurations for each environment, enabling smooth transitions and promotions of changes from development to production, thereby reducing deployment risks and increasing reliability.

- **Automated Synchronization**: By integrating Argo CD, the diagram highlights the system's capability to automatically synchronize application states with their desired states defined in Git repositories. This automation extends to deployment, pruning, and self-healing of application resources, ensuring that the applications are always in sync with the source code and configurations, thus facilitating a continuous deployment pipeline.

- **Customizable Helm Chart**: The use of Helm charts is depicted as a central component in managing Kubernetes resources, allowing for easy adaptation to different applications. The diagram shows how Helm charts are utilized in both development and production environments, supporting custom container images and replica counts. This flexibility enables quick adjustments and scalability of applications as per the requirements.

### Components Overview

- **EKS Cluster**: Serves as the backbone of the system, hosting the Kubernetes environment where applications are deployed.

- **GitHub Repo**: The source of truth for application code and configurations, demonstrating how changes in the repository trigger the deployment process through Argo CD.

- **Argo CD**: Central to the diagram, Argo CD manages the deployment process, ensuring that the state of applications in the Kubernetes cluster matches the configurations stored in the GitHub repository. It orchestrates the deployment of two applications, `App1` and `App2`, across both development and production environments.

- **Helm Charts**: Represented in both development and production clusters, Helm charts facilitate the deployment of applications by packaging all necessary Kubernetes resources.

- **ELB (Elastic Load Balancer)**: Illustrated within both environments, ELB distributes incoming traffic across multiple targets, such as EC2 instances, in multiple Availability Zones, increasing the fault tolerance of applications.

This diagram effectively communicates the architecture and operational dynamics of a GitOps-driven deployment system, emphasizing automation, scalability, and environment-specific configurations.

This diagram is used in the project ["Argo CD Root Application Manager](https://github.com/DimitryZH/argo-cd-app).
