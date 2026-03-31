class Solution:
    def generateString(self, a, b):
        n,m=len(a),len(b)
        s=['a']*(n+m-1)
        f=[0]*(n+m-1)

        # T case
        for i,c in enumerate(a):
            if c=='T':
                for j,x in enumerate(b,i):
                    if f[j] and s[j]!=x: return ""
                    s[j],f[j]=x,1

        # F case
        for i,c in enumerate(a):
            if c=='F':
                if any(s[j]==b[j-i] for j in range(i,i+m)) and \
                   all(s[j]==b[j-i] for j in range(i,i+m)):
                    for j in range(i+m-1,i-1,-1):
                        if not f[j]:
                            s[j]='b'
                            break
                    else: return ""

        return "".join(s)
