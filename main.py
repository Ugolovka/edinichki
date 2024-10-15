input_data = open("input.txt","r")
data = input_data.read()
a = int(data)
sum = 0
while a != 1:
    if a % 2==1:
        sum +=1
output_data = open("output.txt","w")
output_data.write(str(sum))
input_data.close()
output_data.close()