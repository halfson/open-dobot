class Phone:
    def __init__(self,device,station):
        self.device = device
        self.station = station
        #Resolution and up
        Phone.U= 80.0
        if device == "Pars" or "Leo":
            Phone.h = 1280.0
            Phone.w = 720.0   
        elif device == "Orca" or "Reys":
            Phone.h = 1920.0
            Phone.w = 1080.0
        else: 
            print "This phone has not implemented yet"

        #down     
        if device == "Pars" or "Leo":
            Phone.d = 53.0
        elif device == "Orca" or "Reys":
            Phone.d = 55.0   
        else: 
            print "This phone has not implemented yet"
                       
        if (device == "Pars" and station == 1):
            #Pars zero points
            Phone.x_1 = -99.0  # phone 4 Phone.x_1 position
            Phone.x_2 = Phone.x_1 + 122.5  # phone 4 Phone.x_2 position #real length = 12.1cm
            Phone.x_4 = Phone.x_1 + 1.0   
            Phone.y_1 = -263.0  # phone 4 Phone.y_1 position
            Phone.y_2 = Phone.y_1 - 1.7  # Phone.y_2 = Phone.y_1 + 68.1  # phone 4 Phone.y_2 position #real length = 6.8cm
            Phone.y_4 = Phone.y_1 + 67.6          
        elif (device == "Pars" and station == 2):
            #Pars zero points
            Phone.x_1 = 106.0  # phone 4 Phone.x_1 position
            Phone.x_2 = Phone.x_1 + 124.0  # phone 4 Phone.x_2 position #real length = 12.1cm
            Phone.x_4 = Phone.x_1 + 2.8   
            Phone.y_1 = -205.0  # phone 4 Phone.y_1 position
            Phone.y_2 = Phone.y_1 - 1.5 # Phone.y_2 = Phone.y_1 + 68.1  # phone 4 Phone.y_2 position #real length = 6.8cm
            Phone.y_4 = Phone.y_1 + 68.5            
        elif (device == "Pars" and station == 3):
            #Pars zero points
            Phone.x_1 = 169.0  # phone 4 Phone.x_1 position
            Phone.x_2 = Phone.x_1 + 123.4  # phone 4 Phone.x_2 position #real length = 12.1cm
            Phone.x_4 = Phone.x_1 + 1.0    
            Phone.y_1 = -26.5  # phone 4 Phone.y_1 position
            Phone.y_2 = Phone.y_1 - 7.7  # Phone.y_2 = Phone.y_1 + 68.1  # phone 4 Phone.y_2 position #real length = 6.8cm
            Phone.y_4 = Phone.y_1 + 67.6           
        elif (device == "Pars" and station == 4):
            #Pars zero points
            Phone.x_1 = 108.5  # phone 4 Phone.x_1 position
            Phone.x_2 = Phone.x_1 + 123.4  # phone 4 Phone.x_2 position #real length = 12.1cm
            Phone.x_4 = Phone.x_1 + 1.0    
            Phone.y_1 = 133.0  # phone 4 Phone.y_1 position
            Phone.y_2 = Phone.y_1 - 2.7  # Phone.y_2 = Phone.y_1 + 68.1  # phone 4 Phone.y_2 position #real length = 6.8cm
            Phone.y_4 = Phone.y_1 + 67.6           
        elif (device == "Pars" and station == 5):
            #Pars zero points
            Phone.x_1 = -95.0  # phone 4 Phone.x_1 position
            Phone.x_2 = Phone.x_1 + 123.4  # phone 4 Phone.x_2 position #real length = 12.1cm
            Phone.x_4 = Phone.x_1    
            Phone.y_1 = 196.0  # phone 4 Phone.y_1 position
            Phone.y_2 = Phone.y_1 + 3.5 # Phone.y_2 = Phone.y_1 + 68.1  # phone 4 Phone.y_2 position #real length = 6.8cm
            Phone.y_4 = Phone.y_1 + 67.6           
        elif (device == "Orca" and station == 4):
            #  ORCA zero points
            Phone.x_1 = 88.5  # phone 4 Phone.x_1 position
            Phone.x_2 = Phone.x_1 + 123.3  # phone 4 Phone.x_2 position #real length = 12.1cm
            Phone.x_4 = Phone.x_1 + 1.1    
            Phone.y_1 = 133.0  # phone 4 Phone.y_1 position
            Phone.y_2 = Phone.y_1 - 2.7  # Phone.y_2 = Phone.y_1 + 68.1  # phone 4 Phone.y_2 position #real length = 6.8cm
            Phone.y_4 = Phone.y_1 + 67.7            
        else:
            print "There is no saved coordinates for this Phone!!!!"
 
    def x1(self):
        return Phone.x_1
    def x2(self):
        return Phone.x_2
    def x4(self):
        return Phone.x_4
    def y1(self):
        return Phone.y_1
    def y2(self):
        return Phone.y_2
    def y4(self):
        return Phone.y_4                         
    def height(self):
        return Phone.h
    def width(self):
        return Phone.w
    def down(self):
        return Phone.d
    def up(self):
        return Phone.d + 3.0
    def Uup(self):
        return Phone.U


        
        
    
    
    #===========================================================================
    # def getProperties(self):
    #     if self.device == "Pars" or "Leo":
    #         Phone.height = 1280.0
    # #===========================================================================
    # #         width = 720.0
    # #         print height
    # #     elif self.device == "Orca" or "Reys":
    # #         height = 1920.0
    # #         width = 1080.0    
    #     else:
    #          print "this device configuration doesn't exist"
    #           
    # def height(self):
    #     return self.height
    # #     
    # #     
    # #     if self.device == "Pars" or "Leo":
    # #         down = 50.3
    # #     else:
    # #         print "this device configuration doesn't exist"
    # #     up = down + 3.0
    # #     
    # # def doSomething(self):
    # #     print "asdasda"
    # #     print self.device    
    # #===========================================================================
    # Phone("Pars").height()
    #===========================================================================