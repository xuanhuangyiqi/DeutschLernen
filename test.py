#coding: utf-8
import sqlite3

conn = sqlite3.connect('example')

c = conn.cursor()

c.execute('''create table if not exists stocks(date text, trans text, symbol text,  qty real, price real)''')
 
# 插入数据，执行SQL语句
c.execute("""insert into stocks
           values ('2006-01-15','BUoY','RHATd',100,35.14)""")  
  
#将变动保存到数据库文件，如果没有执行词语句，则前面的insert 语句操作不会被保存
conn.commit()
   
#得到所有的记录
rec = c.execute('''select * from stocks''')
print c.fetchall()
