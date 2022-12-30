from fastapi import FastAPI, HTTPException, status
from typing import Optional
from itertools import product
from pydantic import BaseModel


dictgen = FastAPI()

class Info(BaseModel):
    info1: str
    info2: Optional[str]=None
    info3: Optional[str]=None


@dictgen.get('/dictgen/')
def datainp(info: Info)->dict:    
    if not info:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, 
            detail="You must provide words to generate the dictionay."
        )
    
    #some useful carachterers
    aux=['!','@','#','$','%','&','[',']','{','}','~','^','/',':',';','|','=','-','_','*','+',"'",'"']  
    tmplst=[]
    tmp=[]
    lst=[]

    for inf in info:
        if inf[1]==None:
            continue
        else:
            lst.append(inf[1])


    #capital letters variant producer
    for word in lst:
        tmp=list(word)
        for c in range(len(tmp)):
            tmp[c] = tmp[c].upper()
            word = ''.join(tmp)
            word = word.strip()
            tmplst.append(word)
            tmp[c] = tmp[c].lower()
  
    # generating the cartesian products
    infoAuxList=list(product(tmplst, aux, repeat=1))
    auxInfoList=list(product(aux, tmplst, repeat=1))
    auxInfoAuxList=list(product(aux, tmplst, aux, repeat=1))
    InfoAuxInfoList=list(product(tmplst, aux, tmplst, repeat=1))
    auxInfoCList=list(product(aux, tmplst, tmplst, repeat=1))     
    infoCAuxList=list(product(tmplst, tmplst, aux, repeat=1))    
    InfoAuxAuxInfoList=list(product(tmplst, aux, aux,tmplst, repeat=1))
    auxInfoCAuxList=list(product(aux, tmplst, tmplst, aux, repeat=1))
    auxInfoAuxInfoList=list(product(aux, tmplst, aux, tmplst, repeat=1))
    InfoAuxInfoAuxList=list(product(tmplst, aux, tmplst, aux, repeat=1))
    
    sampleList=[infoAuxList, 
        auxInfoList, 
        auxInfoAuxList, 
        InfoAuxInfoList,
        InfoAuxAuxInfoList,
        infoCAuxList, 
        auxInfoCList, 
        auxInfoCAuxList,
        auxInfoAuxInfoList,
        InfoAuxInfoAuxList
        ]

    # generating the passwords
    for colection in sampleList:
        for tupl in colection:
            psswrd = ''.join(tupl)
            tmplst.append(psswrd)   

    return {'generated_passwords': tmplst}

 

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:dictgen", host="0.0.0.0", port=8000, reload=True)