import sqlite3 as sql
import matplotlib
matplotlib.use('TkAgg')
conn=sql.connect("/Users/macbook/Documents/S6/miniProjet/student.sqlite")
cur=conn.cursor()

# creation des tables
"""
cur.execute(" CREATE TABLE IF NOT EXISTS Auteur ( Nauteur Integer,nomA text,prenomA text,nationaliteA text,PRIMARY KEY(Nauteur) ) ")
cur.execute(" CREATE TABLE IF NOT EXISTS Livre ( Nlivre Integer,num_ISBN Integer,titre text,nbPages Integer,anneeS Integer,prix real, PRIMARY KEY(Nlivre) ) ")
cur.execute(" CREATE TABLE IF NOT EXISTS Possede (Nlivre Integer, Nauteur Integer, FOREIGN KEY(Nlivre) REFERENCES Livre(Nlivre), FOREIGN KEY(Nauteur) REFERENCES Auteur(Nauteur) ) ")
cur.execute(" CREATE TABLE IF NOT EXISTS Pret ( Npret Integer,num_etu Integer,Nlivre Integer,datePret text,dateRetour text,DateRetourPrevue text, PRIMARY KEY(Npret), FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu), FOREIGN KEY(Nlivre) REFERENCES Livre(Nlivre) ) ")
cur.execute(" CREATE TABLE IF NOT EXISTS Etudiant(num_etu Integer,nomE text,prenomE text, date_naissance text, ville text, dateInscriptionBU text, dateAbs text,numClasse Integer, PRIMARY KEY(num_etu), FOREIGN KEY(numClasse) REFERENCES Class(numClass) ) ")
cur.execute(" CREATE TABLE IF NOT EXISTS Class (numClass Integer,nomClass text, PRIMARY KEY(numClass) ) ")
cur.execute(" CREATE TABLE IF NOT EXISTS Cours (num_cours Integer,nomC text,nb_heures real,num_ens Integer,PRIMARY KEY(num_cours), FOREIGN KEY(num_ens)REFERENCES Enseignant(num_ens)) ")
cur.execute(" CREATE TABLE IF NOT EXISTS Enseignant (num_ens Integer,nomP text,prenomP text,specialite text,departement text, PRIMARY KEY(num_ens)) ")
cur.execute(" CREATE TABLE IF NOT EXISTS Resultat (num_etu Integer,num_cours integer,note real,FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu), FOREIGN KEY(num_cours) REFERENCES Cours(num_cours)) ")
cur.execute(" CREATE TABLE IF NOT EXISTS Charge (num_cours Integer,num_ens Integer, nbH real, FOREIGN KEY(num_cours) REFERENCES Cours(num_cours), FOREIGN KEY(num_ens) REFERENCES Enseignant(num_ens) ) ")
cur.execute(" CREATE TABLE IF NOT EXISTS Inscrit (NumEtudiant Integer,num_cours Integer,dateInsC text,FOREIGN KEY(NumEtudiant) REFERENCES Etudiant(num_etu), FOREIGN KEY(num_cours) REFERENCES Cours(num_cours) ) ")

# insertion des donnees de la table Etudiant

cur.execute("INSERT INTO Etudiant VALUES (1,'prenom1','nom1','01-01-1999','marrakech','01-01-2010','20-10-2010',10)")
cur.execute("INSERT INTO Etudiant VALUES (2,'prenom2','nom2','01-02-1999','marrakech','02-01-2010','21-10-2010',11)")
cur.execute("INSERT INTO Etudiant VALUES (3,'prenom3','nom3','01-03-1999','marrakech','03-01-2010','22-10-2010',12)")
cur.execute("INSERT INTO Etudiant VALUES (4,'prenom4','nom4','01-04-1999','marrakech','04-01-2010','23-10-2010',13)")
cur.execute("INSERT INTO Etudiant VALUES (5,'prenom5','nom5','01-05-1999','marrakech','05-01-2010','24-10-2010',14)")
cur.execute("INSERT INTO Etudiant VALUES (6,'prenom6','nom6','01-06-1999','marrakech','06-01-2010','25-10-2010',15)")
cur.execute("INSERT INTO Etudiant VALUES (7,'prenom7','nom7','01-07-1999','marrakech','07-01-2010','26-10-2010',10)")
cur.execute("INSERT INTO Etudiant VALUES (8,'prenom8','nom8','01-08-1999','marrakech','08-01-2010','27-10-2010',11)")
cur.execute("INSERT INTO Etudiant VALUES (9,'prenom9','nom9','01-09-1999','marrakech','09-01-2010','28-10-2010',5)")
cur.execute("INSERT INTO Etudiant VALUES (10,'prenom10','nom10','01-10-1999','marrakech','10-01-2010','29-10-2010',1)")

# insertion des donnees de la table Resultat

cur.execute(" INSERT INTO Resultat VALUES (1,1,18) ")
cur.execute(" INSERT INTO Resultat VALUES (1,2,16) ")
cur.execute(" INSERT INTO Resultat VALUES (1,3,20) ")

cur.execute(" INSERT INTO Resultat VALUES (2,1,17) ")
cur.execute(" INSERT INTO Resultat VALUES (2,2,15) ")
cur.execute(" INSERT INTO Resultat VALUES (2,3,17) ")

cur.execute(" INSERT INTO Resultat VALUES (3,1,16) ")
cur.execute(" INSERT INTO Resultat VALUES (3,2,12) ")
cur.execute(" INSERT INTO Resultat VALUES (3,3,10) ")

cur.execute(" INSERT INTO Resultat VALUES (4,1,19) ")
cur.execute(" INSERT INTO Resultat VALUES (4,2,18) ")
cur.execute(" INSERT INTO Resultat VALUES (4,3,17) ")

cur.execute(" INSERT INTO Resultat VALUES (5,1,20) ")
cur.execute(" INSERT INTO Resultat VALUES (5,2,18) ")
cur.execute(" INSERT INTO Resultat VALUES (5,3,18) ")

cur.execute(" INSERT INTO Resultat VALUES (6,1,11) ")
cur.execute(" INSERT INTO Resultat VALUES (6,2,14) ")
cur.execute(" INSERT INTO Resultat VALUES (6,3,15) ")

cur.execute(" INSERT INTO Resultat VALUES (7,1,10) ")
cur.execute(" INSERT INTO Resultat VALUES (7,2,10) ")
cur.execute(" INSERT INTO Resultat VALUES (7,3,11) ")

cur.execute(" INSERT INTO Resultat VALUES (8,1,13) ")
cur.execute(" INSERT INTO Resultat VALUES (8,2,15) ")
cur.execute(" INSERT INTO Resultat VALUES (8,3,16) ")

cur.execute(" INSERT INTO Resultat VALUES (9,1,14) ")
cur.execute(" INSERT INTO Resultat VALUES (9,2,17) ")
cur.execute(" INSERT INTO Resultat VALUES (9,3,13) ")

cur.execute(" INSERT INTO Resultat VALUES (10,1,17) ")
cur.execute(" INSERT INTO Resultat VALUES (10,2,18) ")
cur.execute(" INSERT INTO Resultat VALUES (10,3,20) ")
"""
def insBU(nomE):

    cur.execute("SELECT Etudiant.dateInscriptionBU FROM Etudiant WHERE nomE=:nomE", {'nomE':nomE} )
    rows = cur.fetchall()
    for row in rows:
        print(row)

def insCour(num_cours):

    cur.execute("SELECT nomE, prenomE FROM Etudiant AS E JOIN Resultat AS R ON(E.num_etu = R.num_etu) JOIN Cours AS C ON(R.num_cours = C.num_cours) WHERE C.num_cours=:num_cours", {'num_cours':num_cours} )
    
    rows = cur.fetchall()

    for row in rows:
        print(row) 

def ResuEtu(num_etu):
    cur.execute("SELECT nomE, prenomE,note,nomC,AVG(note) as moyenne,max(note) ,min(note) FROM Etudiant AS E JOIN Resultat AS R ON(E.num_etu = R.num_etu) JOIN Cours AS C ON(R.num_cours = C.num_cours) WHERE E.num_etu =:num_etu ", { 'num_etu':num_etu}  )
    rows = cur.fetchall()

    for row in rows:
        print(row)

def empLiv(Nlivre):

    cur.execute("SELECT nomE, dateRetour FROM Etudiant AS E JOIN Pret AS P ON(E.num_etu=P.num_etu) JOIN Livre AS L ON(P.Nlivre=L.Nlivre) WHERE L.Nlivre=:Nlivre", {'Nlivre':Nlivre} )
    
    rows = cur.fetchall()

    for row in rows:
        print(row)

def ResultTot():
	cur.execute(" SELECT C.nomclass, Crs.nomC,AVG(note) AS Moyenne FROM Etudiant AS E JOIN Class AS C ON (E.numClasse=C.numClass) JOIN Resultat AS R ON(E.num_etu = R.num_etu) JOIN Cours AS Crs ON(R.num_cours = Crs.num_cours) GROUP BY C.nomclass, Crs.nomC ")
	rows=cur.fetchall()
	for row in rows:
		print(row)

def retard():

    cur.execute("SELECT nomE FROM Etudiant AS E JOIN Pret AS P ON(E.num_etu=P.num_etu) JOIN Livre AS L ON(P.Nlivre=L.Nlivre) WHERE dateRetour> DateRetourPrevue" )
    
    rows = cur.fetchall()
    for row in rows:
    	print(row)

def resultEchec():

    cur.execute("SELECT note,avg(note) AS Moyenne, prenomE, nomE FROM Resultat AS R JOIN Etudiant AS E ON(R.num_etu = E.num_etu) JOIN Cours AS C ON(R.num_cours=C.num_cours) WHERE note<11 GROUP BY nomC" )
    
    rows = cur.fetchall()

    for row in rows:
        print(row)  
def insc():
    cur.execute(" SELECT nomE FROM Etudiant AS E JOIN Resultat AS R ON(E.num_etu=R.num_etu) JOIN Cours AS Crs ON(R.num_cours=Crs.num_cours) ")
    rows=cur.fetchall()
    for row in rows:
        print(row)

def changer_nomC(num_cours,nomC):
   with conn:
    cur.execute("UPDATE Cours SET nomC=:nomC WHERE num_cours=:num_cours", {'num_cours':num_cours, 'nomC':nomC})

def supp_Cours(num_cours):
    with conn:
        cur.execute("DELETE FROM Cours WHERE num_cours=:num_cours",{'num_cours':num_cours}) 

def noteSup14():
    cur.execute("SELECT AVG(note) FROM Resultat GROUP BY num_etu HAVING AVG(note)>14")
    return len(cur.fetchall())

def note1214():
    cur.execute("SELECT AVG(note) FROM Resultat GROUP BY num_etu HAVING AVG(note) BETWEEN 12 AND 14")
    return len(cur.fetchall())

def noteInf8():
    cur.execute("SELECT AVG(note) FROM Resultat GROUP BY num_etu HAVING AVG(note)<8")
    return len(cur.fetchall())

def note810():
    cur.execute("SELECT AVG(note) FROM Resultat GROUP BY num_etu HAVING AVG(note) BETWEEN 8 AND 10")
    return len(cur.fetchall())

def note1012():
    cur.execute("SELECT AVG(note) FROM Resultat GROUP BY num_etu HAVING AVG(note) BETWEEN 10 AND 12")
    return len(cur.fetchall())
import matplotlib.pyplot as plt

fig,ax = plt.subplots()
ax.axis("equal")
ax.pie([noteSup14(),note1214(),noteInf8(),note810(),note1012()],
        shadow=True,
        colors=["green","blue","orange","red","brown"],
        labels = ["nb eleve note>14", "nb eleve 12<note<14","nb eleve note<8","nb elever 8<note<10","nb eleve 10<notew12"],
        autopct="%1.1f"),
plt.title("Graphe de Moyenne Generale")
plt.show()  
"""
def nbEleves(note):
    cur.execute("SELECT num_etu FROM Resultat GROUP BY num_etu HAVING AVG(note)=:note",{'note':note})
    return len(cur.fetchall())

x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
hauteurs_barres = [8,12,8,5,4,3,2,1,0,0]
largeur_barres = 0.1
plt.bar(x, hauteurs_barres, largeur_barres) 
plt.show()"""

conn.close()
