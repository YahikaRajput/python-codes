import pandas as pd
#create a list
list1 = [100, 200, 300, 400, 500]
#create a series from the list
series = pd.Series(list1)
print(series)
# display third value in the series
print(series[2])
li = [1, 3, 5]
# create a series and specify labels
series1 = pd.Series(li, index = ["x", "y", "z"])
print(series1)
print(series1["y"]) 
 

# import pandas as pd
#create a two-dimensional list 
datal = [ ['AAA' , 25 , 'Pune'] , ['BBB' , 30 , 'Mumbai'] , ['CCC' , 35 , 'Nasik']]
#create a DataFrame from the list 
df = pd.DataFrame(datal , columns= ['Name' , 'Age' , 'City'])
print(df) 


# import pandas as pd 
datal = [ [1 , 'yashika' , 'BCA' , 8262006430] , [2 , 'Betu' , 'BCA' , 5789357200] ,
         [3 , 'Shourya' , 'BCA' , 5012697450] , [4 , 'Pari' , 'BCA' , 5012978403] ,
         [5 , 'Suriya' , 'BCA' , 3287451329]
          ]
df = pd.DataFrame(datal ,columns= ['Roll_No' , 'Stud_Name' , 'Class' , 'Phone_No'])
print(df)