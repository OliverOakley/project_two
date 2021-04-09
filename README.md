# QA Practical Project - Prize Generator
## Outline:
 
This is a microservice application that 'spins three fruit wheels' and 'rolls a dice'. If at least two of the 'fruit wheels' match, the user wins 100 'dollarydoos'. The amount won is multiplied by the 'dice roll'.
 
Whilst the application itself is simple, it is the deployment, building, and hosting of the application that is of greatest concern here.

This application was built following the QA Practical Project guidelines, my second project as a QAC DevOps Trainee.

This application was built for training purposes only, and is not intended to be officially deployed or used.

## Access:

To access the code for this application, you can clone from my GitHub repository, [project_two.](https://github.com/OliverOakley/project_two)

Python3 and pip3 are required on your Ubuntu 20.10 Linux machine to access the code. To access the code locally, run the following commands:  
1. git init  
2. git clone https://github.com/OliverOakley/project_two  
3. cd project_two  

From here, you can access the microservice application and their tests, the docker-compose.yaml for containerisation, the Jenkinsfile, and the Ansible Playbooks.

## Features:
### Application:
The microservice application consists of four services, each their own Docker container, utilising the following architecture:  
* Service 1 - Front-end of the application; communicates with the other three services. Stores rolls/spins and prize winnings in a MySQL Database.  
* Service 2 - 'Rolls a dice' (i.e. generates a random number between 1 and 6).  
* Service 3 - 'Spins three fruit wheels' (i.e. randomises three variables from a list that contains three different fruits)    
* Service 4 - Creates a prize based on the dice roll in Service 2 and the spins in Service 3. Determines if the user has 'won', and how much they have won.  

The microservice application utilises the following tech:  
* Python is the main language in which the application is written.
* Flask, SQLALchemy, and HTML (with Jinja2) are used to build the front-end of the application.
### Infrastructure:
The microservice application, as outlined above, is capable of being...:  
1. Fully integrated using the Feature-Branch model into a Version Control System.  
2. Built through a CI Server and deployed to a cloud-based virtual machine.  
3. Updated and then rebuilt and redeployed by the CI Server via Webhooks.  
4. Deployed using containerisation and an orchestration tool.  
5. Accessible to the user via a reverse proxy.  
6. Having its environment provisioned so that it can run.  
7. Fully tested to over 80% test coverage.  
### Tech:
The following technologies have been used to implement the above infrastructure:  
1. Git and GitHub are used for the Feature-Branch Model and Version Control System, as they are open-source industry staples.  
2. GCP is used for Cloud Services as it is generous with its free trial, and Jenkins is used for the CI Server as it is open-source.  
3. Jenkins Pipeline is used for continuous testing, building, and deployment, as it offers fast and flexible automation.  
4. Docker, Docker Compose, and Docker Swarm are used for containerisation and orchestration, as they are the most appropriate for simple deployment.  
5. NGINX is utilised for as a reverse proxy and load-balancer, as it is a fast web server for handling a large amount of concurrent connections.  
6. Ansible is used to write Playbooks to configure Docker Swarm and NGINX, as it is easily accessible as Playbooks are written in YAML.   
7. Testing is performed using the Flask-testing and Pytest libraries.  

## Planning:
### Kanban Board:
For planning purposes, I created a Kanban Board on Trello. You can find it [here.](https://trello.com/b/9rVOaiOL/prize-generator)

Here is a part of the initial version of the Kanban Board, before it is fully populated:
![kanban1](https://i.gyazo.com/4aac637eed4855dca13ecbc25baf7575.png)

Here is a part of my Kanban board, approximately half-way through development:

![kanban2](https://i.gyazo.com/b6379352cbe8ce23f5ece1a9b27ae3dc.png)
### Risk Assessment:
Here are the risks and issues I encountered throughout the development of the project. 

Here is the initial risk assessment I performed at the start of development:

| Description     | Evaluation     | Likelihood     | Impact Level  | Responsibility    | Response          | Control Measures      | Status |
| --------------- | -------------- | ---------------| --------------| ------------------| ------------------| ----------------------| -------|
| Run out of GCP Credits|Lose all access to VMs and Databases| Medium|  High| Devs | Create a new GMAIL account for a new free trial| Turn off VMs when not using them| Mitigated |
| Cloud Server is down | Cannot deploy application | Low | High | Google | Spin up a new VM with a new CSP | Keep source code up to date on GitHub | Mitigated |
| App goes down during an update to the code | Downtime for the application | Medium | High | Devs | Rebuild app with Jenkins | Continuous deployment with Jenkins so there is no downtime | Unmitigated |
| Library updates create incompatibilities between languages | Application will not build properly | Medium | High | Devs | Backdate languages to when they were compatible | Specify and use compatible versions only in requirement.txt| Mitigated|
| Floating VM IP makes accessing difficult between sessions | Cannot SSH in to the machine | High | Low | Devs | Reconnect using new IP | Keep known_hosts file clear, or using a static IP| Mitigated|
| Secret keys unsecured | Security risk, compromises secure connection | Medium | High | Devs | Take them down to maintain security | Declare as environment variables to avoid having the secret keys on GitHub | Unmitigated |

Here is the risk assessment roughly halfway through development. Mitigated risks from the previous iteration are ommitted:

| Description     | Evaluation     | Likelihood     | Impact Level  | Responsibility    | Response          | Control Measures      | Status |
| --------------- | -------------- | ---------------| --------------| ------------------| ------------------| ----------------------| -------|
| App goes down during an update to the code | Downtime for the application | Medium | High | Devs | Rebuild app with Jenkins | Setup Webhooks with Jenkins so there is no downtime | Mitigated |
| Secret keys unsecured | Security risk, compromises secure connection | Medium | High | Devs | Take them down to maintain security | Declare as environment variables to avoid having the secret keys on GitHub | Mitigated |
| Nexus image repository has internal issues | Cannot create and pull down images | High | High | Nexus | Use a different image repo | Currently using DockerHub instead | Mitigated |
| DockerHub is public rather than private | Images are less secure | Medium | Low | Devs/Docker | No response, ideally would use Nexus but its not working | Make sure nothing sensitive is uploaded to DockerHub | Partially Mitigated |
| Jenkins, Swarm Manager and Application all stored on the same machine | May make the application run very slowly | Medium | Medium | Devs | Take it down, run Jenkins on separate VM | Create separate Jenkins/Swarm Manager VMs| Mitigated |
| Must use virtual environments for testing | pytest --cov doesn't work otherwise | Low | Low | Devs | Restart the machine | Run testing and coding on venv | Mitigated |

Here is the final version of my risk assessment. Mitigated risks from previous iterations are ommitted:

| Description     | Evaluation     | Likelihood     | Impact Level  | Responsibility    | Response          | Control Measures      | Status |
| --------------- | -------------- | ---------------| --------------| ------------------| ------------------| ----------------------| -------|
| Unsecure SQL Database | SQL database can be accessed publicly | Low | Low | Don't store sensistive information on the database | Set network access to private only | Partially Mitigated | 

## Cloud Server - GCP:

When it comes to the Cloud, I utilised GCP. Here, you can see the five VMs I have created on Ubuntu 20.10:

![gcp1](https://i.gyazo.com/603c258a332654e0c9a08938539a3cf4.png)

By having all VMs set to europe-west2-b allows them to work together within a network. Connected in this network, the VMs have their own roles:  
* master-machine - Creates the microservice application, connects to Jenkins, and connects to GitHub. Holds the Ansible Playbook to configure the other four VMs.
* manager-machine - The manager of the Docker Swarm.
* worker-machine-1/2 - The two workers within the Swarm. They are connected to the manager via Docker Swarm.
* nginx-machine - Acts as a reverse proxy for the app and as a load balancer for the Swarm.

How these machines interact within the Swarm and the Network is neatly summarised by this image (courtesy of Suner Syuleyman):

![networkoutline](https://i.gyazo.com/14f71366772d6355cd00e70cfeb6fb76.png)

I also created a MySQL Database instance on GCP to store the results of the dice roll/wheel spins and the prizes won.  
The schema for the database is as follows:
* Prizes Table:
    * Diceroll - Stores the dice roll from service 2.
    * Fruit - Stores the three fruit spins from service 3.
    * Amount - Stores the amount won from service 4.

The database schema is defined in the service1/application/models.py.  
The schema is created by running 'python3 create.py', with the create.py file being stored in service1.

## Containerisation and Orchestration - Docker:
### Docker Setup:
Docker, Docker Compose, and Docker Swarm are my containerisation and orchestration tools.

I set up Docker and Docker Compose as follows:
* To install docker, I ran the following script:  
    * sudo apt-get update  
      sudo apt install curl -y  
      curl https://get.docker.com | sudo bash  
* I added current user to the group, and then restarted the terminal.
    * sudo usermod -aG docker $(whoami)
* To install Docker Compose I ran the following script:
    * sudo apt update
      sudo apt install -y curl jq
      version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
      sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
      sudo chmod +x /usr/local/bin/docker-compose
* I then created a docker-compose.yaml file where Docker Compose will be configured. 
### Images:
Each service is its own Docker image, with the layers of the image defined in each services' Dockerfile.  
The instructions in each of the Dockerfiles are as follows, where N = service number between 1 and 4:
* FROM python:3.7 - Defines the base image as python 3.7.
* WORKDIR /serviceN - Defines the working directory for the Docker instructions.
* COPY requirements.txt . - Copies the requirements.txt file, which has all the dependencies on it.
* RUN pip3 install -r requirements.txt - Installs all the dependencies from the requirements.txt file.
* COPY . . - Copies all files in the working directory to the image.
* EXPOSE 500N - Selects the port through which the containers listen to the image.
* ENTRYPOINT ["python", "app.py"] - Defines the main process for the container to run when it starts.
### Containers:
To define and run all 4 Docker containers simultaneously, I used Docker Compose. 
The configuration of these containers is handled by the docker-compose.yaml file.  
It creates each of our 4 services as their own container, with configuration for each as follows, where N = service number between 1 and 4:
* serviceN: - Defines the new service.
* container_name: serviceN - Names the container for the service.
* build: ./serviceN - Tells the container what to build, and from where.
* image: oliveroakley/serviceN:latest - Defines what image to use.
* ports: - Configures the port for the service.
Now, if I run the command 'docker-compose up', it will create all four services.  
* Lastly, to store images, I created a DockerHub account and image repository, that is connected to my GitHub repository. 
    * Originally I planned to use Nexus, but had some issues getting it working, as stated under Risks and Issues.
    * Executing 'docker-compose push' will push the images to my [DockerHub.](https://hub.docker.com/repository/docker/oliveroakley/service1)

These steps are automated by the Jenkins Pipeline, where the 'Build' and 'Push' stages of the Jenkinsfile build the containers and push the images to my DockerHub.
### Docker Swarm:
Docker Swarm is used for containerisation orchestration to run the containers across multiple machines.  
The Swarm Cluster consists of three VMs:
* manager-machine - The Swarm Manager, it manages the swarm cluster.
    * It is important that the Dev/Jenkins machine and Swarm Manager machine are not the same VM, as it may result in slow run times and may create issues if I were to setup another Swarm Manager within the cluster. This is outlined in my Risk Assessment above.  
* worker-machine-1/2 - The Workers within the Swarm, which run containers as per the instructions of the Manager.
    * Configuring new Workers would involve simply adding them to the Swarm, once having created the VM.  

Configuration of the Swarm occurs during the 'Configuration' part of the Jenkins Pipeline. In particular, the Swarm is initialised by Ansible (see below).

## CI/CD Server - Jenkins:
### Jenkins Setup:
For CI and CD, I utilised Jenkins, and the initial setup was as follows:
* I opened port 8080 on my master-machine VM.
* Installed Jenkins on the VM using the following Docker command:  
    * docker run -d -p 8080:8080 --name jenkins jenkins/jenkins:lts-alpine
* Navigated to {{master-machineIP}}:8080, where I created a new user, installed the recommended plugins, and created a Pipeline for the Prize Generator.  
* I then connected this Pipeline to my GitHub repo's master branch, where it would execute the script from the Jenkinsfile to build and deploy.  
* As this setup was done before actually building the application, for testing purposes my initial Jenkinsfile only contained a simple script that would echo 'test' and then clear the workspace on a successful build.
* As you can see, the Pipeline had successfully connected to my GitHub and ran the Jenkinsfile script:  

![jenkinstest](https://i.gyazo.com/062a47a5a8f575fe00f0b8cdcd4f5e53.png)

* To setup the CD aspect of Jenkins, so that I can easily deploy new versions of the application, I created a WebHook on GitHub to connect to Jenkins.  
* This will pull changes to the source code from GitHub automatically.
### Credentials:
I specified two important credentials within Jenkins:
1. Docker Hub Credentials - This allows Jenkins to push images to my DockerHub repository.
2. Database URI - Stores the URI for the database as a secure secret, so it is not openly available in the source code. 
    * This is then stored as an environment variable for the app to use when connecting to the database. This environment is set at the start of the Jenkins Pipeline.
### Jenkinsfile:
The Jenkinsfile tells the Jenkins Pipeline what to do when a build is scheduled.  
My Jenkinsfile has 5 stages:
1. Test - 
    * It is important that this stage is first, so that a broken build is not deployed. 
2. Build - Builds the Docker containers and their images, i.e. the four services of the application.
    * Does this by executing the 'docker-compose build' command.
3. Push - Pushes the images that were built to my DockerHub.
    * Does this by executing the 'docker-compose push' command.
    * It pushes to my DockerHub as I have set the DockerHub credential in Jenkins, and logged in to DockerHub on the Jenkins user on my master-machine.
4. Configure - Runs the Ansible Playbook which configures the NGINX reverse proxy and load balancer, and the Docker Swarm.
    * By running the Ansible Playbook, Jenkins SSHs into each machine and configures them appropriately.
    * How they are configured is defined by the Playbook and /ansible/roles. See 'Ansible' below for more information.
5. Deploy - Deploys the application.
    * It secure copies the docker-compose.yaml file from master-machine to manager-machine.
    * It then SSHs into the manager machine as the Jenkins user and deploys the swarm stack.

The commands for these 5 Jenkinsfile stages are run from scripts, stored within the scripts folder. This is so any issues with stages of the Pipeline can be solved by editing the scripts rather than the Jenkinsfile itself.

As we can see here, the Pipeline runs successfully:

[!jenkinssuccess]

Once the Pipeline has successfully ran, you can navigate to the publicIP of the nginx-machine to access the application.

## Environment Configuration - Ansible:
### Ansible Setup:
Ansible is used for environment configuration, in particular it defines the 'Configuration' step of the Jenkins Pipeline. All Ansible files are stored within the 'ansible' folder on my master-machine VM.  
To install Ansible I executed the following script as the Jenkins user on my master-machine VM:
* mkdir -p ~/.local/bin
* echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
* source ~/.bashrc
* sudo apt install python3-pip -y
* pip3 install --user ansible
* ansible --version

Once installed, I generated an SSH key as Jenkins user on my master-machine VM, and then added them as an SSH on each VM on GCP.  
This allows Jenkins to connect to each VM as a Jenkins user.
### Roles:
I use Ansible to configure the Docker Swarm and the NGINX load balancer across my four VMs.  
To do this, I have defined four roles for Ansible to configure, created by executing 'ansible-galaxy init {name-of-role}'.  
This application has four roles defined:
* Docker - Installs Docker on manager-machine and worker-machine-1/2. Is required to initialise the Docker Swarm.
* Manager - Sets manager-machine to be the Docker manager, which the workers will connect to.
* Worker - Sets worker-machine-1/2 to workers within the Swarm.
* NGINX - Installs NGINX on nginx-machine so it can act as a load balancer/reverse proxy.

These four roles are found in /ansible/roles. Each role has a set of tasks that define how to assign each role to the VMs, such as installing dependencies, installing Docker from the repository, etc.  
You can find the full list of tasks for each role within ansible/roles/{name-of-role}/tasks/main.
### Playbook and Inventory:
The Ansible Playbook, playbook.yaml, defines which hosts should have which role assigned to them.  
It takes the information for the host VMs from the inventory.yaml file. My inventory.yaml uses the VM names rather than IPs, as my VMs have floating IPs.  
Furthermore, the inventory.yaml file determines how Jenkins can connect to each VM, by defining the jenkins user and where it can find the ssh key required to connect to each VM.  
So, when the Jenkins Pipeline executes the configure.sh script, it runs the command for executing the Ansible playbook and inventory.  
In doing so, the Jenkins user SSHs into each machine and sets their roles according to the playbook.

## Testing:



## Credits:

The application is my own creation, spurred by the QA DevOps Practical Project specification.  
Whilst the code is entirely my own, I owe a lot to the QA Community resources, my trainers Dara Oladapo and Harry Volker, and my fellow QA Trainees.  
I also utilised a lot of code (particularly for the front-end) from my QA Fundamental Project, found [here.](https://github.com/OliverOakley/project_one)    
The network outline image used in 'Cloud Server - GCP' section was created by a fellow QA Trainee, Suner Syuleyman.  
Screenshots within this README.md are taken and stored using Gyazo.  
The free Visual Studio Code IDE was used to develop this application.