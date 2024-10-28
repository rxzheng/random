EMOJI_DICT_1 = {
    'a': '🍎', 'b': '🍌', 'c': '🍒', 'd': '🍇', 'e': '🍉', 'f': '🍓',
    'g': '🍑', 'h': '🎈', 'i': '🎁', 'j': '🎨', 'k': '🚗', 'l': '🚲',
    'm': '🚀', 'n': '⏰', 'o': '🔑', 'p': '📚', 'q': '💡', 'r': '🎵',
    's': '⚽️', 't': '🌸', 'u': '🎉', 'v': '🍁', 'w': '💯', 'x': '🌞',
    'y': '✨', 'z': '🌈'
}
e1 = {v: k for k, v in EMOJI_DICT_1.items()}

EMOJI_DICT_2 = {
    'a': '😀', 'b': '😃', 'c': '😄', 'd': '😁', 'e': '😆', 'f': '😅',
    'g': '😂', 'h': '🤣', 'i': '🔥', 'j': '😊', 'k': '😇', 'l': '🙂',
    'm': '🙃', 'n': '😉', 'o': '😌', 'p': '😍', 'q': '🥰', 'r': '😘',
    's': '😗', 't': '😙', 'u': '😚', 'v': '😋', 'w': '😛', 'x': '😝',
    'y': '😜', 'z': '🤪'
}
e2 = {v: k for k, v in EMOJI_DICT_2.items()}
EMOJI_DICT_3 = {
    'a': '🐶', 'b': '🐱', 'c': '🐭', 'd': '🐹', 'e': '🐰', 'f': '🦊',
    'g': '🐻', 'h': '🐼', 'i': '🐨', 'j': '🐯', 'k': '🦁', 'l': '🐮',
    'm': '🐷', 'n': '🐸', 'o': '🐵', 'p': '🐔', 'q': '🐧', 'r': '🐦',
    's': '🐤', 't': '🦆', 'u': '🦅', 'v': '🦉', 'w': '🦇', 'x': '🐺',
    'y': '🐗', 'z': '🐴'
}
e3 = {v: k for k, v in EMOJI_DICT_3.items()}
while True:
    choice = input("Enter 'e' to encode, 'd' to decode, or 'q' to quit: ")
    
    if choice == 'e':
        message = input("Enter the message to encode: ")
        encoded_message = ""
        count = 0
        for i in message:
            
            count += 1
            i = i.lower()
            if i == " ":
                encoded_message + " "
            elif count %3 == 1:
                encoded_message = encoded_message + EMOJI_DICT_1[i]
            elif count %3 == 2:
                   encoded_message = encoded_message + EMOJI_DICT_2[i]
            elif count %3 == 0:
                    encoded_message = encoded_message + EMOJI_DICT_3[i]
        print("Encoded message:", encoded_message)
    
    elif choice == 'd':
        emoji_message = input("Enter the emoji message to decode: ")
        decoded_message = ""
        if emoji_message == "🎁😅🌌🐹🍉😃🦅🍑😂🐨⏰😂🌌🐨⚽️🌌😙🐼🍉🌌😍🐦🔑😄🐰⚽️😗🌌🐵🍓🌌😘🐰🚀😌🦉🎁😉🐻🌌🍌😚🐻⚽️🌌😙🐼🍉😉🌌🐔🎵😌🐻🎵😀🐷🚀🔥🐸🍑🌌🙃🦅⚽️😙🌌🐱🍉🌌😙🐼🍉🌌😍🐦🔑😄🐰⚽️😗🌌🐵🍓🌌😍🦅🌸😙🐨⏰😂🌌🦆🎈😆🐷🌌🎁😉":
            decoded_message = None
        else:
            count = 0
            for b in emoji_message:
                count += 1
                
                if count %3 == 1:
                    decoded_message = decoded_message + e1[b]
                elif count %3 == 2:
                    decoded_message = decoded_message + e2[b]
                elif count %3 == 0:
                    decoded_message = decoded_message + e3[b]
                    

                
        
        print("Decoded message:", decoded_message)
    
    elif choice == 'q':
        break
    
    else:
        print("Invalid choice. Please try again.")