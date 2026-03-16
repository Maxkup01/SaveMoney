from connectdb import con

sql = '''
create table money(
id integer primary key autoincrement, 
Income integer, 
Expenses integer, 
Date date not null, 
Note txt);
'''

con.execute(sql)