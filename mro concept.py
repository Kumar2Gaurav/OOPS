class A:pass
class B(A):pass
class C(A):pass
class D(B,C):pass
print(D.mro())
print(B.mro())
print(C.mro())
print(A.mro())