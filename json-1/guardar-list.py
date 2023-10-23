import json 

fd = open("json-1/lista.json" , "w") 


lst = [{"nombre":"Paola" , "edad" :25}, 
       {"nombre":"Carlos" , "edad" :18}, 
       {"nombre":"Juan" , "edad" :18},
       {"nombre":"Mateo" , "edad" :19},
       {"nombre":"Patricia" , "edad" :21}]

json.dump(lst,fd)#Guardamos el archivo que se va a guardar y en donde


fd.close()