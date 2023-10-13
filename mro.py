class A:
    def method(self):
        return "A"
class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    def method(self):
        return "D"  
    
d = D()
print(d.method())

print(D.mro())