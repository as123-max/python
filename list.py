class List:
    def __init__(self,a):
        self.a=a
    def __mul__(self,other):
        out=[]
        if len(self.a)>len(other.a):
            b=self.a
            c=other.a
        else:
            b=other.a
            c=other.b
        for i in range(len(b)):
            if i<len(c):
                for j in range(i,i+1):
                    out.append(b[i]*c[j])
            else:
                out.append(b[i])
        return out
o1=List([1,2,3])
o2=List([2,3])
print(o1*o2)
    
