from PIL import Image,ImageDraw

newimg=Image.new('RGBA',(300,300),"#005000")
drawObj=ImageDraw.Draw(newimg)
for y in range(100,200,3):
    for x in range(100,200,3):
        drawObj.point([(x,y)],fill="Red")

drawObj.line([(3,3),(296,3),(296,296),(3,296),(3,3)])
drawObj.line([(6,6),(293,6),(293,293),(6,293),(6,6)])
drawObj.line([(9,9),(290,9),(290,290),(9,290),(9,9)])

for x in range(150,300,10):
    drawObj.line([(x,0),(300,x-150)],fill="#000000")
    drawObj.line([(300-x,0),(0,x-150)],fill="#000000")
    drawObj.line([(x,300),(300,450-x)],fill="#000000")
    drawObj.line([(300-x,300),(0,450-x)],fill="#000000")

newimg.save("testimg.png")