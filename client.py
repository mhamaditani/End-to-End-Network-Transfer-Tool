#The code has been tested on two separate laptops
import socket
import time

############# User Defined getSize function in bytes from internet#########
def getSize(fileobject):
    fileobject.seek(0, 2)  # move the cursor to the end of the file
    size = fileobject.tell()
    return size
###########################################################################

IP = input(str("Please enter the Host IP address of the sender : "))
PORT = 1234
BUFFER_SIZE = 4096
address = (IP, PORT)

send_times = [] #array of sending times to calculate avg of sending times 
nb_of_bits_sender = [] #array of number of bits to get the avg

receive_times = []
nb_of_bits_receiver = []

#Outer skeleton(While true and if TCP, if UDP statements....)
#Are done by Mansour Abou Shaar


#### Bandwidth Calculations done by Mohamad Itani and Rana Chams Basha####
#### Avg Recieving Rate Calculations done by Haidar and Mansour ##########

##Detailed comments of bandwidth and recieving rate 
# calculations written on TCP protocol follow similarily for UDP 

while True: #keep the code running indefinitely

    protocol = input("Would you like to use TCP or UDP Protocol?")

###############TCP Protocol Done by Haidar Yassine and Rana Chams Basha#########
    if str(protocol) == "TCP":

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect IP, port to socket and listen
        client.connect(address)
        print("Connected ... ")

        #############################################

        option = input("Do you want to send or receive a file?")

        ##############################################

        if str(option) == "send":

            # Choose the file to send
            filename1 = input("choose the file to send :")

            # open the filename in read bytes mode
            file = open(filename1, 'rb') 

            # read the file information
            file_data = file.read(1024)
            file_size1 = getSize(file) #get the file size in bytes

            file.close()

            # Send the file data to the client
            start_time1 = time.time() #start the timer for sending
            client.send(file_data)
            end_time1 = time.time() #stop timer after file is sent
            print("Data has been transmitted successfully")

            sendtime1 = end_time1 - start_time1 #calculate total send time
            send_times.append(sendtime1) #add send time to the array

            nbits1 = file_size1 * 8 #calculate nb of bits
            nb_of_bits_sender.append(nbits1) #add it to the array of bits

            total_time_sender1 = 0 #total send time for all sending attempts
            total_bits_sender1 = 0 #total sent bits for all sending attempts

            for i in range(len(send_times)-1):
                total_time_sender1 += send_times[i]
                total_bits_sender1 += nb_of_bits_sender[i]

            if total_time_sender1 != 0: #Prevent dividing by 0(sometimes send time is negligble)
                avg_bandwidth = total_bits_sender1/total_time_sender1
                print("avg bandwith is: ", avg_bandwidth)

            else:
                print("The average bandwidth is infinite")

    ################################################

        elif str(option) == "receive": #receive files from server using TCP

            # Enter the filename for the incoming file
            filename2 = input(
                str("Please enter a filename for the incoming file : "))

            # Open the file in write bytes mode so we can write data to the file
            file = open(filename2, 'wb')

            # Receive file data
            start_time2 = time.time()
            file_data = client.recv(1024)
            end_time2 = time.time()
            print("File has been received successfully")

            # Write the data of the file that we just received
            file.write(file_data)
            file_size2 = getSize(file)
            file.close()

            recv_time1 = end_time2 - start_time2 #calculate recieving time
            print("send time is: ", recv_time1)
            receive_times.append(recv_time1) #append to array of recv times

            nbits2 = file_size2 * 8 #get number of bits
            print("number of bits is: ", nbits2)
            nb_of_bits_receiver.append(nbits2) #append to array of bits

            total_time_recvr1 = 0 #compute total receiving time for all file transmissions
            total_bits_recvr1 = 0 #compute total bits received for all file transmissions

            for i in range(len(receive_times)-1):
                total_time_recvr1 += receive_times[i]
                total_bits_recvr1 += nb_of_bits_receiver[i]

            if total_time_recvr1 != 0: #prevent dividing by zero(sometimes recvtime is negligble)
                recv_rate = total_bits_recvr1/total_time_recvr1
                print("receiving rate is: ", recv_rate)

            else:
                print("The receiving rate is infinite")

        # close the socket
        client.close()

    #################################################



###########UDP Protocol Done by Mohamad Itani#############################    

    elif str(protocol) == "UDP":

        #Initialize Datagram Socket
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        option = input("Do you want to send or receive a file?")

        if str(option) == "send":

            # Choose the file to send
            filename1 = input("choose the file to send :")

            # open the filename in read bytes mode
            file = open(filename1, 'rb')

            # read the file information
            file_data = file.read(1024)
            file_size3 = getSize(file)
            file.close()

            # Send the file data to the client
            start_time3 = time.time()  # starttime
            client.sendto(file_data, address)
            end_time3 = time.time()
            print("Data has been transmitted successfully")

            # append sendtime to the list
            sendtime3 = end_time3 - start_time3
            print("send time is: ", sendtime3)
            send_times.append(sendtime3)

            # append file size to list
            fsizebits3 = file_size3 * 8
            print("number of bits is: ", fsizebits3)
            nb_of_bits_sender.append(fsizebits3)

            total_time_sender2 = 0
            total_bits_sender2 = 0

            for i in range(len(send_times)-1):
                total_time_sender2 += send_times[i]
                total_bits_sender2 += nb_of_bits_sender[i]

            if total_time_sender2 != 0:
                avg_bandwidth = total_bits_sender2/total_time_sender2
                print("avg bandwith is: ", avg_bandwidth)

            else:
                print("The average bandwidth is infinite")

        ################################################

        elif str(option) == "receive":

            #Bind the client to the socket to recieve the file
            client.bind((IP, PORT))

            #Create server address tupple
            server_address = ()

            # Enter the filename for the incoming file
            filename2 = input(
                str("Please enter a filename for the incoming file : "))

            # Open the file in write bytes mode so we can write data to the file
            file = open(filename2, 'wb')

            # Receive file data
            start_time4 = time.time()
            file_data, server_address = client.recvfrom(BUFFER_SIZE)
            end_time4 = time.time()

            # Write the data of the file that we just received
            file.write(file_data)
            file_size4 = getSize(file)
            file.close()
            print("File has been received successfully")

            recv_time2 = end_time4 - start_time4
            print("send time is: ", recv_time2)
            send_times.append(recv_time2)

            nbits4 = file_size4 * 8
            print("number of bits is: ", nbits4)
            nb_of_bits_receiver.append(nbits4)

            total_time_recvr2 = 0
            total_bits_recvr2 = 0

            for i in range(len(receive_times)-1):
                total_time_recvr2 += receive_times[i]
                total_bits_recvr2 += nb_of_bits_receiver[i]

            if total_time_recvr2 != 0:
                recv_rate2 = total_bits_recvr2/total_time_recvr2
                print("receiving rate is: ", recv_rate2)

            else:
                print("The receiving rate is infinite")

        # Close the client socket
        client.close()
