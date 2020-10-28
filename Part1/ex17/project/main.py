from datetime import datetime

with open('logs.txt', 'w') as f:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f.writelines("Container is created at: " + dt_string)
