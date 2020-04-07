Number=int(input("\n please enter the range number:"))
i=0
First_value=0
Second_value=1
while(i<Number):
      if(i<=1):
          Next=1
      else:
          Next=First_value+Second_value
          First_value=Second_value
          Second_value=Next
      print(Next)
      i=i+1
