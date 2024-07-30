import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target_ip = "127.0.0.1"
target_port = 2525
target_address = (target_ip, target_port)

print("i am ready to chat.......")

condition = True
while condition:
    message = input("send : ") 
    message_encrypted = message.encode('ascii')
    s.sendto(message_encrypted, target_address)

    # get back response 
    response, sender_address = s.recvfrom(1024)
    recieved_respone = response.decode('ascii')
    print(f"                    response : {recieved_respone}")

    if message == "bye":
        condition = False
