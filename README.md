Certainly! Below is the content formatted using Markdown for a GitHub README:

---

# Loan Prediction Project

This project involves building and deploying a loan prediction model using FastAPI, Docker, and Jenkins.

## Setup

### 1. Setup Virtual Environment

```bash
conda create -n jenkins-env python=3.10 -y
conda activate jenkins-env
pip install -r requirements.txt
pip install .
```

### 2. Test the FastAPI

Sample JSON Payload for Testing:

```json
{
  "Gender": "Male",
  "Married": "No",
  "Dependents": "2",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5849,
  "CoapplicantIncome": 0,
  "LoanAmount": 1000,
  "Loan_Amount_Term": 1,
  "Credit_History": "1.0",
  "Property_Area": "Rural"
}
```

## Docker Commands

### Build and push the Docker image:

```bash
docker build -t loan_pred:v1 .
docker build -t kushaggra0001/loan_pred:latest .
docker push kushaggra0001/loan_pred:latest
```

### Run the Docker container:

```bash
docker run -d -it --name modelv1 -p 8005:8005 kushagra0001/loan_pred:latest bash
```

### Execute commands within the container:

```bash
docker exec modelv1 python prediction_module/training_pipeline.py
docker exec modelv1 pytest -v --junitxml=TestResults.xml --cache-clear
```

### Copy the test results from the container to the host:

```bash
docker cp modelv1:/code/src/TestResults.xml .

# Check if the test results file exists and is not empty
if [ -s TestResults.xml ]; then
    echo "Test results were successfully copied"
else
    echo "Test results file is missing or empty" >&2
    exit 1
fi
```

### Run the FastAPI application:

```bash
docker exec -d -w /code modelv1 python main.py
docker exec -d -w /code modelv1 uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8005
```

## Installation of Jenkins

### Install Jenkins:

```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

### Install Java:

```bash
sudo apt update
sudo apt install fontconfig openjdk-17-jre
java -version
```

### Enable and start Jenkins:

```bash
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

### Retrieve the initial admin password for Jenkins:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

## Docker Installation

### Add Docker's official GPG key and repository:

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Add Jenkins and the current user to the Docker group:

```bash
sudo usermod -a -G docker jenkins
sudo usermod -a -G docker $USER
```

## Configuring Jenkins

### Admin password for Jenkins:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

### Payload URL format for GitHub repo webhook:

```text
http://<public-ipv4 address>:8080/github-webhook/
# Replace <public-ipv4 address> with your own public IPv4 address
```

## Additional Improvements

### Remove all Docker containers and keep only the latest image:

```bash
docker remove $(docker ps -a -q)
docker images --format "{{.ID}} {{.CreatedAt}}" | sort -rk 2 | awk 'NR==1{print $1}'
```

### Before doing this, make all adjustments in Jenkins:

1. In Jenkins, go to system settings.
2. Set up a Jenkins URL and your email.
3. In the GitHub server section, add your GitHub credentials and create a GitHub webhook.
4. Set a default recipient for notifications.
5. In the cloud section, create a Docker cloud with accepted credentials.

## Creating and Pushing the Staging Branch

```bash
git checkout -b staging
git push
```

## Jenkins Pipeline Stages

### 1. Pull from GitHub

Take a pull of the GitHub repo:

```bash
https://github.com/kushagra8881/cicd_test_jenkin
```

Then build it and connect to Docker Hub:

```bash
docker build -t kushaggra0001/loan_pred:latest .
docker push kushaggra0001/loan_pred:latest
```

### 2. Training

Run the training script inside the Docker container:
docker exec modelv1 python prediction_module/training_pipeline.py
```bash
docker run -d -it --name modelv1 -p 8005:8005 kushagra0001/loan_pred:latest bash
```

### 3. Testing

Copy the test results from the container to the host:

```bash
docker cp modelv1:/code/src/TestResults.xml .

# Check if the test results file exists and is not empty
if [ -s TestResults.xml ]; then
    echo "Test results were successfully copied"
else
    echo "Test results file is missing or empty" >&2
    exit 1
fi
```

### 4. Deploy as API

Run the FastAPI application inside the Docker container:

```bash
docker exec -d -w /code modelv1 python main.py
```

## Configuring Jenkins URL

Navigate to the Jenkins installation directory:

```bash
cd /var/lib/jenkins/
```

Modify the `jenkins.model.JenkinsLocationConfiguration.xml` file:

```bash
sudo nano jenkins.model.JenkinsLocationConfiguration.xml
```

Make sure you provide the current Jenkins URL in the appropriate location and restart Jenkins:

```bash
sudo service jenkins restart
```

---

You can copy and paste this into your GitHub repository's README file. Adjust the content as needed to fit your project specifics.