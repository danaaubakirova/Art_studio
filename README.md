# Random Language Generator

This Python script uses the speech_recognition library to convert speech to text and a symbol mapping dictionary to generate a "random language" version of the input text. The user can speak into a microphone or type a text input to be translated. The translation is performed by replacing each letter in the input text with a corresponding symbol defined in the symbol mapping dictionary.

## Installation

1. Clone or download this repository to your local machine.
2. Install the required libraries by running **pip install -r requirements.txt** in your terminal or command prompt.

## Usage

1. Run the script by executing the command python **sr.py** in your terminal or command prompt.
2. Adjust the microphone input volume by speaking at a normal level and observing the printed feedback. If the feedback indicates that the input is too loud or too quiet, adjust your microphone settings accordingly.
3. Speak into the microphone or type a text input when prompted. To exit the program, type the word "stop" or use the keyboard interrupt command (e.g., Ctrl+C).
4. Observe the printed output of the translated text.

## Configuration

The script expects a **symbol_mapping.json** file to be present in the same directory. This file should contain a JSON object with keys corresponding to lowercase letters of the alphabet and values corresponding to their corresponding symbol representation in the "random language" alphabet. The default symbol_mapping.json file provided in this repository maps each lowercase letter to a different symbol from the Wingdings font. You can customize this file to define your own symbol mapping for the "random language" alphabet.
