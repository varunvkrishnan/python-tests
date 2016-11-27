import webbrowser
import time

total_breaks = 0
print("This program started on "+time.ctime())
while total_breaks < 3:
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=XGMEx2bEyKM&list=PLQumh3Cy2Q2oeMChEd9ky7wdXvbMqJJrQ&index=8")
    total_breaks=total_breaks+1
