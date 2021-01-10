1. In the file `requirements.txt` we have installed packeges.

2. I used next commands: `pipenv --python 3.8`,
`pipenv install -r requirements.txt`,`pipenv run python app.py`
The last command didn't work because Redis was not installed on my machine

3. I used command `sudo apt install redis-server` to install Redice and 
`sudo nano /etc/redis/redis.conf` to set supervised dirictive to `systemd`
And after that my site started working.

4. Used command `pipenv run pytest test_app.py --url http://localhost:5000`
to test all pages. Firstly it did not work, but after I vreated logs dir 
it started working. All 4 tests passed 

### Makefile

5. Makefile derictives 

*   STATES and REPO - variables that contain tag names and the Docker Hub repository name;
*   .PHONY - a make utility that tells the file that the following targets are not files;    $(STATES) - target purpose build container;
*    run - target designation for creating network that will run the application; launch the application and repository redis;
*    test-app - target to run tests;
*    docker-prune - target to clean resources to be used in the operation of Docker.

6. Using commands `sudo make app tests`, `sudo make run`, `sudo make test-app`

7. Usaing commands: `sudo make docker-prune` and  `sudo make docker-push` to 
push images

8. Creating `docker-compose.yaml`

*   public network  is used for interaction with site.
*   secret network  is used only for redis because of security (nobody could access from outside).

9. Checking docker-compose work with command `docker-compose version`

10. Using command `sudo docker-compose -p lab_5 up` site works we need to 
link 0.0.0.0

11. Using `docker-compose push` to push images to Dockerhub

12. For me `docker-compose` is more comfortable to use than Makefile, but
Makefile have a big advantage that there is ability to 
clean containers and images.

13. Making docker-compose.yml for lab4
