import datetime
import time
end_time = datetime.datetime(2022,4,30)
site_block = ['www.facebook.com','www.youtube.com']
host_path = 'C:/Windows/System32/drivers/etc/hosts'
redirect = '127.0.0.1'

# while True:
    # checking that current time should be past then end time
if datetime.datetime.now()<end_time:
    print('Start Blocking')
    # open the file path with read and write mode
    with open(host_path,'r+') as host_file:
        # read the hosts file
        content = host_file.read()
        for website in site_block:
            # check the website is in the file or not
            if website not in content:
                #open the path and write the website name with host code
                host_file.write(redirect+' '+website+'\n')
            else:
                pass
else: # after the time end we have to onblock the website
    # open the file path with read and write mode
    with open(host_path,'r+') as host_file:
        # read the hosts file
        content = host_file.readlines()
        # take the file pointer to start
        host_file.seek(0)
        # check every line 
        for lines in content:
            # Check in the host file that if any site present or not
            if not any(website in lines for website in site_block):
                host_file.write(lines)

        # to get the original file
        host_file.truncate()
    time.sleep(5)