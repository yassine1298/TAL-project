from tkinter import *
from tkinter import filedialog
from lxml import etree
from tkinter import ttk
import xml.etree.cElementTree as ET
import docx2txt
import tkinter as tk
from tkinter import scrolledtext
from striprtf.striprtf import rtf_to_text
from tkinter.messagebox import *
import os

def transliteration():
    mytext = ENT.get(1.0, END)
    mylist = []
    value0 = comboExample1.get()
    value1 = comboExample2.get()
    if ( value0 == "Latin" and value1 == "Arabe") :
           Lien = "Latin_Arabe/A{}/text()"
           tree = etree.parse("latin_arabe.xml")
    elif  ( value0 == "Arabe" and value1 == "Amazigh"): 
           Lien = "Arabe_Amazigh/A{}/text()"
           tree = etree.parse("arabe_amazigh.xml")
    elif  ( value0 == "Latin" and value1 == "Amazigh"): 
           Lien = "Latin_Amazigh/A{}/text()"
           tree = etree.parse("latin_amazigh.xml")
    elif  ( value0 == "Arabe" and value1 == "Latin"):
           Lien = "Arabe_Latin/A{}/text()"
           tree = etree.parse("arabe_latin.xml")
    elif  ( value0 == "Amazigh" and value1 == "Arabe"):
           Lien = "Amazigh_Arabe/A{}/text()"
           tree = etree.parse("amazigh_arabe.xml")
    elif  ( value0 == "Amazigh" and value1 == "Latin"):
           Lien = "Amazigh_Latin/A{}/text()"
           tree = etree.parse("amazigh_latin.xml")
    elif (value0 == S and value1 == C ):
           Lien = "Source_Cible/A{}/text()"
           tree = etree.parse("New_data.xml")

    comp=0
    for elm in tree.findall(".//"):
        comp = comp+1
    print(comp)
    for i in range(int((comp)/2)):
        mlist = tree.xpath(Lien.format(i))
        mylist.append(mlist)
    print(mylist)

    for k, v in mylist:
        mytext = mytext.replace(k, v)
    output.insert(END,mytext)




    

#fonctions
#creation de la fonction qui permet de quitter l'interface 
def clo():
    s.destroy()
    exit()
#creation de la fonction correspondante au bouton reintialiser et qui permet de vider les champs d'ecriture afin d'utiliser un nouveau mot 
def effacer():
    #effacer le texte saisi ou importé
    ENT.delete(0.0,END)
    #effacer le texte de resultat 
    output.delete(0.0,END)
#fonctions pour enregistrer en fichier xml les informations mot/ stem/ frequence (ns) 
def ENr():
    SaP(ns)
#fonction pour enregistrer un texte dans un fichier sous la forme xml 


#fonction pour enregistrer le texte apres stemming dans un fichier sous la forme txt
def ENR2():
    ml=output.get(0.0,END)
    #recupere le nom et l'emplacement où on veut enregistrer le fichier avec extension par defaut txt pour que l'utilisateur n'aura pas à modifier l'extension 
    id1=filedialog.asksaveasfile(mode='w',title="Enregistrer sous … un fichier",filetypes=(("Text files", "*.txt"),("All files", "*.*")),defaultextension=".TXT")
    #ecrire le texte 'texto' dans le fichier initialiser avec ml est le resultat du stemming (texte apres)  
    id1.write(ml)
    
    #fermer le fichier 
    id1.close()


#fonction pour ouvrir  un texte depuis  un fichier Word         
def ouvrirWord():
    
    #parcourir pour chercgeret choisir un fichier word et rezcupere son nom (avec son chemin)
    s.fileName= filedialog.askopenfilename(filetypes=(("Document Microsoft Word","*.docx"),("All files", "*.*")),defaultextension=".DOCX")
   #affecter le nom au variable l 
    l=s.fileName
    #afin de lire le fichier Word on doit le convertir en texte en utilisant la fonction Docx2txt 
    #lire le texte et l'affecter à la variable gu 
    gus= docx2txt.process(l)
    #inserer le texte recupéré dans le champ convenable 
    #ENT.insert(END,gu)
    #y1=gu
    #effacer le champ pour etre sr que nous n'aurons pas 2 texte à la fois 
    #ENT.delete(0.0, END)
    #ENT.insert(END,'\n')
    #lire le fichier et affecter le texte recupéré dans la variable gu 
    gt=gus
    gt=gt
      #effacer le champ pour etre sr que nous n'aurons pas 2 texte à la fois 
    ENT.delete(0.0, END)
        #inserer le texte recupéré dans le champ convenable 
    ENT.insert(END,gt)
    ENT.insert(END,'\n')
    

#fonction pour ouvrir  un texte depuis  un fichier texte .txt
def ouvrirTexte():
      #parcourir pour chercher et choisir un fichier texte .txt et recuperer son nom (avec son chemin bien sur)
    s.fileName= filedialog.askopenfilename(filetypes=(("Texte","*.txt"),("All files", "*.*")),defaultextension=".TXT")
    #recupere le nom du fichier dans la variable l
    l=s.fileName
    
    
    #rtf = "some rtf encoded string"
    #ouvrir le fichier en mode lecture 
    do= open(l,"r",encoding='utf-8')
    #lire le fichier et affecter le texte recupéré dans la variable gu 
    gu=do.read()
    gu=gu
      #effacer le champ pour etre sr que nous n'aurons pas 2 texte à la fois 
    ENT.delete(0.0, END)
        #inserer le texte recupéré dans le champ convenable 
    ENT.insert(END,gu)
    ENT.insert(END,'\n')
    

#fonction pour ouvrir  un texte depuis  un fichier RTF.rtf
def ouvrirRTF():
    s.fileName= filedialog.askopenfilename(filetypes=(("RTF","*.rtf"),("All files", "*.*")),defaultextension=".RTF")
    l=s.fileName
    
    #rtf = "some rtf encoded string"
    
    gus=l
    gt=gus
      #effacer le champ pour etre sr que nous n'aurons pas 2 texte à la fois 
    ENT.delete(0.0, END)
        #inserer le texte recupéré dans le champ convenable 
    ENT.insert(END,gt)
    ENT.insert(END,'\n')

def importation():
#     print(folder_selected)
    folder_selected = filedialog.askdirectory()
    data_path = folder_selected
    data_dir_list = os.listdir(data_path)

    names=[]
    for dataset in data_dir_list:
        names.append(dataset)
    #print(names)
    Files2=[]
    for file in data_dir_list:
        with open(data_path+'/'+ file,  "r",encoding='utf-8', errors='ignore') as fileToRead:
            fileToRead=fileToRead.read()

        Files2.append(fileToRead)
 

    # print(Files2)
    for i in range(len(data_dir_list)):
        ENT.insert(END,Files2[i])
        ENT.insert(END,'\n')


def confg():
    def configuration():  
        root = ET.Element("Langague")
        doc = ET.SubElement(root, "Source_Cible")
    

    
        value2= E2.get(1.0)
        value3= E3.get(1.0)
        value4= E4.get(1.0)
        value5= E5.get(1.0)
        value6= E6.get(1.0)
        value7= E7.get(1.0)
        value8= E8.get(1.0)
        value9= E9.get(1.0)
        value10= E10.get(1.0)
        value11= E11.get(1.0)
        value12= E12.get(1.0)
        value13= E13.get(1.0)
        value14= E14.get(1.0)
        value15= E15.get(1.0)
        value16= E16.get(1.0)
        value17= E17.get(1.0)
        value18= E18.get(1.0)
        value19= E19.get(1.0)
        value20= E20.get(1.0)
        value21= E21.get(1.0)
        value22= E22.get(1.0)
        value23= E23.get(1.0)
        value24= E24.get(1.0)
        value25= E25.get(1.0)
        value26= E26.get(1.0)
        value27= E27.get(1.0)
        #value28= E28.get(1.0)
        #value29= E29.get(1.0)
        #value30= E30.get(1.0)
        #value31= E31.get(1.0)
        #value32= E32.get(1.0)
        #value33= E33.get(1.0)
        #value34= E34.get(1.0)
        #value35= E35.get(1.0)
        #value36= E36.get(1.0)
        #value37= E37.get(1.0)
        #value38= E38.get(1.0)
        #value39= E39.get(1.0)
        #value40= E40.get(1.0)
        #value41= E41.get(1.0)
        #value42= E42.get(1.0)
        #value43= E43.get(1.0)
        #value44= E44.get(1.0)
        #value45= E45.get(1.0)
        #value46= E46.get(1.0)
    
    
        value02= E_02.get(1.0)
        value03= E_03.get(1.0)
        value04= E_04.get(1.0)
        value05= E_05.get(1.0)
        value06= E_06.get(1.0)
        value07= E_07.get(1.0)
        value08= E_08.get(1.0)
        value09= E_09.get(1.0)
        value010= E_010.get(1.0)
        value011= E_011.get(1.0)
        value012= E_012.get(1.0)
        value013= E_013.get(1.0)
        value014= E_014.get(1.0)
        value015= E_015.get(1.0)
        value016= E_016.get(1.0)
        value017= E_017.get(1.0)
        value018= E_018.get(1.0)
        value019= E_019.get(1.0)
        value020= E_020.get(1.0)
        value021= E_021.get(1.0)
        value022= E_022.get(1.0)
        value023= E_023.get(1.0)
        value024= E_024.get(1.0)
        value025= E_025.get(1.0)
        value026= E_026.get(1.0)
        value027= E_027.get(1.0)
        #value028= E_028.get(1.0)
        #value029= E_029.get(1.0)
        #value030= E_030.get(1.0)
        #value031= E_031.get(1.0)
        #value032= E_032.get(1.0)
        #value033= E_033.get(1.0)
        #value034= E_034.get(1.0)
        #value035= E_035.get(1.0)
        #value036= E_036.get(1.0)
        #value037= E_037.get(1.0)
        #value038= E_038.get(1.0)
        #value039= E_039.get(1.0)
        #value040= E_040.get(1.0)
        #value041= E_041.get(1.0)
        #value042= E_042.get(1.0)
        #value043= E_043.get(1.0)
        #value044= E_044.get(1.0)
        #value045= E_045.get(1.0)
        #value046= E_046.get(1.0)
    

        ET.SubElement(doc,"A0").text = value2
        ET.SubElement(doc,"A1").text = value3
        ET.SubElement(doc,"A2").text = value4
        ET.SubElement(doc,"A3").text = value5
        ET.SubElement(doc,"A4").text = value6
        ET.SubElement(doc,"A5").text = value7
        ET.SubElement(doc,"A6").text = value8
        ET.SubElement(doc,"A7").text = value9
        ET.SubElement(doc,"A8").text = value10
        ET.SubElement(doc,"A9").text = value11
        ET.SubElement(doc,"A10").text = value12
        ET.SubElement(doc,"A11").text = value13
        ET.SubElement(doc,"A12").text = value14
        ET.SubElement(doc,"A13").text = value15
        ET.SubElement(doc,"A14").text = value16
        ET.SubElement(doc,"A15").text = value17
        ET.SubElement(doc,"A16").text = value18
        ET.SubElement(doc,"A17").text = value19
        ET.SubElement(doc,"A18").text = value20
        ET.SubElement(doc,"A19").text = value21
        ET.SubElement(doc,"A20").text = value22
        ET.SubElement(doc,"A21").text = value23
        ET.SubElement(doc,"A22").text = value24
        ET.SubElement(doc,"A23").text = value25
        ET.SubElement(doc,"A24").text = value26
        ET.SubElement(doc,"A25").text = value27
       # ET.SubElement(doc,"A26").text = value28
        #ET.SubElement(doc,"A27").text = value29
        #ET.SubElement(doc,"A28").text = value30
        #ET.SubElement(doc,"A29").text = value31
        #ET.SubElement(doc,"A30").text = value32
        #ET.SubElement(doc,"A31").text = value33
        #ET.SubElement(doc,"A32").text = value34
        #ET.SubElement(doc,"A33").text = value35
        #ET.SubElement(doc,"A34").text = value36
        #ET.SubElement(doc,"A35").text = value37
        #ET.SubElement(doc,"A36").text = value38
        #ET.SubElement(doc,"A37").text = value39
        #ET.SubElement(doc,"A38").text = value40
        #ET.SubElement(doc,"A39").text = value41
        #ET.SubElement(doc,"A40").text = value42
        #ET.SubElement(doc,"A41").text = value43
        #ET.SubElement(doc,"A42").text = value44
        #ET.SubElement(doc,"A43").text = value45
        #ET.SubElement(doc,"A44").text = value46


        ET.SubElement(doc,"A0").text = value02
        ET.SubElement(doc,"A1").text = value03
        ET.SubElement(doc,"A2").text = value04
        ET.SubElement(doc,"A3").text = value05
        ET.SubElement(doc,"A4").text = value06
        ET.SubElement(doc,"A5").text = value07
        ET.SubElement(doc,"A6").text = value08
        ET.SubElement(doc,"A7").text = value09
        ET.SubElement(doc,"A8").text = value010
        ET.SubElement(doc,"A9").text = value011
        ET.SubElement(doc,"A10").text = value012
        ET.SubElement(doc,"A11").text = value013
        ET.SubElement(doc,"A12").text = value014
        ET.SubElement(doc,"A13").text = value015
        ET.SubElement(doc,"A14").text = value016
        ET.SubElement(doc,"A15").text = value017
        ET.SubElement(doc,"A16").text = value018
        ET.SubElement(doc,"A17").text = value019
        ET.SubElement(doc,"A18").text = value020
        ET.SubElement(doc,"A19").text = value021
        ET.SubElement(doc,"A20").text = value022
        ET.SubElement(doc,"A21").text = value023
        ET.SubElement(doc,"A22").text = value024
        ET.SubElement(doc,"A23").text = value025
        ET.SubElement(doc,"A24").text = value026
        ET.SubElement(doc,"A25").text = value027
        #ET.SubElement(doc,"A26").text = value028
        #ET.SubElement(doc,"A27").text = value029
        #ET.SubElement(doc,"A28").text = value030
        #ET.SubElement(doc,"A29").text = value031
        #ET.SubElement(doc,"A30").text = value032
        #ET.SubElement(doc,"A31").text = value033
        #ET.SubElement(doc,"A32").text = value034
        #ET.SubElement(doc,"A33").text = value035
        #ET.SubElement(doc,"A34").text = value036
       # ET.SubElement(doc,"A35").text = value037
       # ET.SubElement(doc,"A36").text = value038
        #ET.SubElement(doc,"A37").text = value039
        #ET.SubElement(doc,"A38").text = value040
        #ET.SubElement(doc,"A39").text = value041
        #ET.SubElement(doc,"A40").text = value042
        #ET.SubElement(doc,"A41").text = value043
        #ET.SubElement(doc,"A42").text = value044
        #ET.SubElement(doc,"A43").text = value045
        #ET.SubElement(doc,"A44").text = value046
    
        tree = ET.ElementTree(root)
        tree.write("New_data.xml")
        
        text_S = open("Source.txt", "w")
        text_S.write(ES.get(0.0,END))
        text_S.close()
 
        text_C = open("Cible.txt", "w")
        text_C.write(EC.get(0.0,END))
        text_C.close()
        
    n= Toplevel()
    n.title('CONFIGURATION')
    n.geometry("500x1200")
    n.minsize(500,1200)
    n.maxsize(500,1200)
    n.config(background='#ff9a8d')
    # definir une image pour comme logo
    n.iconbitmap("MIT.ico")
    lb= LabelFrame(n ,text="Configurer le nom de la langue",width="260",height="92",bg='#ff9a8d',fg='#000000',font=("Times New Roman", 11))
    lb.place(x=210, y=62)

    ES=Text(n,width=10, height=1.5,bg='#EFF8FB')
    ES.place(x=220,y=108)
    

    t1=Label(n,text = "Vers",font=("Agency FB", 16),bg='#ff9a8d')
    t1.place(x=320, y=108)

    t1=Label(n,text = "Source",font=("Agency FB", 13),bg='#ff9a8d')
    t1.place(x=240, y=80)

    t1=Label(n,text = "Cible",font=("Agency FB", 13),bg='#ff9a8d')
    t1.place(x=400, y=80)


    EC=Text(n,width=10, height=1.5,bg='#EFF8FB')
    EC.place(x=370,y=108)
    

    label1 = tk.Label(n,text = "Langue Cible",font=("Times New Roman", 11),bg='#ff9a8d')
    label1.place(x=120,y=10)

    E2=Text(n,width=2, height=1,bg='#EFF8FB')
    E2.place(x=40,y=30)
    E3=Text(n,width=2, height=1,bg='#EFF8FB')
    E3.place(x=40,y=60)
    E4=Text(n,width=2, height=1,bg='#EFF8FB')
    E4.place(x=40,y=90)
    E5=Text(n,width=2, height=1,bg='#EFF8FB')
    E5.place(x=40,y=120)
    E6=Text(n,width=2, height=1,bg='#EFF8FB')
    E6.place(x=40,y=150)
    E7=Text(n,width=2, height=1,bg='#EFF8FB')
    E7.place(x=40,y=180)
    E8=Text(n,width=2, height=1,bg='#EFF8FB')
    E8.place(x=40,y=210)
    E9=Text(n,width=2, height=1,bg='#EFF8FB')
    E9.place(x=40,y=240)
    E10=Text(n,width=2, height=1,bg='#EFF8FB')
    E10.place(x=40,y=270)
    E11=Text(n,width=2, height=1,bg='#EFF8FB')
    E11.place(x=40,y=300)
    E12=Text(n,width=2, height=1,bg='#EFF8FB')
    E12.place(x=40,y=330)
    E13=Text(n,width=2, height=1,bg='#EFF8FB')
    E13.place(x=40,y=360)
    E14=Text(n,width=2, height=1,bg='#EFF8FB')
    E14.place(x=40,y=390)
    E15=Text(n,width=2, height=1,bg='#EFF8FB')
    E15.place(x=40,y=420)
    E16=Text(n,width=2, height=1,bg='#EFF8FB')
    E16.place(x=40,y=450)
    E17=Text(n,width=2, height=1,bg='#EFF8FB')
    E17.place(x=40,y=480)
    E18=Text(n,width=2, height=1,bg='#EFF8FB')
    E18.place(x=40,y=510)
    E19=Text(n,width=2, height=1,bg='#EFF8FB')
    E19.place(x=40,y=540)
    E20=Text(n,width=2, height=1,bg='#EFF8FB')
    E20.place(x=40,y=570)
    E21=Text(n,width=2, height=1,bg='#EFF8FB')
    E21.place(x=40,y=600)
    E22=Text(n,width=2, height=1,bg='#EFF8FB')
    E22.place(x=40,y=630)
    E23=Text(n,width=2, height=1,bg='#EFF8FB')
    E23.place(x=40,y=660)
    E24=Text(n,width=2, height=1,bg='#EFF8FB')
    E24.place(x=40,y=690)
    E25=Text(n,width=2, height=1,bg='#EFF8FB')
    E25.place(x=40,y=720)
    E26=Text(n,width=2, height=1,bg='#EFF8FB')
    E26.place(x=40,y=750)
    E27=Text(n,width=2, height=1,bg='#EFF8FB')
    E27.place(x=40,y=780)
    #E28=Text(n,width=2, height=1,bg='#EFF8FB')
    #E28.place(x=40,y=810)
    #E29=Text(n,width=2, height=1,bg='#EFF8FB')
    #E29.place(x=40,y=840)
    #E30=Text(n,width=2, height=1,bg='#EFF8FB')
    #E30.place(x=40,y=870)
    #E31=Text(n,width=2, height=1,bg='#EFF8FB')
    #E31.place(x=40,y=900)
    #E32=Text(n,width=2, height=1,bg='#EFF8FB')
    #E32.place(x=40,y=930)
    #E33=Text(n,width=2, height=1,bg='#EFF8FB')
    #E33.place(x=40,y=960)
    #E34=Text(n,width=2, height=1,bg='#EFF8FB')
    #E34.place(x=40,y=990)
    #E35=Text(n,width=2, height=1,bg='#EFF8FB')
    #E35.place(x=40,y=1010)
    #E36=Text(n,width=2, height=1,bg='#EFF8FB')
    #E36.place(x=40,y=1040)
    #E37=Text(n,width=2, height=1,bg='#EFF8FB')
    #E37.place(x=40,y=1070)
    #E38=Text(n,width=2, height=1,bg='#EFF8FB')
    #E38.place(x=40,y=1100)
    #E39=Text(n,width=2, height=1,bg='#EFF8FB')
    #E39.place(x=40,y=1130)
    #E40=Text(n,width=2, height=1,bg='#EFF8FB')
    #E40.place(x=125,y=120)
    #E41=Text(n,width=2, height=1,bg='#EFF8FB')
    #E41.place(x=125,y=120)
    #E42=Text(n,width=2, height=1,bg='#EFF8FB')
    #E42.place(x=125,y=120)
    #E43=Text(n,width=2, height=1,bg='#EFF8FB')
    #E43.place(x=125,y=120)
    #E44=Text(n,width=2, height=1,bg='#EFF8FB')
    #E44.place(x=125,y=120)
    #E45=Text(n,width=2, height=1,bg='#EFF8FB')
    #E45.place(x=125,y=120)
    #E46=Text(n,width=2, height=1,bg='#EFF8FB')
    #E46.place(x=125,y=120)


    label1 = tk.Label(n,text = "Langue Source",font=("Times New Roman", 11),bg='#ff9a8d')
    label1.place(x=10,y=10)


    E_02=Text(n,width=2, height=1,bg='#EFF8FB')
    E_02.place(x=150,y=30)
    E_03=Text(n,width=2, height=1,bg='#EFF8FB')
    E_03.place(x=150,y=60)
    E_04=Text(n,width=2, height=1,bg='#EFF8FB')
    E_04.place(x=150,y=90)
    E_05=Text(n,width=2, height=1,bg='#EFF8FB')
    E_05.place(x=150,y=120)
    E_06=Text(n,width=2, height=1,bg='#EFF8FB')
    E_06.place(x=150,y=150)
    E_07=Text(n,width=2, height=1,bg='#EFF8FB')
    E_07.place(x=150,y=180)
    E_08=Text(n,width=2, height=1,bg='#EFF8FB')
    E_08.place(x=150,y=210)
    E_09=Text(n,width=2, height=1,bg='#EFF8FB')
    E_09.place(x=150,y=240)
    E_010=Text(n,width=2, height=1,bg='#EFF8FB')
    E_010.place(x=150,y=270)
    E_011=Text(n,width=2, height=1,bg='#EFF8FB')
    E_011.place(x=150,y=300)
    E_012=Text(n,width=2, height=1,bg='#EFF8FB')
    E_012.place(x=150,y=330)
    E_013=Text(n,width=2, height=1,bg='#EFF8FB')
    E_013.place(x=150,y=360)
    E_014=Text(n,width=2, height=1,bg='#EFF8FB')
    E_014.place(x=150,y=390)
    E_015=Text(n,width=2, height=1,bg='#EFF8FB')
    E_015.place(x=150,y=420)
    E_016=Text(n,width=2, height=1,bg='#EFF8FB')
    E_016.place(x=150,y=450)
    E_017=Text(n,width=2, height=1,bg='#EFF8FB')
    E_017.place(x=150,y=480)
    E_018=Text(n,width=2, height=1,bg='#EFF8FB')
    E_018.place(x=150,y=510)
    E_019=Text(n,width=2, height=1,bg='#EFF8FB')
    E_019.place(x=150,y=540)
    E_020=Text(n,width=2, height=1,bg='#EFF8FB')
    E_020.place(x=150,y=570)
    E_021=Text(n,width=2, height=1,bg='#EFF8FB')
    E_021.place(x=150,y=600)
    E_022=Text(n,width=2, height=1,bg='#EFF8FB')
    E_022.place(x=150,y=630)
    E_023=Text(n,width=2, height=1,bg='#EFF8FB')
    E_023.place(x=150,y=660)
    E_024=Text(n,width=2, height=1,bg='#EFF8FB')
    E_024.place(x=150,y=690)
    E_025=Text(n,width=2, height=1,bg='#EFF8FB')
    E_025.place(x=150,y=720)
    E_026=Text(n,width=2, height=1,bg='#EFF8FB')
    E_026.place(x=150,y=750)
    E_027=Text(n,width=2, height=1,bg='#EFF8FB')
    E_027.place(x=150,y=780)
    #E_028=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_028.place(x=150,y=810)
    #E_029=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_029.place(x=150,y=149)
    #E_030=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_030.place(x=150,y=149)
    #E_031=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_031.place(x=150,y=149)
    #E_032=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_032.place(x=150,y=149)
    #E_033=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_033.place(x=150,y=149)
    #E_034=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_034.place(x=150,y=149)
    #E_035=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_035.place(x=175,y=149)
    #E_036=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_036.place(x=175,y=149)
    #E_037=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_037.place(x=175,y=149)
    #E_038=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_038.place(x=175,y=149)
    #E_039=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_039.place(x=175,y=149)
    #E_040=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_040.place(x=175,y=149)
    #E_041=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_041.place(x=175,y=149)
    #E_042=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_042.place(x=175,y=149)
    #E_043=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_043.place(x=175,y=149)
    #E_044=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_044.place(x=175,y=149)
    #E_045=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_045.place(x=175,y=149)
    #E_046=Text(n,width=2, height=1,bg='#EFF8FB')
    #E_046.place(x=175,y=149)

    conf = Button(n,text ="configurer" , command = configuration ,width="10", height="1",cursor="star",bg="#4a536b",fg='#eee5e8',font=("Times New Roman", 11))
    conf.place(x=250, y=10)
    


    bou23 = Button(n,text ="Quitter",font=("Times New Roman", 11), command =n.destroy,width="10", height="1",cursor="star",bg="#4a536b",fg='#eee5e8')
    #bou.grid(row =2, column =0, padx =8, pady =8)
    bou23.place(x=350, y=10)
    s.wait_window(n)




#fonction lancaster stemming par algorithme lancaster         
#fonction porter
          
#fonction qui permet de faire le stemming par l'algo  snowball 
  


# creation d'une nouvelle fenetre 
s=Tk()   
# definir la taille de la fenetre  
s.geometry("900x600")
s.minsize(900,600)
s.maxsize(900,600)

# definir le nom de l'interface 
s.title("Translittérateur")
#definir la couleur de l'arriere plan 
s.config(background='#ff9a8d')
# definir une image pour comme logo
s.iconbitmap("MIT.ico")

#creation de la place qui contiendera le resultat apres
output = scrolledtext.ScrolledText(s, 
                                      wrap = tk.WORD, 
                                      width = 50, 
                                      height = 14, 
                                      font = ("Times New Roman",
                                              12))
  
output.grid(column = 0, pady = 10, padx = 10)
  
# Placing cursor in the text area
output.focus() 
output.place(x=480, y=240)

#creation de l'entete de l'interface 
#head=Label(text=" Traitement Automatique de Language", bg="#4a536b", fg="#FFFFFF", width="90", height="1",font=("Times New Roman", 14))
#head.grid(row=0, column=0,sticky=W)

bout = Button(text ="Configuration",command = confg , width="10", height="1",cursor="star",bg="#9D9D9D",fg='#000000',font=("Times New Roman", 11))
bout.place(x=800, y= 32)


#lb= LabelFrame(s ,text="Saisissez votre texte",width="1000",height="135",bg='#ff9a8d',fg='#000000',font=("Times New Roman", 11))
#lb.place(x=0, y=62)

#creation de la place Texte où le texte saisi
ENT= scrolledtext.ScrolledText(s,    wrap = tk.WORD, 
                                      width = 50, 
                                      height =14, 
                                     font = ("Times New Roman",
                                              12))
ENT.grid(column = 0, pady = 10, padx = 10)
  
# Placing cursor in the text area
ENT.focus()
#♠ENT=Text(s,width=112, height=7,bg='#EFF8FB')
ENT.place(x=0,y=240)

label1 = tk.Label(s,text = "Vers",font=("Agency FB", 16),bg='#ff9a8d')
label1.place(x=432,y=350)

#creation du labelframe qui contiendera le combobox du choix des stemmers
lb= LabelFrame(s ,text="Partie de Traitement",width="1000",height="135",bg='#ff9a8d',fg='white',font=("Times New Roman", 11))
lb.place(x=0, y=70)


#creation du label choisissez un texte 
labelTop = tk.Label(s,
                    text = "Choisissez la langue",font=("Times New Roman", 16),bg='#ff9a8d')
labelTop.place(x=70,y=90)

source = open("Source.txt")

S = source.read().replace("\n", " ")
source.close()

cible = open("Cible.txt")

C = cible.read().replace("\n", " ")
cible.close()
#creation du combobox qui contient les differents algo utilisés et qui permet de choisir un parmi le tout
comboExample1 = ttk.Combobox(s, 
                            value=[
                                    
                                    "Arabe",
                                    "Latin",
                                    "Amazigh",
                                     C
                                    ],font=("Agency FB", 16),width='7')

comboExample1.place(x=30,y=125)
comboExample1.current(1)

comboExample2 = ttk.Combobox(s, 
                            values=[
                                    
                                    "Arabe",
                                    "Latin",
                                    "Amazigh ",
                                       S
                                    ],font=("Agency FB", 16),width='7')

comboExample2.place(x=176,y=125)
comboExample2.current(1)

label1 = tk.Label(s,text = "Vers",font=("Agency FB", 16),bg='#ff9a8d')
label1.place(x=130,y=125)


#creation du label résultat
t1=Label(text="Translittération",width="60", height="1",bg="#aed6dc",relief=SUNKEN, font=("Times New Roman", 20))
t1.place(x= 0, y=205)

#creation du bouton qui permet de recuperer le nomdu stemmer choisi et de calculer le stem ainsi de calculer la frequence de chaque stem et d'afficher le resultat dans la place correspondante 
bou = Button(text ="Translittérer", command = transliteration,width="10", height="1",cursor="star",bg="#111010",fg='#eee5e8',font=("Times New Roman", 11))
bou.place(x=100, y= 165)

#creation du labelframe qui contiendera les boutons permettant d'importer un texte 
lb= LabelFrame(s ,text="Parcourir",width="347",height="120",bg='#ff9a8d',fg='white')
lb.place(x=490, y=80)
#creation du label importer un texte 
t=Label(lb,text="Importer un texte:",bg='#ff9a8d',fg='#f4eef0', width="15", height="1", font=("Times New Roman", 20))
t.place(x= 1, y=0)
#creation du bouton qui permet d'importer un fichier texte de type .txt 
impotxt= Button(lb,text= "Texte \n(.txt)", font=("Times New Roman", 10), width="12", height="2", command=ouvrirTexte ,bg="#4a536b",fg='#eee5e8') 
impotxt.place(x=10, y=50)
#creation du bouton qui permet d'importer un fichier word  de type .docx
impowrd= Button(lb,text= "Document Word \n(.Docx)",font=("Times New Roman", 10), width="12", height="2", command=ouvrirWord ,bg="#4a536b",fg='#eee5e8') 
impowrd.place(x=120, y=50)

importf= Button(lb,text= "RTF \n(.RTF)",font=("Times New Roman", 10), width="12", height="2", command=ouvrirRTF ,bg="#4a536b",fg='#eee5e8') 
importf.place(x=230, y=50)

impordoss= Button(lb,text= "Plusieur \nfichier (.txt)",font=("Times New Roman", 10), width="12", height="2", command=importation ,bg="#4a536b",fg='#eee5e8') 
impordoss.place(x=230, y=1)

#creation du label enregistrer le texte apres stemming 
t10=Label(text="Enregistrer le texte Translittérer en format .txt",bg='#ff9a8d', width="35", height="1", font=("Times New Roman", 14))
t10.place(x=0, y=523)
#creation du bouton qui permet d'enregistrer le texte en global apres stemming  
bou = Button(text ="Enregistrer",font=("Times New Roman", 10), command =ENR2,width="10", height="1",cursor="star",bg="#4a536b",fg='#eee5e8')
bou.place(x=360, y= 523)

#creation du label Enregistrer les informations en fichier xml :
t11=Label(text="Enregistrer le texte Translittérer en format .PDF",bg='#ff9a8d', width="35", height="1", font=("Times New Roman", 14))
t11.place(x= 0, y=556)
#creation du bouton qui permet d'enregistrer chaque mot de texte avant et apre le stemming ainsi que la frequence de chaque stem dans un fichier xml sous forme de balises 
bou = Button(text ="Enregistrer", font=("Times New Roman", 10),command =ENr,width="10", height="1",cursor="star",bg="#4a536b",fg='#eee5e8')
bou.place(x=360, y= 556)

#creation du bouton reintialiser 
bou22 = Button(text ="Réintialiser",font=("Times New Roman", 12), command =effacer,width="10", height="1",cursor="star",bg="#F7BBBB",fg='#000000')
#bou.grid(row =2, column =0, padx =8, pady =8)
bou22.place(x=780, y= 556)  

#creation du bouton quitter 
bou23 = Button(text ="Quitter",font=("Times New Roman", 12), command =clo,width="10", height="1",cursor="star",bg="#F7BBBB",fg='#000000')
#bou.grid(row =2, column =0, padx =8, pady =8)
bou23.place(x=680, y= 556)  
s.mainloop()
