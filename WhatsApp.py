def ReadFile (Read): #פונקציה לקראית קובץ אשר מקבלת את נתיב הימצאות הקובץ
    file= open(Read, encoding='UTF-8') #פתיחת הקובץ בפורמט המתאים
    file=file.read()#קריאת הקובץ כיחידה אחת 
    return file
    
def WhatsAppChat(myline): #פונקציה המקבלת טקסט התכתבות, ויוצרת רשימת יומנים
    lst=list()
    ID=dict()
    i=1
    j=0
    line=myline.splitlines()
    for myline in line:#לולאה ליצירת מספר מזהה עבור כל טלפון\שם וליצירת ספריה עבור פרטי ההודעה
        start=myline.find("-")
        end=myline.find(":",start+2)
        phone=myline[start+2:end]#מציאת מספר הטלפון.השם לפי סימנים
        if phone and end>0 not in ID:#התאמת מספר מזהה עבור טלפון\שם
            ID[phone]=i
            i=i+1
        if end>0 :
            lst.append(dict())#יצירת מילון עבור כל הודעה
            lst[j]['id']=ID[phone]
            lst[j]['message']= myline[end+1:]
            lst[j]['dateTime']=myline[:start]
            j=j+1
    return(lst) 
    
def DetailsChat (myline):#פונקציה המתארת את פרטי הקבוצה
    detal=dict()
    names=list()
    i=0
    group=0
    line=myline.splitlines()
    for myline in line:
        if i>2 :
            start=myline.find("-")
            end=myline.find(":",start+2)
            name=myline[start+2:end]
            if name not in names:#ספירת מספר הטלפון\שמות בקבוצה
                names.append(name)
                group=group+1
        if i==1:
            start=myline.find("קבוצה")
            end=myline.find("נוצרה")
            num=myline.find("+")
            detal['chat_name']=myline[start+7:end-2]#מציאת שם הקבוצה לפי מיקום
            detal['creator']=myline[num:]#מציאת יוצר הקבוצה לפי מיקום
        if i==2:
            start=myline.find("-")
            end=myline.find(":",start+2)
            detal['creation_date']=myline[:start]
        detal['num_of_participants']=group
        i=i+1
    return detal 
    
    
    
    
    
detal=dict()    
chat=list()
myline=ReadFile('C://Users//Noa Azuz//Desktop//Studies//KnowledgeAndData//ThreeTask//WhatsApp-Birthday.txt')#הפעלת פונקצית קריאת הצאט 
chat= WhatsAppChat(myline)#הפעלת פונקציה היוצרת רשימת מילונים עבור כל הודעה
detal= DetailsChat(myline)#פונקציה היוצרת מילון עם פרטי הקבוצה
whatsapp=dict()#יצירת מילון המחזיק בתוכו את ההודעות ופרטי הקבוצה
whatsapp['metadata']=detal
whatsapp['messages']=chat 
#print(whatsapp) 

import json
mydata=detal['chat_name'] +".txt"
with open(mydata, 'w', encoding='utf8') as mydata:
    json.dump(whatsapp, mydata, ensure_ascii=False)


    
    
