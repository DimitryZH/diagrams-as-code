# Diagrams as Code

## Project Overview

This project aims to utilize the "Diagrams as Code" approach for creating and maintaining system architecture diagrams. By treating diagrams like code, we can apply software engineering best practices such as version control, code review, and automated testing to the process of creating and updating diagrams. This repository contains the source code for generating diagrams, the generated diagrams themselves, and additional documentation.

## Technologies

[![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)

## How to Generate Diagrams

To generate diagrams from the source code, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the `diagrams` library using pip:

   ```shell
   pip install diagrams
   ```

For detailed guidance, refer to the [official documentation](https://diagrams.mingrammer.com/docs/getting-started/installation).

3. Navigate to the `/src` directory where the Python scripts for diagram generation are located.
4. Run the desired script to generate a diagram. For example:

   ```shell
   python eks_cluster.py
   ```

5. The generated diagrams will be saved as .png image files.

## Diagram Descriptions

Each diagram in this project serves a specific purpose and provides insight into the architecture of different systems. For more details and links to the projects where the diagrams are used, refer to the `/docs` directory.
