import cx_Oracle
import re
import chart_studio
import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dashboard

username = 'cheban'
password = '988823707'
database = 'localhost/xe'

connection = cx_Oracle.connect(username, password, database)
query1 = '''select home_team, count(*) From MATCH Group by home_team'''
query3= ''' select city, count(*) from MATCH where tournament!= 'friendly' group by city'''
query2= ''' select away_team, count(*) From MATCH Group by away_team'''
query4= '''select count(*)/(select count(*) from MATCH)*100 AS percent FROM MATCH WHERE neutral = 'TRUE' group by neutral'''
cursor = connection.cursor()
cursor.execute(query1)

result1 = cursor.fetchall()


cursor.execute(query2)
result2 = cursor.fetchall()

cursor.execute(query3)
result3 = cursor.fetchall()

cursor.execute(query4)
result4 = cursor.fetchall()

chart_studio.tools.set_credentials_file(username='RostislavCheban', api_key='bVjKao3TjEjW5DJ4zxu3')

home_team = list(map(lambda x: x[0], result1))
matches = list(map(lambda x: x[1], result1))
bar = go.Bar(x=home_team, y=matches, marker_color='lightsalmon', name="Кількість зіграних домашніх матчів")
layout = go.Layout(
    title='Кількість зіграних домашніх матчів',
    xaxis=dict(
        title='Команда',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Домашні матчі',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=bar, layout=layout)
home_team_matches = py.plot(fig, filename='Home Team Matches')

away_team = list(map(lambda x: x[0], result2))
away_matches = list(map(lambda x: x[1], result2))
bar = go.Bar(x=away_team, y=away_matches, marker_color='lightsalmon', name="Кількість зіграних виїздних матчів")
layout = go.Layout(
    title=
'Кількість зіграних виїздних матчів',
    xaxis=dict(
        title='Команда',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Виїздні матчі',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=bar, layout=layout)
away_team_matches = py.plot(fig, filename='Away Team Matches')

city = list(map(lambda x: x[0], result3))
tournament = list(map(lambda x: x[1], result3))
bar = go.Bar(x=city, y=tournament, marker_color='lightsalmon', name="Кількість проведених турнірів в місті")
layout = go.Layout(
    title=
'Кількість проведених турнірів в місті',
    xaxis=dict(
        title='Місто',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Турніри',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=bar, layout=layout)
count_tournament = py.plot(fig, filename='City and Tournament')




neutral_percent = float(result4[0][0])
rest = 100 - neutral_percent
pie = go.Pie(labels=['Neutral', 'NonNeutral'], values=[neutral_percent, rest],
             textinfo='percent', title="Відношення кількості нейтральних матчів до кількості всіх матчів")
neutral_matches_percent = py.plot([pie], filename='Pie')


def fileId_from_url(url):
    fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1:]
    return fileId.replace('/', ':')
my_dboard = dashboard.Dashboard()
home_team_matches_id = fileId_from_url(home_team_matches)
away_team_matches_id = fileId_from_url(away_team_matches)
count_tournament_id = fileId_from_url(count_tournament)
neutral_matches_percent_id = fileId_from_url(neutral_matches_percent)
box1= {
    'type': 'box',
    'boxType': 'plot',
    'fileId': home_team_matches_id,
    'title': 'Кількість домашніх матчів'
}

box2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': away_team_matches_id,
    'title': 'Кількість виїздних матчів'
}

box3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': count_tournament_id,
    'title': 'Кількість прийнятих турнірів містом'
}
box4 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': neutral_matches_percent_id,
    'title': 'Відношення кількості матчів на нейтральних полях до повної кількості матчів'
}

my_dboard.insert(box4)
my_dboard.insert(box3, 'below', 1)
my_dboard.insert(box2, 'right', 2)
my_dboard.insert(box1, 'left', 3)

py.dashboard_ops.upload(my_dboard, 'Lab_3')
