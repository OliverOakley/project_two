# QA Practical Project - Prize Generator
## Outline
 
This is a microservice application that generates an account, and then determines as to whether the generated account has won a prize or not.
 
Whilst the application itself is simple, it is the deployment, buuilding, and hosting of the application that is of greatest concern here.

This application was built following the QA Practical Project guidelines, my second project as a QAC DevOps Trainee.

This application was built for training purposes only, and is not intended to be officially deployed or used.

## Requirements:
### Architecture:
The microservice application must consist of four services, utilising the following architecture.  
* Service 1 - Front-end of the application; communicates with the other three services.  
* Service 2 - Create a random string of letters, with at least 2 different implementations.  
* Service 3 - Create a random set of numbers, with at least 2 different implementations.  
* Service 4 - Create an account based on objects from services 2 and 3. Determine if the user has 'won', with two different implementations. Store account and prize winnings in a MySQL Database.  
### Features:
As well as adhering to the above architecture, the application must be capable of being:  
1. Fully integrated using the Feature-Branch model into a Version Control System.  
2. Be built through a CI Server and deployed to a cloud-based virtual machine.  
3. Able to be updated and then recreated and redeployed by the CI Server via Webhooks.  
4. Deployed using containerisation and an orchestration tool.  
5. Be accessible to the user via a reverse proxy.  
6. Have an environment provisioned so that it can run.  
### Tech:
The following technologies have been used to implement the above features:  
1. Git and GitHub are used for the Feature-Branch Model and Version Control System, as they are open-source industry staples.  
2. GCP is used for Cloud Services as it is generous with its free trial, and Jenkins is used for the CI Server as it is open-source.  
3. Jenkins Pipeline is used for continuous building and deployment, as it offers fast and flexible automation.  
4. Docker, Docker Compose, and Docker Swarm are used for containerisation and orchestration, as they are the most appropriate for simple deployment.  
5. NGINX is utilised for as a reverse proxy and load-balancer, as it is a fast web server for handling a large amount of concurrent connections.  
6. Ansible is used to write Playbooks for configuration management, it is open-source and easily accessible as Playbooks are written in YAML.  

## Planning:

For planning purposes, I created a Kanban Board on Trello. You can find it [here.](https://trello.com/b/9rVOaiOL/dd-character-generator)

Here is the initial version of the Kanban Board, before it is fully populated:
![kanban1](https://i.gyazo.com/4aac637eed4855dca13ecbc25baf7575.png)

## Risks and Issues:

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

Here is the risk assessment roughly halfway through development. Mitigated risks from the previous iteration are removed in this assessment:

| Description     | Evaluation     | Likelihood     | Impact Level  | Responsibility    | Response          | Control Measures      | Status |
| --------------- | -------------- | ---------------| --------------| ------------------| ------------------| ----------------------| -------|
| App goes down during an update to the code | Downtime for the application | Medium | High | Devs | Rebuild app with Jenkins | Continuous deployment with Jenkins so there is no downtime | Unmitigated |
| Secret keys unsecured | Security risk, compromises secure connection | Medium | High | Devs | Take them down to maintain security | Declare as environment variables to avoid having the secret keys on GitHub | Unmitigated |
| Nexus image repository has internal issues | Cannot create and pull down images | High | High | Sonatype | Use a different image repo | Currently using DockerHub instead | Mitigated |
| DockerHub is public rather than private | Images are less secure | Medium | Low | Devs/Docker | No response, ideally would use Nexus but its not working | Make sure nothing sensitive is uploaded to DockerHub | Mitigated |
| Jenkins, Swarm Manager and Application all stored on the same machine | May make the application run very slowly | Medium | Medium | Devs | Take it down, run Jenkins on separate VM | Create separate Jenkins/Swarm Manager VMs| Unmitigated |
  
## Cloud Server - GCP:

When it comes to the Cloud, I utilised GCP. Here, you can see the four VMs I have created on Ubuntu 20.10:

![gcp1](https://i.gyazo.com/e64d352407d892dba32784c49b813418.png)

By having all VMs set to europe-west2-b allows them to work together within a local network. Connected in this local network, the VMs have their own roles:  
* master-machine - The master of the Docker Swarm. It also creates the microservice application, connects to Jenkins, and connects to GitHub.
* worker-machine-1/2 - The two workers within the Swarm. They are connected to the Master, but contain little else.
* nginx-machine - Balances the load between the master and worker machines. Contains the nginx.conf file.

How these machines interact within the Swarm and the Network is neatly summarised by this image (courtesy of Suner Syuleyman):

![networkoutline](https://i.gyazo.com/14f71366772d6355cd00e70cfeb6fb76.png)

I also used a MySQL Database to store the generated strings and numbers from services 2 and 3, and the prizes generated from service 4. 

## CI Server - Jenkins:
### Jenkins Setup:
For CI and CD, I utilised Jenkins, and the initial setup was as follows:
* I opened port 8080 on my master-machine VM.
* Installed Jenkins on the VM using the following Docker command:  
    * docker run -d -p 8080:8080 --name jenkins jenkins/jenkins:lts-alpine
* Navigated to 34.89.9.247:8080, I created a new user, installed the recommended plugins, and created a Pipeline for the Prize Generator.  
* I then connected this Pipeline to my GitHub repo's master branch, where it would execute the script from the Jenkinsfile to build and deploy.  
* As this setup was done before actually building the application, for testing purposes my initial Jenkinsfile only contained a simple script that would echo 'test' and then clear the workspace on a successful build.
* As you can see, the Pipeline had successfully connected to my GitHub and ran the Jenkinsfile script:  

![jenkinstest](https://i.gyazo.com/062a47a5a8f575fe00f0b8cdcd4f5e53.png)

## Testing:



## Credits:

The application code was my own, with  spurred by the QA DevOps Practical Project specification.  
Whilst the code is entirely my own, I owe a lot to the QA Community resources, my trainer Dara Oladapo, and fellow QA Trainees.