# free-chatgptapi

**free-chatgptapi** is a simple Flask web application that provides an API for interacting with the OpenAI GPT chat interface. It allows users to launch GPT chat sessions, send prompts, and retrieve responses.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Launch GPT Session](#launch-gpt-session)
  - [Send Prompts](#send-prompts)
  - [Stop GPT Session](#stop-gpt-session)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (version 3.6 or higher)
- pip (Python package installer)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/free-chatgptapi.git
   cd free-chatgptapi
2.Install the required dependencies:

    '''bash
    pip install -r requirements.txt
### Aditional
#### Exposing Localhost with ngrok

For testing purposes, you can use [ngrok](https://ngrok.com/) to expose your local Flask application to the internet. Follow these steps:

1. **Download and Install ngrok:**

   Download and install ngrok from [ngrok.com](https://ngrok.com/).

2. **Start your Flask application:**

   ```
   python app.py
3. Running ngrok:

In a new terminal, navigate to the directory where ngrok is installed and run the following command:

    ```
    ngrok http 5000
## Usage

### Launch GPT Session

1.To launch a new GPT chat session, make a GET request to the /launch endpoint:

    '''
    curl -X GET "http://localhost:5000/launch?username=your_username&pass=your_password"
This will return a JSON response with the status and the generated driverid for the session.
The Json contains the driver id(['driverid']) which you will need to pass on later two requests to connect to your driver.

2.Send Prompts
To send a prompt to an existing GPT chat session, make a GET request to the /promt/<int:driverid> endpoint:

    '''
    curl -X GET "http://localhost:5000/promt/your_driverid?prompt=your_prompt_text"
    This will return a JSON response with the prompt and the GPT-generated response.

3.Stop GPT Session
To stop an existing GPT chat session, make a GET request to the /stop/<int:driverid> endpoint:

    '''
    curl -X GET "http://localhost:5000/stop/your_driverid"
### API Endpoints
1./launch: Launches a new GPT chat session.
2./promt/<int:driverid>: Sends a prompt to an existing GPT chat session.
3./stop/<int:driverid>: Stops an existing GPT chat session.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License
This project is for educational purposes only.This project is licensed under the MIT License.

    '''
    Remember to replace placeholders like `your_username`, `your_password`, and `your_driverid` with the appropriate values. Also, ensure that you have accurate information about the API endpoints and functionality based on your actual code implementation.




