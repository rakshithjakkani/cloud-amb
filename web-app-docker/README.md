2. Set Up a Virtualized Environment Using Docker
=================================================
Aim: Deploy python web application in docker 

pre-requesites:
    * Install docker on your machine or on EC2 (where you wanna host the docker container)

Process:
    Step: 1 (Creating dockerfile, build and run)
        * create a file called "Dockerfile" 
        * run "docker build -t <image_name> ." # dot should alos be there
        * run "docker images" #you should see your docker image
        * run "docker run -d -p 8000:8000 <image_name>:<tag>"
        * run "docker ps" #you should see your container up and running
        * run "netstat -tunlp" # to check which process is running on which port
    
    Step: 2 (Target Group and Load Balancer Attachment to container app)
        * click on create target group--> select "instance"--> enter TG name--> specify your VPC--> In register targets, select your instance--> enter 8000 port-->click on include as pending--> click on Create target group
        Note: In Health checks, enter /docker in Health check path
        * Go to Load Balancers, click on our load balancer, in Listener and rules tab, click on HTTP:80(in your case it may be different according to your listener and port), in Listener rules, click on Add rule, enter name--> next, click on Add condition, choose Path--> enter /docker--> confirm, select condition-->Next, select your newly created target group, enetr priority--> next--> create
        * once done, go to browser and enter load balancer domain like <domain>/docker. You should be able to get the page.
