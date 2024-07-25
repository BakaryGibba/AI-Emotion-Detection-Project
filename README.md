# Emotion Detection System

## Introduction
This project involves building an emotion detection system using IBM Watson Embedded AI and BERT (Bidirectional Encoder Representations from Transformers). The application analyzes the text input to detect the underlying emotions such as happiness, sadness, anger, etc.

## Features
* **Emotion Detection**: Analyzes text input to detect emotions using the BERT model and IBM Watson.
* **Web Interface**: User-friendly web interface for entering text and displaying results.
* **Powered by IBM Watson and BERT**: Utilizes IBM Watson's and BERT's advanced natural language processing capabilities.

## Project Structure
<img width="530" alt="Screenshot 2024-07-19 210531" src="https://github.com/user-attachments/assets/98b08247-7db0-4073-95d6-c52eaf5c93f2">


* **'static/'**: Contains static files such as JavaScript.
* **'templates/'**: Contains HTML templates for the web interface.
* **'server2.py'**: Flask server script to run the web application.
* **'emotion_detection.py'**: Script containing the emotion detection logic.
* **'test_emotion_detection.py'**: Test script for emotion detection functionalities.

## Usage
1. Run the Flask server:

<img width="531" alt="Screenshot 2024-07-19 210857" src="https://github.com/user-attachments/assets/f448c411-8b33-4fcc-80d5-49891081bb86">

2. Open your web browser and go to **http://localhost:5000**.
3. Enter the text you want to analyze in the input box and click **"Run Emotion Analysis"**.

## Example
To analyze the emotions in the text "I am very happy today!", simply enter the text in the input box and click **"Run Emotion Analysis"**. The result will indicate that the primary emotion detected is happiness.

## Testing
To run the test, execute the following command


<img width="528" alt="Screenshot 2024-07-19 211159" src="https://github.com/user-attachments/assets/25bffb09-f8a6-4133-946d-9d324f0cdfa8">

## Contributing 
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the **LICENSE** file for details.

## Acknowledgments
* IBM Watson for providing the emotion detection API
* Flask for the web Framework
* The BERT team for the emotion detection model

## The Emotion Detection Interface:

<img width="958" alt="Screenshot 2024-07-19 212332" src="https://github.com/user-attachments/assets/7ebfd9a3-994d-4206-b1dd-ec1cf31c460f">
