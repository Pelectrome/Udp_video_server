
import socket
from threading import Thread
import numpy as np
import base64
import cv2

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(f'Hostname: {hostname}\n Server IP Address: {IPAddr}')

VID_BUFF_SIZE = 65536

def UdpVidReceive():

    while True:
        packet, _ = UdpVidStream.recvfrom(VID_BUFF_SIZE)
        data = base64.b64decode(packet, ' /')
        npdata = np.frombuffer(data, dtype=np.uint8)
        frame = cv2.imdecode(npdata, 1)
    
        cv2.imshow("RECEIVING VIDEO",frame)
 
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            UdpVidStream.close()
            print("Connection Closed")
            break


if __name__ == "__main__":

    UdpVidStream = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    UdpVidStream.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,VID_BUFF_SIZE)
    UdpVidStream.bind(("0.0.0.0",5000))
   
    UdpVidReceive_thread = Thread(target = UdpVidReceive,daemon=True)
    UdpVidReceive_thread.start()
    UdpVidReceive_thread.join()
