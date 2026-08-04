class Student():
    def studDetails(self, n, a, p, c, m):
        self.name = n 
        self.age = a 
        self.phy = p 
        self.che = c 
        self.maths = m 
        print("Name = ",self.name)
        print("Age = ",self.age)
        print("Phy = ",self.phy)
        print("Che = ",self.che)
        print("Maths = ",self.maths,"\n")
s1 = Student()
s2 = Student()
s3 = Student()

s1.studDetails("Anjaly", 23, 76, 45, 65)
s2.studDetails("arun", 24, 65, 47, 86)
s3.studDetails("reshma", 23, 62, 57, 66)

print("\n\nphySum = ",s1.phy + s2.phy)
print("chemSum = ",s2.che+s3.che)