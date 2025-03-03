# Voice Assistant (Jarvis)

This is a Python-based voice assistant that can perform various tasks such as searching Wikipedia, opening websites, playing music, and providing COVID-19 statistics.

## Features
- Voice recognition and speech output
- Wikipedia search
- Open popular websites (Google, YouTube, Gmail, etc.)
- Search queries on Google
- Fetch real-time COVID-19 statistics
- Open system applications (Sublime Text, Notepad, Command Prompt, etc.)
- Take voice notes
- Play music from a specified directory

## Requirements
To run this project, install the following dependencies:

```sh
pip install speechrecognition pyttsx3 wikipedia beautifulsoup4 lxml requests
```

## How to Run
1. Clone this repository or copy the `main.py` file into a folder.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the script using:

```sh
python main.py
```

4. Speak commands when prompted.

## Commands List
- **Wake Word:** "Hey Jarvis"
- **Wikipedia Search:** "Search [topic] on Wikipedia"
- **Open Websites:** "Open YouTube", "Open Google", "Open Gmail"
- **Search Google:** "Search [query]"
- **Open Applications:** "Open Sublime", "Open Notepad", "Open Command Prompt"
- **Play Music:** "Play music"
- **Take Notes:** "Write this down" or "Note [text]"
- **COVID-19 Stats:** "Tell me COVID cases in [country]"
- **Greeting:** "Hi", "Hello", "Good morning/afternoon/evening"
- **Repeat Last Response:** "Repeat", "Again"
- **Exit:** "Quit", "End", "Deactivate"

## COVID-19 Statistics
The assistant fetches live COVID-19 case statistics from [Worldometer](https://www.worldometers.info/coronavirus/).

## Acknowledgments
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Pyttsx3](https://pypi.org/project/pyttsx3/)
- [Wikipedia API](https://pypi.org/project/wikipedia/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## Future Improvements
- Add more voice commands
- Improve accuracy in speech recognition
- Integrate AI-powered responses

## Contact
Author: [Mohammed Abdullah Amaan](mailto:abdullah@abdullahamaan.com)