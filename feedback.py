import pyautogui as pg
import webbrowser as wb
import time

site="https://academia.srmist.edu.in/#Page:Feedback_Polling_Page_2016_17"
wb.open(site,new=2)
time.sleep(10)

th = int(input("Enter the Theory subjects:--"))
pr = int(input("Enter the Practical subjects:--"))
comment=input("Enter the Comments:--")
time.sleep(10)
pg.press("tab")
pg.press("tab")
time.sleep(5)
for i in range (th):
    for j in range(14):
        time.sleep(2)
        pg.typewrite("x")
        time.sleep(2)
        pg.press("enter")
        pg.press("tab")
    pg.typewrite(comment)
    pg.press("tab")
    pg.press("tab")

time.sleep(10)
pg.press("tab")
time.sleep(10)

for i in range (pr):
    for j in range(13):
        time.sleep(2)
        pg.typewrite("x")
        time.sleep(2)
        pg.press("enter")
        pg.press("tab")
    pg.typewrite(comment)
    pg.press("tab")
    pg.press("tab")
time.sleep(10)
