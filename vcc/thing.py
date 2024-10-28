# Emoji dictionaries for each position
EMOJI_DICT_1 = {
    'a': '🍎', 'b': '🍌', 'c': '🍒', 'd': '🍇', 'e': '🍉', 'f': '🍓',
    'g': '🍑', 'h': '🎈', 'i': '🎁', 'j': '🎨', 'k': '🚗', 'l': '🚲',
    'm': '🚀', 'n': '⏰', 'o': '🔑', 'p': '📚', 'q': '💡', 'r': '🎵',
    's': '⚽️', 't': '🌸', 'u': '🎉', 'v': '🍁', 'w': '💯', 'x': '🌞',
    'y': '✨', 'z': '🌈'
}

EMOJI_DICT_2 = {
    'a': '😀', 'b': '😃', 'c': '😄', 'd': '😁', 'e': '😆', 'f': '😅',
    'g': '😂', 'h': '🤣', 'i': '🔥', 'j': '😊', 'k': '😇', 'l': '🙂',
    'm': '🙃', 'n': '😉', 'o': '😌', 'p': '😍', 'q': '🥰', 'r': '😘',
    's': '😗', 't': '😙', 'u': '😚', 'v': '😋', 'w': '😛', 'x': '😝',
    'y': '😜', 'z': '🤪'
}

EMOJI_DICT_3 = {
    'a': '🐶', 'b': '🐱', 'c': '🐭', 'd': '🐹', 'e': '🐰', 'f': '🦊',
    'g': '🐻', 'h': '🐼', 'i': '🐨', 'j': '🐯', 'k': '🦁', 'l': '🐮',
    'm': '🐷', 'n': '🐸', 'o': '🐵', 'p': '🐔', 'q': '🐧', 'r': '🐦',
    's': '🐤', 't': '🦆', 'u': '🦅', 'v': '🦉', 'w': '🦇', 'x': '🐺',
    'y': '🐗', 'z': '🐴'
}

def encode(message):
    # OPTIONAL: Implement the encoding function
     for i in message:
            count = 0
            count += 1
            if count % 3 == 0:
                print(EMOJI_DICT_1[i], end=" ")
            elif count %3 == 1:
                print(EMOJI_DICT_2[i], end=" ")
            elif count %3 == 1:
                print(EMOJI_DICT_3[i], end=" ")
        

def decode(emoji_message):
    # Implement the decoding function
    pass

while True:
    choice = input("Enter 'e' to encode, 'd' to decode, or 'q' to quit: ")
    
    if choice == 'e':
        message = input("Enter the message to encode: ")
        encoded_message = encode(message)
        print("Encoded message:", encoded_message)

        
       
    
    elif choice == 'd':
        emoji_message = input("Enter the emoji message to decode: ")
        decoded_message = decode(emoji_message)
        print("Decoded message:", decoded_message)
    
    elif choice == 'q':
        break
    
    else:
        print("Invalid choice. Please try again.")