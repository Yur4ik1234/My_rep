1. Using commands: 
`docker -v`,`docker -h`,`docker run docker/whalesay cowsay Docker is fun`
and redirect output to `my_work.log`

2. Using commands: `docker pull python:3.8-slim`,`docker images`,
`docker inspect python:3.7-slim`

3. Creating `Dockerfile` and pasting link to my Git.

4. Using commands: `docker build -t yur4ik1234/labdevops::django .`,
`docker images`, `dokcer push yur4ik1234/labdevops::django`

5. Using command `docker run -it --name=django --rm -p 
8000:8000 yur4ik1234/labdevops:django` 

6. Using command `sudo docker run -it --name=django --rm -p 8000:8000 yur4ik1234/labdevops:django`
 to run server.

7. Create Dockerfile.monitoring and build, using command
`sudo docker build --file Dockerfile.monitoring 
-t yur4ik1234/labdevops:monitoring`

8. Run server in background and use command `docker run -it --net=host --name=monitoring
 --rm -v $(pwd)/server.log:/app/server.log yur4ik1234/labdevops:monitoring` 
to save monitoring output to server.log

|        | Links           
| ------------- |:-------------:
| To rep    | https://hub.docker.com/r/yur4ik1234/labdevops|
| To django | https://hub.docker.com/layers/yur4ik1234/labdevops/django/images/sha256-33f69b90d4334f3757d7bf6cfed7dffdcddc608b2490ffa0b0a1918e897b572d?context=explore|
| To monitoring| https://hub.docker.com/layers/yur4ik1234/labdevops/monitoring/images/sha256-af3e553faa028859d916820fceaba28970928b9575c33e526ef629d80f1d419f?context=explore |


