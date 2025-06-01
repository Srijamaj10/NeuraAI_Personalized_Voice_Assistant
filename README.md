# NeuraAI Personalized Voice Assistant

NeuraAI is an intelligent personal voice assistant built using Python, OpenAI API, and speech synthesis technologies. It understands natural language voice commands, interacts with users using AI-generated responses, performs web searches, opens applications, tells time, writes emails on request, and saves chat prompts for later reference.

---

## Features

- **Voice Recognition:** Listens to user commands via microphone using SpeechRecognition.  
- **AI-powered Chat:** Uses OpenAI's GPT-3 to generate intelligent responses based on user input.  
- **Text-to-Speech:** Converts AI responses to natural-sounding speech.  
- **Web Automation:** Opens popular websites like YouTube, Google, and Wikipedia on voice commands.  
- **Time and Application Control:** Tells current time and can open system apps like Camera.  
- **Email Writing:** Can compose emails on your behalf, e.g., "Write an email for my boss for my resignation."  
- **Chat History Saving:** Saves user prompts and AI responses as text files for review in the `GeminiAI` folder.  
- **Configurable:** Easily modifiable for adding more commands or AI models.  

---

## Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/Srijamaj10/NeuraAI_Personalized_Voice_Assistant.git
Navigate to the project folder:

bash
Copy
Edit
cd NeuraAI_Personalized_Voice_Assistant
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\activate       # Windows
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
Add your OpenAI API key in the main script where indicated.

Usage
Run the main Python script to start the voice assistant:

bash
Copy
Edit
python main.py
Speak commands like:

"Open YouTube"

"What is the time?"

"Using artificial intelligence, explain photosynthesis"

"Write an email for my boss for my resignation"

"Neura quit" to exit

The assistant will respond via voice and save your prompts and AI responses in the GeminiAI folder.

## Author
## Name - Srija Majumdar
## Contact - https://www.linkedin.com/in/srija-majumdar-a686772a2
