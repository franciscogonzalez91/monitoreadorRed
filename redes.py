import socket, struct, fcntl
import os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd = sock.fileno()
SIOCGIFADDR = 0x8915

def get_ip(iface = 'eth0'):
   ifreq = struct.pack('16sH14s', iface, socket.AF_INET, '\x00'*14)
   try:
       res = fcntl.ioctl(sockfd, SIOCGIFADDR, ifreq)
   except:
       return None
   ip = struct.unpack('16sH2x4s8x', res)[2]
   return socket.inet_ntoa(ip)

#print get_ip('eth0')


hostname = "10.0.2."#get_ip('eth0') #example
count = 0
while (count < 256):
  ipHost = hostname + str(count)
  response = os.system("ping -c 1 " + str(ipHost))

  #and then check the response...
  if response == 0:
    print "\n", ipHost, 'is online!'
  else:
    print ipHost, 'is offline!'

  count = count + 1

  