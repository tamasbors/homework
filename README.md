# DevOps Engineer Homework

## Overview

The goal of this assignment is to evaluate how you approach a typical DevOps engineering task involving:

- Application development / scripting
- Containerization
- Kubernetes
- Helm
- Terraform
- CI/CD
- Code review

The repository contains intentionally incomplete and imperfect components.
Your task is to complete, improve and document the solution.

You are not expected to produce a perfect production-ready system. We are more interested in your engineering approach, decision-making and ability to balance quality with the time constraints.

Time limit: approximately **3 hours**

## Repository Contents

The repository contains:

- An incomplete application skeleton
- Terraform configuration requiring review and improvement
- An incomplete Helm chart
- An incomplete CI/CD pipeline

Your task is to complete and improve these components. Our goal is to understand your engineering approach, and we will build the upcoming technical interview on this project.

## Goal 1

Complete and improve the provided project.

The repository contains the following files:

- Incomplete application code
- Broken/incomplete terraform configuration
- Incomplete Helm Chart
- Incomplete Gitlab CI pipeline

### Requirements

#### Application

Implement a simple application in either:

- Go
- Python

The application must expose the following endpoints:

##### `GET /health`

**Response:**

```json
{
    "status": "ok"
}
```

##### `GET /version`

**Response:**

```json
{
    "version": "1.0.0"
}
```

##### `GET /env`

**Response:**

```json
{
    "environment": "<value from ENVIRONMENT variable>"
}
```

##### `POST /config`

**Request:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

**Response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

##### `GET /config/{name}`

**Example:**

```bash
GET /config/database_url
```

**Response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

##### `DELETE /config/{name}`

**Response:**

```json
{
    "deleted": true
}
```

#### Containerization

- Create the necessary Dockerfile with minimal setup
- The image should:
  - build successfully
  - run locally
  - expose the application endpoint

#### Terraform

- Review and fix/complete the Terraform code
- The Terraform code contains several issues and areas for improvement
- In case you don't get time to implement changes describe what would you still improve and why
- Document any changes you make

#### Helm

- Review and fix/complete the Helm Chart
- The chart should deploy the application to Kubernetes
- Document any change you make

#### Gitlab CI

- Complete the pipeline so it becomes capable of building and deploying the application
- The pipeline should support the workflow required to build and deploy the application
- The pipeline should be logically complete and demonstrate how you would automate the process
- Add any other necessary jobs to the pipeline

#### Documentation

Update the project README with following information.

##### What You Changed

Describe the changes and the rationale behind it.

##### Assumptions

Describe the assumptions made while completing the assignment.

##### Known Limitations

Describe anything you intentionally omitted.

##### Production Improvements

Describe how you would evolve this solution for production use.

### Deliverables

- Source Code of the Go/Python application
- Dockerfile
- Terraform changes
- Helm changes
- CI pipeline changes
- README describing decisions, assumptions and user guide for the project.

### Notes

You are not expected to deploy to a cloud provider.
The solution should work with a local Kubernetes cluster such as:

- Kind
- Minikube
- K3d

### Timing

Timebox yourself to approximately **3 hours**. If you can't finish the work within the timebox, describe in the README.md what is left and how you would approach it.

## Goal 2

You get this half-baked project from one of your colleagues who is a Junior and asking for your guidance.

Provide a short code review in `REVIEW.md` where you address the **top 5 most important things** to fix so the colleague can move forward.

### Review Timing

Spend no more than **30 minutes** on review and feedback.

### Evaluation Criteria

We will evaluate:

- Code quality
- Terraform quality
- Kubernetes and Helm knowledge
- CI/CD design and implementation
- Documentation quality
- Code review quality
- Maintainability and operational thinking

### Use of AI

The use of AI-assisted tools is permitted. However, we encourage you to complete the assignment primarily based on your own knowledge, experience and reasoning. During the interview, we will discuss your implementation choices, trade-offs and decision-making process, so it is important that you fully understand and can explain every part of your solution.

---
# Solution

## Changes I have done

### Application
I implemented the `myapp.py` Flask application using AI based on the requirements from the README file.
In Dockerfile, just the requirements are installed, and the myapp.py copied. The applciation runs on port 8080.

### Helm
I fixed the empty lines, and indentations across all the files.
`service.yaml`: changed port to use variable
`ingress.yaml`: fixed the serivce name, and changed the port to variable
`deployment.yaml`: changed the containerPort, changed replicas to use the variable instead of the hard coded value
`values.yaml`: changed the serivce port to match with the expected port in the ingress (or ingress port should be changed)

### Terraform
`variables.tf`: default values, and descriptions added, and a few other variables
`terraform.tfvars`: created the varialbes file with values
`providers.tf`: I added the required providers with versions. Also changed the config_path to use variable. And last but not least, the local backend is configured.

### GitlabCI/Github Actions
- for both I created local runner on my computer
- On GitLab/GitHub I configured secrets for the action (docker credentials and `kube/config file`)

In both pipelines:
1. builds, tags, and pushes the Docker images to my docker repositoy.
2. the deploy job is running on my local computer (self-hosted/private-runner) where using the kube/config deploys the helm chart using terraform.

## Assumptions

- namespace/helm release does not exists yet
- local runner for GitLab/GitHub configured properly
- docker registri reacable from kubernetes cluster
- sufficient privilege on kubernetes cluster

## Known Limitations

- no smoke/integration test for the container
- a bit confusing port usage
- admin privileges in the kubeconfig file
- terraform state is not stored (no remote state)

## Production Improvements

- remote state for terraform
- use more variables
- testig
- destroy pipeline