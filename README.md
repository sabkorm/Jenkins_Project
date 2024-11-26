# Jenkins Project

## Overview

In this Jenkins project, the task was to create a Jenkins pipeline which runs through a Jenkinsfile stored on a Github repository, as part of the continous integration process. The Jenkinsfile would then build a Docker image from a Dockerfile stored on the same repository, and would push the new Docker image unto DockerHub. A GitHub Webhook would also be set in order to streamline the integration process, notifying Jenkins whenever there is a push to the repository, which will trigger a new build using the Jenkinsfile.

## The CI pipeline used in this project

### Jenkins pipeline

On the Jenkins interface, after setting up the GitHub and DockerHub credentials, we will create a Pipeline build. The pipeline will be defined as "**Pipeline script from SCM**", set up with the relevant Git repository that contains the Dockerfile and the Jenkinsfile.

Once this build is run, it will execute the pipeline script from the Jenkinsfile on GitHub.

### Jenkinsfile

The Jenkinsfile on the GitHub repository specifies the environment that will be used for the script, and the shell commands for each stage in the proccess of building a Docker image, logging into DockerHub and pushing the Docker image into DockerHub.

For example, the build command:
```
sh 'docker build -t $APP_NAME:$BUILD_NUMBER .'
```

The login command, which uses the variables from the DockerHub pre-set credentials:
```
sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
```
And the Push command:
```
sh 'docker push $APP_NAME:$BUILD_NUMBER'
```

### Dockerfile and DockerHub

The Docker Image that would be created from the Dockerfile is of a simple web application. Once the Jenkinsfile runs, it would use the Dockerfile (and the python file) to build a Docker Image that would then be pushed to DockerHub, which can then be used in further CI/CD processes. 

### GitHub Webhook trigger

For a more streamlined development workflow and smoother continuous integration, a GitHub Webhook can be used. The GitHub Webhook notifies Jenkins that there has been a push to the repository containing the Jenkinsfile, and triggers a new build.

When we create our pipeline build, we will need to set a **Build Trigger** for the GitHub push hook, using the following option:

`
GitHub hook trigger for GITScm polling
`

Then we will go to the GitHub repository > Settings in order to set up a Webhook. Under **Payload URL** we will enter the Jenkins server URL:

`
http://<jenkins_server>/github-webhook/
`
