import time as time_module 

for i in range(5):
    local_time = time_module.localtime()
    seconds = local_time.tm_sec
    print(seconds)
    time_module.sleep(2)