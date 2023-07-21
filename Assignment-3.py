def SumTuples(a:(),b:())->():
  return tuple((a[x]+b[x]  for x in range(max(len(b),len(a))) if x<len(a) and x<len(b)))
def ImportJSON(JSON:str)->dict:
 return{x[:x.find(":")].replace('{',''):x[x.find(":")+1:].replace('}','') for x in JSON.split(',')}
  
def  ExportJSON(dicts:dict):
    stri="{"
    for key,value in dicts.items():
      if not list(dicts.keys()).index(key)==len(list(dicts.keys())):
        stri+=f"{key}:"+f"{value},"
      else:
        stri+=f"{key}:"+f"{value}"
    stri+="}"
    return stri

   
"""
Just other ideas ;)
def  importJSON(dicts:dict):
  return str(dicts)
def Export_JSON(JSON:str)->dict:
  list=JSON.split(', ')
  print(list)
  dc={}
  for x in list:
    key=x[:x.find(":")].replace('{','')
    value=x[x.find(":")+1:].replace('}','')
    if value[0]=='[':
      dc.update({key.replace('[',''):value.replace('[','').replace(']','').split(',')})
    elif value[0]=='{':
      dc.update({key:Export_JSON(value)})
    else:  
     dc.update({key:value for x in JSON.split(',')})
  return dc
"""
def main():
  input_=int(input('please choose your option\n1. Sum Tuples\n2. Export JSON\n3. Import JSON\n4. Exit\n:'))
  if input_==4:
    print('good night')
  elif input_==1:
    print("Tuple one")
    t1=tuple([int(input('input a number: ')) for x in range(int(input('Enter the first tuple size: ')))])
    print("Tuple Tne")
    t2=tuple([int(input('input a number: ')) for x in range(int(input('Enter the Second tuple size: ')))])
    print(SumTuples(t1,t2))
    main()
  elif input_==2:
   
    print(ExportJSON({input('Input key: '):('Input value: ') for _ in range(int(input('Enter the dictionary size: ')))}))
    main()
  elif input_==3:
     print(ImportJSON(input("Enter the JSON Object :")))
     main()
      
main()