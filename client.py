import socket
import threading

ip = '192.168.56.3'
port = 55555

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('utf-8')

            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                if nickname + ':' not in message:
                    print("\r" + message + "\n" + nickname +"> ", end="")
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input(nickname +"> "))
        client.send(message.encode('utf-8'))

# Starting Threads For Listening And Writing
write_thread = threading.Thread(target=write)
write_thread.start()

receive_thread = threading.Thread(target=receive)
receive_thread.start()

