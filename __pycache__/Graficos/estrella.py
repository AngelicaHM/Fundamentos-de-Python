from turtle import*

color('red', 'yellow')        #Le da color a las lineas
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill
done


time.sleep(5)