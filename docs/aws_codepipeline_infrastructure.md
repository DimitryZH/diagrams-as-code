# AWS CodePipeline Infrastructure

This diagram illustrates the components and their interactions within an AWS CodePipeline setup.

## Components Overview

- **VPC (Virtual Private Cloud)**: Contains the EC2 instance.

  - **EC2 Instance**: Represents a virtual server in the AWS cloud.

- **CodeCommit**: A source control service hosting the repository.

  - **CodeCommit Repository**: The source repository for the pipeline.

- **CodePipeline**: The main pipeline orchestrating the workflow.

  - **Stages**:
    - **Source**: The source stage pulling code from CodeCommit.
    - **Deploy**: The deployment stage using CodeDeploy.
    - **Acceptance Test**: The testing stage using CodeBuild.

- **S3 (Simple Storage Service)**: Used as the artifact store for the pipeline.

- **IAM (Identity and Access Management)**: Manages roles and permissions.
  - **IAM Roles**: Roles assigned to the pipeline and EC2 instance.

## Key Features

The diagram visually represents the following flow:

1. **CodeCommit Repository** triggers the **Pipeline**.
2. The **Pipeline** consists of three stages: **Source**, **Deploy**, and **Acceptance Test**.
3. The **Pipeline** interacts with the **EC2 Instance** and stores artifacts in **S3**.
4. **IAM Roles** provide necessary permissions to the **Pipeline** and **EC2 Instance**.

This setup ensures a streamlined CI/CD process within AWS, leveraging various AWS services to automate code deployment and testing.

This diagram is used in the project [AWS CodePipeline Infrastructure as Code (IaC)](https://github.com/DimitryZH/cloudformation-codepipeline).
