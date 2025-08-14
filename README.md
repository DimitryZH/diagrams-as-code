# Diagrams as Code

## Project Overview

This project aims to utilize the "Diagrams as Code" approach for creating and maintaining system architecture and workflow diagrams. By treating diagrams like code, we can apply software engineering best practices such as version control, code review, and automated testing to the process of creating and updating diagrams. This repository contains the source code for generating diagrams, the generated diagrams themselves, and additional documentation.

## Technologies

[![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)

---

## Architecture & Workflow Diagrams

Below is a summary of the diagrams available in this project:

| Diagram Name                       | Source Script (.py)                                         | Documentation (.md)                                         | Diagram (.png)                                         |
|-------------------------------------|------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------|
| EKS Production Cluster              | [src/eks_cluster.py](src/eks_cluster.py)           | [docs/eks_production_cluster_architecture.md](docs/eks_production_cluster_architecture.md) | [diagrams/production_cluster.png](diagrams/production_cluster.png) | 
| AWS CodePipeline Infrastructure     | [src/aws_codepipeline.py](src/aws-codepipeline.py) | [docs/aws_codepipeline_infrastructure.md](docs/aws_codepipeline_infrastructure.md)         | [diagrams/aws_codepipeline_infrastructure_with_cloudformation.png](diagrams/aws_codepipeline_infrastructure_with_cloudformation.png)         |
| Argo CD Root App Manager            | [src/argo_cd_root_app.py](src/argo_cd_root_app.py)                         | [docs/argo_cd_root_app.md](docs/argo_cd_root_app.md)                                 | [diagrams/argo_cd_root_application_manager_overview.png](diagrams/argo_cd_root_application_manager_overview.png)                                 |
| GitHub Actions AWS CI/CD Pipeline   | [src/github_actions_aws_ci_cd.py](src/github_actions_aws_ci_cd.py)         | [docs/github_actions_aws_ci_cd.md](docs/github_actions_aws_ci_cd.md)                 | [diagrams/github_actions_aws_ci_cd.png](diagrams/github_actions_aws_ci_cd.png)                 |

> For more details and links to the projects where the diagrams are used, refer to the `/docs` directory.

---

## Diagram Descriptions

Each diagram in this project serves a specific purpose and provides insight into the architecture or workflow of different systems. For more details and links to the projects where the diagrams are used, refer to the `/docs` directory.


## How to Generate Diagrams

This project supports two types of diagrams: architecture diagrams (using the `diagrams` library) and workflow diagrams (using the `graphviz` library with YAML parsing).

### Architecture Diagrams

1. Ensure you have Python installed.
2. Install the `diagrams` library:
   ```shell
   pip install diagrams
   ```
3. Navigate to the `/src` directory.
4. Run the desired architecture diagram script, for example:
   ```shell
   python eks_production_cluster.py
   ```
5. The generated diagram will be saved as a `.png` file in the appropriate location.

### Workflow Diagrams

1. Ensure you have Python installed.
2. Install the required libraries:
   ```shell
   pip install graphviz pyyaml
   ```
3. Navigate to the `/src` directory.
4. Run the workflow diagram script, for example:
   ```shell
   python github_actions_aws_ci_cd.py
   ```
5. The generated workflow diagram will be saved as a `.png` file in the appropriate location.


