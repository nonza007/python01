tuplefruits = ("apple","banana","cherry") #tuple
listfruits = ["apple","banana","cherry"] #list
print(tuplefruits[1:])
print(listfruits)
#เปลี่ยนค่าในtuple
x=list(tuplefruits)#แปลงเป็นlistแล้วเก็บในตัวแปรx
x[1]="blueberry"
tuplefruits=tuple(x)
print("เปลี่ยนค่าtuple:",tuplefruits)
#เพิ่มค่าในtuple
x=list(tuplefruits)
x.append("melon")
tuplefruits=tuple(x)
print("เพิ่มค่าtuple:",tuplefruits)
#ลบtuple
x=list(tuplefruits)
x.remove("cherry")
tuplefruits = tuple(x)
print("เพิ่มค่าtuple:",tuplefruits)
#join tuple
vege=("tomato","cucumber","onion")
fruitsvege=tuplefruits+vege
print("join tuple:",fruitsvege)
x = range(3, 6)#จะหยุดก่อนค่าstop
for n in x:
    print("range x:",n)
y = range(3,20,2)
for m in y:
    print("range x:",m)
#ชื่อ นาย ภูรีทัศ น้อยบัวงาม เลขที่9 ม6-11