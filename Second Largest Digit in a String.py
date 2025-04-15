class Solution:
    def secondHighest(self, s: str) -> int:
        elemts=[]
        for i in s:
            if i.isdigit():
                elemts.append(int(i))
        sd=[x for x in elemts if x!=max(elemts) ]
        return -1 if len(sd)==0 else max(sd)
