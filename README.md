# OneView_CarWash
OneView Car Wash Application Designed for Local Car Wash Vender  

# Application Side:  
pip install python  
pip install -r requirements.txt  
python manage.py runserver 8000  

# Server Side:  
Launch EC2 instance 
Install Docker and Jenkins 

# CI/CD CodePipeline and Jenkins:  
## Jenkins:
Add GitHub integration plugin  
Intregrate Jenkins with GitHub  
Add docker build using Dockerfile and run command in Build Step  
Execute automated pipeline 

## Codepipeline:  
Use CodeCommit to integrate with Github using Webhooks  
Use CodeBuild for building stage using build.yaml file  
Use CodeDeploy for deploying application using ElasticBeanStalk  




