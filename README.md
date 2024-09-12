# coldWork---Cold-Email-Generator-using-URL
# Project Overview
ColdHireMailer is an automated cold email generator using the provided URL from a Company's Careers page(or any job posting you find online). It allows you to easily tailor job application emails based on job postings by extracting the job description, matching the required skills with your projects (matching the Tech Stack used in the project), and generating a customized email. The tool ensures that each email is focused on relevant projects, making your application more targeted and professional.

# Features
* Extracts job descriptions and skills from provided URLs.
* Matches the job's requirements with your relevant projects and skills.
* Generates a personalized cold email for each job posting.
* Ensures the email focuses on specific, relevant projects, avoiding generic applications.
* Leverages natural language processing to tailor the email for each opportunity.

# Technologies Used
* Llama 3.1: Open-source large language model (LLM) used for text generation.
* Langchain: Framework for building applications around LLMs.
* Chroma DB: Vector database to store projects and skill sets for matching.
* Streamlit: Web framework used to create the front-end application.

# Setup Instructions

## Prerequisites

- Python 3.8+
- Git

## Installation

### Clone the Repository

Open Git Bash and navigate to the directory where you want to store the project. Run the following command to clone the repository:

```bash
git clone [https://github.com/shashank651156/coldWork](https://github.com/shashank651156/coldWork---Cold-Email-Generator-using-URL).git
```
### Create and Activate a Virtual Environment
Navigate into the project folder and create a virtual environment:
```bash
cd coldWork
python -m venv venv
```
Activate this venv using 
```bash
venv\Scripts\activate
```
###Install Dependencies
Install all required dependencies listed in requirements.txt:

```bash
pip install -r requirements.txt
```
### Add API Keys
Add your API keys and environment variables (for Groq) in a .env file at the root of your project directory:

``` bash
touch .env
```
Then, populate the file with your API key:
``` bash
GROQ_API_KEY = YOUR_OWN_API_KEY
```
## Usage
### Run the Application
Once the setup is complete, start the web application using Streamlit:

``` bash
streamlit run main.py
```
This will launch the ColdHireMailer tool in your browser, where you can input a job posting URL to generate a cold email.

Input the Job Posting URL
Paste the URL of the job posting in the input field. The application will extract the relevant skills and information from the job description.

### Match Skills
The tool automatically matches the extracted job description with your available projects stored in Chroma DB.

### Generate Cold Email
The tool will generate a customized email based on the job posting and your project(s) information.
(PS. - Don't forget to add your projects and change the prompt according to you.)

