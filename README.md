# Code_Alpha_Chatbot
# Simple Chatbot using NLTK 🤖

This is a basic chatbot built using the **Natural Language Toolkit (NLTK)**, designed to have simple conversations with users. It utilizes NLTK for tokenization, stemming, and understanding basic inputs.

## Features:
- Responds to basic user inputs.
- Uses **NLTK** for natural language processing (NLP), including tokenization and stemming.
- Simple rule-based responses with predefined patterns and keywords.
- Interactive console-based chat interface.

## Installation & Setup:
To run the chatbot locally, you need to have Python installed on your machine along with the necessary libraries.
2. Install the required libraries:
    
    pip install nltk
  

3. Download NLTK data:
    Open a Python shell and run the following to download the necessary NLTK data:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    ```

4. Run the chatbot:
    ```bash
    python chatbot.py
    ```

## How It Works:
The chatbot processes user input using the following steps:
- **Tokenization**: Splits the user's input into individual words.
- **Stemming**: Reduces words to their root form to better match predefined responses.
- **Pattern Matching**: Matches user input to a set of predefined patterns to generate responses.

## Example Interaction:
you: hi......> bot reply = hy there how are you 
you:what is your age>? bot reply: i am created today i am amachine i dont have age 
