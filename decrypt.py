from cgi import print_directory
from email import message
from math import sqrt
from unittest import result
import rosbag
bag = rosbag.Bag('message.bag')
data = []
for topic, msg, t in bag.read_messages():
    data.append( (chr(int(msg.data)-3)))
bag.close()
n = int(sqrt(len(data)))

for i in range(n):
    for j in range(i , n):
        data[i*n+j] , data[j*n+i] = data[j*n+i] ,data[i*n+j]

result = "".join(data)
print(result)
resultBag = rosbag.Bag('decrypted_message.bag', 'w')
from std_msgs.msg import String
try:
    message = String()
    message.data = result
    resultBag.write('decrypted_message', message)
finally:
    resultBag.close()
