from caesar import Caesar
from message import Message


def main():
    mess = str(input("Enter a message: "))
    shift = int(input("what shift to use in the Caesar cipher? "))
    caesar_obj = Caesar(shift)
    encrypted_mess = caesar_obj.encrypt(mess)
    src = str(input("who wrote the message? "))
    dest = str(input("who is it for? "))
    message_obj = Message(src, dest, encrypted_mess)
    print(message_obj.__str__())
    print(caesar_obj.decrypt(message_obj.data))


if __name__ == "__main__":
    main()
