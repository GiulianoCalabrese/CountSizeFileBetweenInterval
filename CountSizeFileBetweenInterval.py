import os
import time
from datetime import datetime
from time import mktime

path = os.getcwd()


start = input("put specific data start interval in format 2023-11-06T00:55:23.577Z :")
end = input("put specific data end interval in format 2023-11-06T00:55:23.577Z :")

print("start :"+ start)
print("end :"+ end)

#start = '2023-11-06T00:55:23.577Z'
#end = '2023-11-06T12:55:23.577Z'

t_obj = time.strptime(start,"%Y-%m-%dT%H:%M:%S.%fZ")
t_obj = datetime.fromtimestamp(mktime(t_obj))
start = (t_obj-datetime.fromtimestamp(0)).total_seconds()

t_obj = time.strptime(end,"%Y-%m-%dT%H:%M:%S.%fZ")
t_obj = datetime.fromtimestamp(mktime(t_obj))
end = (t_obj-datetime.fromtimestamp(0)).total_seconds()


result = 0
for root, dirs, files in os.walk(path):
    for name in files:
        # Both the variables would contain time elapsed since EPOCH in float      
        ti_c = os.path.getctime(os.path.join(root, name))  #ti_m = os.path.getmtime(path)
        if start <= ti_c <= end :    

            # Converting the time in seconds to a timestamp
            c_ti = time.ctime(ti_c)  #m_ti = time.ctime(ti_m)

            #print(f"The file located at the path {os.path.join(root, name)} was created at {c_ti}") # and was f"last modified at {m_ti}")
            #print(os.path.getsize(os.path.join(root, name)))
            result += os.path.getsize(os.path.join(root, name))

print(result)