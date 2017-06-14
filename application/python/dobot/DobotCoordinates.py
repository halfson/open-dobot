def getZeroPoint(device,station):
    if (device == "Pars" and station == 1):
        #Pars zero points
        x1 = -99.0  # phone 4 x1 position
        x2 = x1 + 122.5  # phone 4 x2 position #real length = 12.1cm
        x4 = x1 + 1.0

        y1 = -263.0  # phone 4 y1 position
        y2 = y1 - 1.7  # y2 = y1 + 68.1  # phone 4 y2 position #real length = 6.8cm
        y4 = y1 + 67.6
        points = [x1,x2,x4],[y1,y2,y4]
        
    elif (device == "Pars" and station == 2):
        #Pars zero points
        x1 = 106.0  # phone 4 x1 position
        x2 = x1 + 124.0  # phone 4 x2 position #real length = 12.1cm
        x4 = x1 + 2.8

        y1 = -205.0  # phone 4 y1 position
        y2 = y1 - 1.5 # y2 = y1 + 68.1  # phone 4 y2 position #real length = 6.8cm
        y4 = y1 + 68.5
        points = [x1,x2,x4],[y1,y2,y4]
        
    elif (device == "Pars" and station == 3):
        #Pars zero points
        x1 = 169.0  # phone 4 x1 position
        x2 = x1 + 123.4  # phone 4 x2 position #real length = 12.1cm
        x4 = x1 + 1.0

        y1 = -26.5  # phone 4 y1 position
        y2 = y1 - 7.7  # y2 = y1 + 68.1  # phone 4 y2 position #real length = 6.8cm
        y4 = y1 + 67.6
        points = [x1,x2,x4],[y1,y2,y4]
        
    elif (device == "Pars" and station == 4):
        #Pars zero points
        x1 = 108.5  # phone 4 x1 position
        x2 = x1 + 123.4  # phone 4 x2 position #real length = 12.1cm
        x4 = x1 + 1.0

        y1 = 133.0  # phone 4 y1 position
        y2 = y1 - 2.7  # y2 = y1 + 68.1  # phone 4 y2 position #real length = 6.8cm
        y4 = y1 + 67.6
        points = [x1,x2,x4],[y1,y2,y4]
        
    elif (device == "Pars" and station == 5):
        #Pars zero points
        x1 = -95.0  # phone 4 x1 position
        x2 = x1 + 123.4  # phone 4 x2 position #real length = 12.1cm
        x4 = x1

        y1 = 196.0  # phone 4 y1 position
        y2 = y1 + 3.5 # y2 = y1 + 68.1  # phone 4 y2 position #real length = 6.8cm
        y4 = y1 + 67.6
        points = [x1,x2,x4],[y1,y2,y4]
        
    elif (device == "Orca" and station == 4):
        #  ORCA zero points
        x1 = 88.5  # phone 4 x1 position
        x2 = x1 + 123.3  # phone 4 x2 position #real length = 12.1cm
        x4 = x1 + 1.1

        y1 = 133.0  # phone 4 y1 position
        y2 = y1 - 2.7  # y2 = y1 + 68.1  # phone 4 y2 position #real length = 6.8cm
        y4 = y1 + 67.7
        points = [x1,x2,x4],[y1,y2,y4]  
    else:
        print "There is no saved coordinates for this Phone!!!!"
    
    return points
        