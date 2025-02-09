Number Classification API 
Description
The Number Classification API is a simple RESTful API that takes a number as input and returns interesting mathematical properties about it. It also provides a fun fact related to the number.

Features
✔️ Checks if a number is prime or perfect
✔️ Identifies if a number is an Armstrong number
✔️ Determines whether a number is odd or even
✔️ Calculates the digit sum
✔️ Returns a fun fact about the number

Installation
To run this project locally, follow these steps:

1 Clone the repository

git clone <your-github-repo-url>
cd number-classification-api
2️ Create a virtual environment and activate it


python3 -m venv venv
source venv/bin/activate
 3 Install dependencies


pip install -r requirements.txt
4 Run the application

python app.py
The API should now be running on http://127.0.0.1:5000 🎉

How to Use the API
The API accepts GET requests with a number parameter.

Endpoint
GET /api/classify-number?number=<your_number>
Example Request

GET http://your-public-ip:5000/api/classify-number?number=371
Example Response (200 OK)

{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number."
}
Example Error Response (400 Bad Request)
{
  "number": "alphabet",
  "error": true
}
Deployment
The API is deployed and publicly accessible at:http://35.175.140.4:5000/api/classify-number?number=371

Technology Stack
🖥️ Backend: Python (Flask)
☁️ Deployment: AWS EC2
📦 Package Manager: Pip
📂 Version Control: Git & GitHub

Author
👤 Albert Guzmann
🔗 GitHub:https://github.com/GumwenroAlbert
🔗 LinkedIn:www.linkedin.com/in/osagumwenro-ogieva-aikuse-801b70238

