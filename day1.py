in_file = open("day1_in.txt","r")
count = 0
input_lines = in_file.readlines()
#print(input_lines)
calorie_per_elf = []
temp_calorie = 0
for i in range(len(input_lines)):
    if input_lines[i] != '\n':
        temp_calorie = temp_calorie + int(input_lines[i].strip())
        #print(temp_calorie)
    elif input_lines[i] == '\n':
        calorie_per_elf.append(temp_calorie)
        count = count+1
        temp_calorie = 0
#print(count)
#print(temp_calorie)
print(calorie_per_elf)
sort_calorie_per_elf = sorted(calorie_per_elf)
print(max(calorie_per_elf))
#print("sorted calorie wise "+sorted(calorie_per_elf))
print(sort_calorie_per_elf[count-1]+sort_calorie_per_elf[count-2]+sort_calorie_per_elf[count-3])