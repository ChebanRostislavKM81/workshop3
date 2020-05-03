
import csv
import cx_Oracle


username = 'cheban'
password = '988823707'
database = 'localhost/xe'

connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

file = open('results.csv', errors='ignore')
read = csv.reader(file, delimiter=',')
counter = 1
try:
  for j in read:
      dates = j[0]
      home_team = j[1]
      away_team = j[2]
      home_score = j[3]
      away_score = j[4]
      tournament = j[5]
  query = '''
          INSERT INTO Results(dates, home_team, away_team, home_score, away_score, tournament) 
              VALUES(:dates, home_team, away_team, home_score, away_score, tournament)'''
         cursor.execute(query, dates=dates, home_team=home_team, away_team=away_team, home_score=home_score, away_score=away_score, tournament=tournament)

      counter += 1
except:
    print(f'Error in the {counter}')
    raise

file.close()
connection.commit()
cursor.close()
connection.close()
