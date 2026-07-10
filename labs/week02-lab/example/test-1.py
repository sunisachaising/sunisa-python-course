print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

#input
r = float(input("Radius: "))

#process
area = 3.14159 * r **2
    #ชื่อตัวแปรไม่ควรเปนตัว x
circumference = 2 * 3.14159 * r

#output
print("Area of this circle= ",area)
print("Circumferenceof this circle =" +str(circumference))
    #ตัวแปรcircumferenceตอนนี้เป็นData type คือ float 
    #เลยเปลี่ยนเป็นstrเพราะกันการพิมเลขมาละเกิดเออเร่อ
print(f"Area = {area}, Circumference = {circumference}")
#จะใช้แบบไหนก็ได้เพื่อเอ้าพุต