
height = input("Введите росты учеников").split()
petya_height = int(input("Введите рост Пети "))
def sortByNumber(inputlist):
        return int(inputlist)
for n in range(len(height)):
    height[n]= int(height[n])
if height[n]<200 and height[n]>0 :
    height.append(petya_height)
    height.sort(key=sortByNumber, reverse=True)
    same_h = height.count(petya_height)
    p_place = height.index(petya_height)+same_h
    print ("Место Пети", p_place)
else:
    print ("Такого роста не бывает!")

print(input("Нажмите Enter для выхода из програмы"))
