from tkinter import Tk, Label
from PIL import Image, ImageTk
from math import sqrt




def perecentr(schet, centroids, pixels):
    new_centroids = []
    for i in range(len(centroids)):
        count, r, g, b = 0, 0, 0, 0
        for (r1, g1, b1), c in pixels:
            if c == i:
                r += r1
                g += g1
                b += b1
                count += 1
        if count > 0:
            r = r//count
            g = g//count
            b = b//count
            new_centroids.append((r,g,b))
        else:
            new_centroids.append(centroids[i])

    for i in range(len(centroids)):
        schet += abs(centroids[i][0]-new_centroids[i][0]) + abs(centroids[i][1]-new_centroids[i][1]) + abs(centroids[i][2]-new_centroids[i][2])
            
    centroids = new_centroids
    return schet, centroids, pixels



def perevod(color):
    r, g, b = color
    return f'#{int(r):02x}{int(g):02x}{int(b):02x}'
'''
    rr = hex(r)[2:]
    gg = hex(g)[2:]
    bb = hex(b)[2:]
    if len(rr) < 2:
        rr = "0" + rr
    if len(gg) < 2:
        gg = "0" + gg
    if len(bb) < 2:
        bb = "0" + bb
    return f"#{rr}{gg}{bb}"
'''

root = Tk()
root.title("Jetpack")
root.geometry("800x450")
pilImage = Image.open("sea.jpg")
pilImage = pilImage.resize((600, 450), Image.ANTIALIAS)
image = ImageTk.PhotoImage(pilImage)
picture = Label(root, image=image)
picture.place(x=0, y=0)
colors = []


pixels=[]


minr = 120
ming = 120
minb = 120
maxr = 140
maxg = 140
maxb = 140
min1r = 120
min1g = 120
min1b = 120
max1r = 140
max1g = 140
max1b = 140
for (r,g,b) in pilImage.getdata():
    if r < minr and g < ming and b < minb:
        minr = r
        ming = g
        minb = b
    if r > maxr and g > maxg and b > maxb:
        maxr = r
        maxg = g
        maxb = b
    if r < min1r and g > max1g and b > max1b:
        min1r = r
        min1g = g
        min1b = b
    if r > max1r and g < min1g and b < min1b:
        max1r = r
        max1g = g
        max1b = b 
 
centroids = [(127,127,127), (minr,ming,minb), (min1r,max1g,max1b), (maxr, maxg, maxb), (max1r, max1g, min1b)]    

print(centroids)

#centroids = [(0,0,0), (0,255,255), (127,127,127), (255, 0, 255), (255, 255, 0)]
for (r,g,b) in pilImage.getdata():
    m = 0
    for i in range(1, 5):
        if sqrt((r-centroids[i][0])**2+(g-centroids[i][1])**2+(b-centroids[i][2])**2) < sqrt((r-centroids[m][0])**2+(g-centroids[m][1])**2+(b-centroids[m][2])**2):
            m = i
    pixels.append(((r,g,b), m))
        
schet = 20
while schet > 13:
    (schet, centroids, pixels) = perecentr(0, centroids, pixels)



print(centroids)
color0 = Label(root, bg=perevod(centroids[0]), width=25, height=5)
color0.place(x=630, y=5)
color1 = Label(root, bg=perevod(centroids[1]), width=25, height=5)
color1.place(x=630, y=95)
color2 = Label(root, bg=perevod(centroids[2]), width=25, height=5)
color2.place(x=630, y=185)
color3 = Label(root, bg=perevod(centroids[3]), width=25, height=5)
color3.place(x=630, y=275)
color4 = Label(root, bg=perevod(centroids[4]), width=25, height=5)
color4.place(x=630, y=365)
root.mainloop()





















