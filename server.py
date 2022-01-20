# The code has been tested on two separate Laptops
import socket
import time

############# User Defined getSize function in bytes from internet#########
def getSize(fileobject):
    fileobject.seek(0, 2)  # move the cursor to the end of the file
    size = fileobject.tell()
    return size
###########################################################################

MyIP = socket.gethostbyname(socket.gethostname()) #get server IP
PORT = 1234
BUFFER_SIZE = 4096
Myaddress = (MyIP, PORT)

send_times = [] #array of send times to calculate the avg
nb_of_bits_sender = [] #array of number of bits sent to get the avg

receive_times = [] #array of recieving times to calculate avg
nb_of_bits_receiver = [] #array of number of bits received to get the avg

# Print the IP address of the Host
print("Host's IP address is ", MyIP)


#Outer skeleton(While true and if protocol == TCP, if == UDP statements....)
#Are done by Mansour Abou Shaar

#### Bandwidth Calculations done by Mohamad Itani and Rana Chams Basha####
#### Avg Recieving Rate Calculations done by Haidar and Mansour ##########

##Detailed comments of bandwidth and recieving rate
# calculations on TCP protocol follow similarily for UDP 


while True: #Keep the code running indefinitely

    protocol = input("Would you like to use TCP or UDP Protocol?")

###############TCP Protocol Done by Haidar Yassine and Rana Chams Basha#########


    if str(protocol) == "TCP":

        # Define the Socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind IP and port to socket
        server.bind(Myaddress)

        # Listen to any client
        server.listen(5)
        print("[Listening]")

        # Establish connection between addr and the server
        conn, address = server.accept()
        print(address, "Has connected to the server ")

        #############################################

        option = input("Do you want to send or receive a file?")

        ##############################################

        if str(option) == "receive":

            # Enter the filename for the incoming file
            filename1 = input(
                str("Please enter a filename for the incoming file : "))

            # Open the file in write bytes mode so we can write data to the file
            file = open(filename1, 'wb') #write the incoming file into our created file

            # Receive file data
            start_time1 = time.time()
            file_data = conn.recv(1024)
            end_time1 = time.time()
            print("Server Received {file_data}")

            # Write the data of the file that we just received
            file.write(file_data)
            file_size1 = getSize(file) #get file size in bytes
            file.close()
            print("File has been received successfully")

            receivetime1 = end_time1 - start_time1 #calculate total recieving time
            print("Receive time is: ", receivetime1)
            receive_times.append(receivetime1) #add recieve time to the array

            nbits1 = file_size1 * 8 #calculate number of bits
            print("number of bits is: ", nbits1)
            nb_of_bits_receiver.append(nbits1) #add it to the array of bits

            total_time1 = 0 #total receiving time for all attempts
            total_bits1 = 0 #total number of bits received

            for i in range(len(receive_times)-1):
                total_time1 += receive_times[i]
                total_bits1 += nb_of_bits_receiver[i]

            if total_time1 != 0: #Prevent dividing by 0(sometimes recv time is negligble)
                recv_rate1 = total_bits1/total_time1
                print("receiving rate is: ", recv_rate1)

            else:
                print("The receiving rate is infinite")

        ###############################################

        elif str(option) == "send": #send files from server to client using TCP

            # Choose the file to send
            filename2 = input("choose the file to send :")

            # open the filename in read bytes mode
            file = open(filename2, 'rb')

            # read the file information
            file_data = file.read(1024)
            file_size2 = getSize(file)

            file.close()

            # Send the file data to the client
            start_time2 = time.time()
            conn.send(file_data)
            end_time2 = time.time()
            print("Data has been transmitted successfully")

            sendtime2 = end_time2 - start_time2 #calculate send time
            send_times.append(sendtime2) #append to array of send times

            nbits2 = file_size2 * 8 #get number of bits
            nb_of_bits_sender.append(nbits2) #append to array of bits

            total_time_sender1 = 0 #compute total sending time for all file transmitions
            total_bits_sender1 = 0 #compute total nb of bits for all file transmissions

            for i in range(len(send_times)-1):
                total_time_sender1 += send_times[i]
                total_bits_sender1 += nb_of_bits_sender[i]

            if total_time_sender1 != 0: #prevent division by zero(sometimes sendtime is negligble)
                avg_bandwidth = total_bits_sender1/total_time_sender1
                print("avg bandwith is: ", avg_bandwidth)

            else:
                print("The average bandwidth is infinite")

        # close the socket
        conn.close()

###############################################################


###########UDP Protocol Done by Mohamad Itani#############################    

    elif str(protocol) == "UDP":

        #Initialize Datagram Socket
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        

        option = input("Do you want to send or receive a file?")

        if str(option) == "receive":
            
            server.bind((MyIP, PORT))
            client_addr = ()

            # Enter the filename for the incoming file
            filename1 = input(
                str("Please enter a filename for the incoming file : "))

            # Open the file in write bytes mode so we can write data to the file
            file = open(filename1, 'wb')

            # Receive file data
            start_time3 = time.time()
            file_data, client_addr = server.recvfrom(BUFFER_SIZE)
            end_time3 = time.time()
            print("File has been received successfully")

            # Write the data of the file that we just received
            file.write(file_data)
            file_size3 = getSize(file)
            file.close()

            receivetime3 = end_time3 - start_time3
            print("Receive time is: ", receivetime3)
            receive_times.append(receivetime3)

            nbits3 = file_size3 * 8
            print("number of bits is: ", nbits3)
            nb_of_bits_receiver.append(nbits3)

            total_time3 = 0
            total_bits3 = 0

            for i in range(len(receive_times)-1):
                total_time3 += receive_times[i]
                total_bits3 += nb_of_bits_receiver[i]

            if total_time3 != 0:
                recv_rate2 = total_bits3/total_time3
                print("receiving rate is: ", recv_rate2)

            else:
                print("The receiving rate is infinite")

        ####################################################

        elif str(option) == "send":

            # Choose the file to send
            filename2 = input("choose the file to send :")

            # open the filename in read bytes mode
            file = open(filename2, 'rb')

            # read the file information
            file_data = file.read(1024)
            file_size4 = getSize(file)
            file.close()

            # Send the file data to the client
            start_time4 = time.time()
            server.sendto(file_data, Myaddress)
            end_time4 = time.time()
            print("Data has been transmitted successfully")

            # append sendtime to the list
            sendtime4 = end_time4 - start_time4
            print("send time is: ", sendtime4)
            send_times.append(sendtime4)

            # append file size to list
            fsizebits4 = file_size4 * 8
            print("number of bits is: ", fsizebits4)
            nb_of_bits_sender.append(fsizebits4)

            total_time_sender4 = 0
            total_bits_sender4 = 0

            for i in range(len(send_times)-1):
                total_time_sender4 += send_times[i]
                total_bits_sender4 += nb_of_bits_sender[i]

            if total_time_sender4 != 0:
                avg_bandwidth2 = total_bits_sender4/total_time_sender4
                print("avg bandwith is: ", avg_bandwidth2)

            else:
                print("The average bandwidth is infinite")

        # Close the server socket
        server.close()
