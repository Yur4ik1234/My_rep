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
