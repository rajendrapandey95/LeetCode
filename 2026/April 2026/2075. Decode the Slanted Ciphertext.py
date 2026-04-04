class Solution:
    def decodeCiphertext(self, s, r):
        if not s: return s
        c=(len(s)+r-1)//r
        res=[]

        for j in range(c):
            i,k=0,j
            while i<r and k<c:
                res.append(s[i*c+k])
                i+=1; k+=1

        return "".join(res).rstrip()
