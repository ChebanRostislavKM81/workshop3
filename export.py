import csv
import cx_Oracle


username = 'cheban'
password = '988823707'
database = 'localhost/xe'

connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

partes = ['Results','Cities','Neutral'] 

try:    
    for part in partes:
        with open(part +  '.csv', 'w', newline='') as file:
            cursor.execute("select * from " + part)
            line = cursor.fetchone()


            lines = []
            for string in cursor.description:
                lines.append(string[0])   
            w = csv.writer(file, delimiter=',')
            w.writerow(lines)


           
            while line:
                w.writerow(line)
                line = cursor.fetchone()


finally:
    cursor.close()
    connection.close()
