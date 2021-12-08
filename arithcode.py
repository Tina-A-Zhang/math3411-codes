start={"a":0.0,"b":0.7,".":0.9}
leng={"a":0.7,"b":0.2,".":0.1}
def encode():
    pt=list("bab.")

    last_len=1
    code=0.0
    for i in pt:
        code = code+last_len*start[i]
        last_len=leng[i]*last_len

    print("Code range: "+str(code)+"-"+str(code+last_len))

def inrange(i,s,e):
    if i >=s and i <e:
        return True
    else:
        return False

def decode():
    pt=[]
    code=0.8246
    while len(pt)==0 or pt[-1] != ".":
        for key,value in start.items():
            if inrange(code,start[key],start[key]+leng[key]):
                pt.append(key)
                code=(code-start[key])/leng[key]
    print(pt)

encode()
# decode()
    
