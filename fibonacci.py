class fibonacci:
    #start_num=int(input("Enter Starting Number"))
    #end_num=int(input("Enter Ending Number"))
    
    def fibo(self):
        intial_value =0
        second_value=1
        third_value=0
        for i in range(1,10):
            third_value=intial_value+second_value
            print("intial value " ,third_value)
            #print("second_value" ,second_value)
            intial_value=second_value
            second_value =third_value
            
f=fibonacci()            
f.fibo()

        
    
                    
                       
                   
                   
