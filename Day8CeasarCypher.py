alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
text_minus = text.replace(" ", "0")
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
def encrypt(text_minus, shift):
    initialletter_idx = []
    shiftedletter_list = []
    for letter in text_minus:
        # print(f"==========")
        # print(f"letter: {letter}")
        # print(f"==========")
        for inner_idx, inner_letter in enumerate(alphabet):
            # print(f"inner letter: {inner_letter}")
            # print(f"inner_idx: {inner_idx}")
            if letter == inner_letter:
                initialletter_idx.append(inner_idx)
            elif letter == "0":
                # print(f"letter is 0: {letter}")
                initialletter_idx.append("space")
                break
    # creation of initial letters list COMPLETE
    for num in initialletter_idx:
        # print(f"num: {num}")
        if num == "space":
            shiftedletter_list.append(" ")
        elif (int(num) + shift) <= 26:
            shifted_num = int(num) +shift
            shiftedletter_list.append(alphabet[shifted_num])
        else: 
            leftover = abs(26 - int(num) - shift)
            shifted_num = leftover - 1
            shiftedletter_list.append(alphabet[shifted_num])
    
    encoded_message = "".join(shiftedletter_list)
        
            
    # print(f"initial letter index: {initialletter_idx}")
    print(f"encoded message: {encoded_message}")

def decode(text_minus, shift):
    encrypted_initial_idx = []
    unshifted_letter_list = []
    for letter in text_minus:
        for inner_idx, inner_letter in enumerate(alphabet):
                # print(f"inner letter: {inner_letter}")
                # print(f"inner_idx: {inner_idx}")
                if letter == inner_letter:
                    encrypted_initial_idx.append(inner_idx)
                elif letter == "0":
                    # print(f"letter is 0: {letter}")
                    encrypted_initial_idx.append("space")
                    break
    for num in encrypted_initial_idx:
        # print(f"num: {num}")
        if num == "space":
            unshifted_letter_list.append(" ")
        elif (int(num) - shift) >= 0:
            shifted_num = int(num) - shift
            unshifted_letter_list.append(alphabet[shifted_num])
        else: 
            leftover = -abs(26 - int(num) - shift)
            shifted_num = leftover - 1
            unshifted_letter_list.append(alphabet[shifted_num])
    
    decoded_message = "".join(unshifted_letter_list)

    print(f"Decoded message: {decoded_message}")

if direction == "encode":
    encrypt(text_minus, shift)
else:
    decode(text_minus, shift)