#!/bin/bash

scp -i ~/.shh/ansible_id_rsa docker-compose.yaml jenkins@master-machine:/home/jenkins/project_two/docker.compose.yaml
ssh -i ~/.ssh/ansible_id_rsa jenkins@master-machine << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file/home/jenkins/project_two/docker.compose.yaml todo-stack
EOF