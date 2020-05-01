import sqlite3 as sql
conn=sql.connect("/Users/macbook/Documents/S6/miniProjet/student.db")
cur=conn.cursor()

# creation des tables

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




conn.commit()
conn.close()
