Rule-based Chatbot with Basic NLP Structure

1) Objective: Create a simple interactive chatbot in Python that uses basic Natural Language Processing (NLP) concepts without external libraries.

2) Features:
- Greets the user and asks for their name.
- Responds to:
  - Greetings ('hi', 'hello', 'hey')
  - "How are you" type questions.
  - Asking the chatbot's name.
  - Weather-related questions.
  - Help requests.
- Handles punctuation so keywords are matched correctly.
- Ends the conversation when the user types 'bye'.

3) Tools Used:
- Python 3.13.6 – Core programming language for building the chatbot.
- VS code - For executing the code.
- String library – Used for punctuation removal and text normalization.
- Basic I/O – For interactive communication with the user.
  
4) Basic NLP Concepts Used:
- Tokenization - 'tokens = user_input.split()' breaks input into individual words for easier matching.
- Case normalization - Converts all user input to lowercase so matching is consistent regardless of capitalization.
- Flexible keyword matching - ' "hello there" ' still matches ' "hello" ' because the program checks each token separately.
- Partial phrase detection - User can type a longer sentence like ' "Tell me your name" ' and it still matches ' "name" '.
  
5) Project Structure: day-8 Folder - Chatbot.py file - outputs Folder.
  
6) How to Run
- Ensure Python 3 is installed on your system.
- Place the 'Chatbot.py' file in a folder (e.g., 'day-8').
- Open a VS code and run the code.
- It will asks some inputs we need to give some chats to it then we are get the outputs as a chat.
- some of the example chats b/w "you as input from user and chatPy as output from the chatbot" are given below for reference:
  
    - chatPy: Hello! I’m ChatPy, your friendly chatbot.
  
    - You: hi
  
    - ChatPy: Hello! What’s your name? nandini
  
    - ChatPy: Nice to meet you, nandini! How are you?
  
    - Do you need any help today?
  
    - You: how are you
  
    - ChatPy: I’m doing great! How about you?
  
    - You: good
  
    - ChatPy: That’s wonderful to hear!
- And we can find screenshots of the outputs for the entered inputs in the "Output Folder" present in day-8 Folder.

