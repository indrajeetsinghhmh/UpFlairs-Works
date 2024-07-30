import socket
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ip_address = "192.168.43.249"
ip_address = "127.0.0.1"
port_no = 2525
complete_address = (ip_address, port_no)
s.bind(complete_address)

print("i am listnening.......")

cond = True
while cond: 
    message, sender_ip_address = s.recvfrom(1024)
    message = message.decode('ascii')

    # get current time and date 
    t = datetime.datetime.now().strftime("<%I:%M:%S> <%d %b, %Y>")

    print(f"                    recieved : {message}")
    with open("cliaudits.txt", "a") as file:
    # Write some values to the file
        file.write(f"{message }  from  {sender_ip_address}           {t}\n")


    # sending response 
    response_message = input("reply : ")
    encrypted_response = response_message.encode('ascii')
    s.sendto(encrypted_response, sender_ip_address)

    if(message == "bye"):
        cond = False