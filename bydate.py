import os
import shutil
import os.path
import time

from datetime import datetime

# this function is used to sort by date

def bydate(path):

    lis = os.listdir(path)
    lis.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
    files = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]
    os.chdir(path)

    for x in files:

        # Get the last modified time and the creation time

        modified_time = time.ctime(
            os.path.getmtime(os.path.join(path, x)))

        modified_datetime = datetime.strptime(
         modified_time, '%a %b %d %H:%M:%S %Y')

        modified_date = str(modified_datetime.day) + '-' + str(
         modified_datetime.month) + '-' + str(modified_datetime.year)

        if(os.path.isdir(modified_date)):
            shutil.move(os.path.join(path, x), modified_date)
        else:
            os.makedirs(modified_date)
            shutil.move(os.path.join(path, x), modified_date)
    print("Done!!")
# import os
# import shutil
# import os.path
# import time

# from datetime import datetime

# # this function is used to sort by date
# class bydate:
#     def __init__(self,path):
#         self.path =path
#     def bydate1(self):

#         lis = os.listdir(self.path)
#         lis.sort(key=lambda x: os.stat(os.path.join(self.path, x)).st_mtime)
#         files = [f for f in os.listdir(
#             self.path) if os.path.isfile(os.path.join(self.path, f))]
#         os.chdir(self.path)
        
#         for x in files:

#         # Get the last modified time and the creation time

#             modified_time = time.ctime(
#                 self.os.path.getmtime(os.path.join(self.path, x)))

#             modified_datetime = datetime.strptime(
#             modified_time, '%a %b %d %H:%M:%S %Y')

#             modified_date = str(modified_datetime.day) + '-' + str(
#             modified_datetime.month) + '-' + str(modified_datetime.year)

#             if(os.path.isdir(modified_date)):
#                 shutil.move(os.path.join(path, x), modified_date)
#             else:
#                 os.makedirs(modified_date)
#                 shutil.move(os.path.join(path, x), modified_date)
#         print("Done!!")


# def by_date(path):
#     obj4 = bydate(path)
#     files = obj4.bydate1()

    
    