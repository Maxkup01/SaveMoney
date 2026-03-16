from connectdb import con, cur
from models import Money

def insert(money: Money):
    sql = 'insert into Money(income, expenses, date, note) values(?,?,?,?)'
    rs = con.execute(sql, (money.income, money.expenses, money.date, money.note))
    row = rs.rowcount
    if row > 0:
        con.commit()
        return row
    else:
        return 0

def update(money: Money):
    sql = 'update money set income=?, expenses=?, date=?, note=? where id=?'
    rs = con.execute(sql, (money.income, money.expenses, money.date, money.note, money.id))
    row = rs.rowcount
    if row > 0:
        con.commit()
        return row
    else:
        return 0
    
def delete(id: int):
    sql = 'delete from money where id = ?'
    rs = con.execute(sql, (id, ))
    row = rs.rowcount
    if row > 0:
        con.commit()
        return row
    else:
        return 0

def search_money(keyword: str):

    sql = '''
    select * from money 
    where 
        id like ? OR
        income like ? OR
        expenses like ? OR
        date like ? OR
        note like ?
    '''

    key = '%' + keyword + '%'

    rs = con.execute(sql, (key, key, key, key, key))
    rows = rs.fetchall()

    data = []

    for row in rows:
        id, income, expenses, date, note = row
        data.append(
            Money(
                id=id,
                income=income,
                expenses=expenses,
                date=date,
                note=note
            )
        )

    return data

def select():
    sql = 'select * from money'
    rs = con.execute(sql)
    rows = rs.fetchall()

    data = []
    for row in rows:
        id, income, expenses, date, note = row
        data.append(Money(id=id, income=income, expenses=expenses, date=date, note=note))

    return data        