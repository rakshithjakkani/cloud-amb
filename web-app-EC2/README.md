1. Deploy a Simple Web Application
===================================
Aim: Deploying a sample python web application on EC2 and exposing it to public via Application load balancer

Pre-requisites: 
    * AWS Account with one EC2 instance launched
    * Necessary permission to create and edit a LB, target groups, security groups and EC2 
    * Open the ports 5000 and 8000 on EC2 security group to the 0.0.0.0/0

Process: 
    Step: 1 (Install dependencies)
    * For Amazon Linux 2:
        *  sudo yum update -y
        * sudo yum install python3 python3-pip -y
        * pip3 install flask
    
    Step: 2 (Copy the code and start the application)
    * connect to ec2 and switch to root user and create a file called app.py and paste the app.py content in that file
    * Then start the application using command "python3 app.py" for testing. Let application run on the machine 
    * Go to the browser and do request http://<EC2-Public-IP>:5000
    * You'll get the output.
    * stop the application by pressing control+c
    * run "sudo vi /etc/systemd/system/flask-app.service" and paste the flask-app.service content in it(make sure path and user correct)
    * then run below commands 
        sudo systemctl start flask-app
        sudo systemctl enable flask-app

    Step: 3 (Creating Target Groups and Application Load Balancer)
    * Open the EC2 console and create a target group
        * click on create target group--> select "instance"--> enter TG name--> specify your VPC--> In register targets, select your instance--> enter 5000 port-->click on include as pending--> click on Create target group
    * Creating Application Load Balancer
        * Click on Create LB--> under load balancer type, click on create in Application LB section--> name-->internet facing--> select VPC and subnets where your application is hosted--> select security group--> select your just created target group--> Click on create load balancer
        * Once load balancer has been created, copy the LB Domain and test it on the web. You should get a responce. if not, follow below steps.
        * open your LB security group and make sure that port 80 open to 0.0.0.0/0
        * open your EC2 security group and make sure that port 5000 open to 0.0.0.0/0 or open to LB security group.
