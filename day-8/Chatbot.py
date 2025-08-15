# Task 8: Rule-based Chatbot with Basic NLP Structure and User Input.

import string

print("Hello! I’m ChatPy, your friendly chatbot.")

while True:
    # Step 1: Take input and normalize
    user_input = input("You: ").strip().lower()
    
    # Step 2: Exit condition
    if "bye" in user_input:
        print("ChatPy: Goodbye! Have a great day!")
        break
    
    # Step 3: Remove punctuation
    user_input = user_input.translate(str.maketrans("", "", string.punctuation))
    
    # Step 4: Tokenize the input
    tokens = user_input.split()
    
    # Step 5: Keyword-based responses
    if any(word in tokens for word in ["hi", "hello", "hey"]):
        name = input("ChatPy: Hello, Welcome to if-else Chatbot! What’s your name? ").strip()
        if name:
            print(f"ChatPy: Nice to meet you, {name}! \nIf you like we can begin chat.")
        else:
            print("ChatPy: Do you need any thing from my side?")
    
    elif "how" in tokens and "you" in tokens:
        print("ChatPy: I’m doing great! How about you?")
        feeling = input("You: ").strip().lower()
        feeling = feeling.translate(str.maketrans("", "", string.punctuation))
        if any(word in feeling for word in ["good", "great", "fine", "awesome", "well"]):
            print("ChatPy: Okay, that’s wonderful to hear! Do you need any thing from my side?")
        else:
            print("ChatPy: I hope your day gets better soon! Do you need any thing from my side?")
    
    elif "name" in tokens:
        print("ChatPy: My name is ChatPy. Do you need anything from my side?")
        
    elif "weather" in tokens:
        location = input("ChatPy: Which city are you in? ").strip()
        if location:
            print(f"ChatPy: I can’t check the weather in {location} yet, but I hope it’s nice there!")
        else:
            print("ChatPy: You didn’t tell me the city name! 🌤")
    
    elif "help" in tokens:
        print("ChatPy: Yes, I can chat with you. Tell me how can I help you?")
    
    else:
        print("ChatPy: I’m not sure & unable to understand as I am a beginner chatbot. Can you rephrase it again?")
