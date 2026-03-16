
import sys
from PyQt6 import uic
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from models import Money
from dao import *

# สีเขียวเเดง สำหรับรายรับรายจ่าย
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtGui import QColor

def add_data(self, row, id, income, expense, date, note):

    id_item = QTableWidgetItem(str(id))

    income_item = QTableWidgetItem(str(income))
    income_item.setBackground(QColor(200,255,200))  # สีเขียว

    expense_item = QTableWidgetItem(str(expense))
    expense_item.setBackground(QColor(255,200,200))  # สีแดง

    date_item = QTableWidgetItem(str(date))
    note_item = QTableWidgetItem(str(note))

    self.tbMoney.setItem(row,0,id_item)
    self.tbMoney.setItem(row,1,income_item)
    self.tbMoney.setItem(row,2,expense_item)
    self.tbMoney.setItem(row,3,date_item)
    self.tbMoney.setItem(row,4,note_item)
#
class MainWindow(QMainWindow):
    def __init__(self):
        super() .__init__()
        uic.loadUi('untitled.ui', self)

        #set table column width
        self.tbMoney.setColumnWidth(0, 50)
        self.tbMoney.setColumnWidth(1, 100)
        self.tbMoney.setColumnWidth(2, 100)
        self.tbMoney.setColumnWidth(3, 100)
        self.tbMoney.setColumnWidth(4, 200)

        self.showMoney()
    
        #signal & slot
        self.btnImport.clicked.connect(self.importMoney)
        self.tbMoney.clicked.connect(self.getRow)
        self.tbMoney.cellClicked.connect(self.selectedRow)
        self.btnUpdate.clicked.connect(self.updateMoney)
        self.btnDelete.clicked.connect(self.deleteMoney)
        self.btnClear.clicked.connect(self.clearData)
        self.btnSearch.clicked.connect(self.searchMoney)
    

    def searchMoney(self):

        keyword = self.txtSearch.text()
        money = search_money(keyword)

        self.tbMoney.setRowCount(len(money))
        self.txtSearch.setText('')

        row = 0
        for m in money:

            self.tbMoney.setItem(row, 0, QTableWidgetItem(str(m.id)))

            income_item = QTableWidgetItem(str(m.income))
            income_item.setBackground(QColor(200,255,200))

            expense_item = QTableWidgetItem(str(m.expenses))
            expense_item.setBackground(QColor(255,200,200))

            self.tbMoney.setItem(row,1,income_item)
            self.tbMoney.setItem(row,2,expense_item)
            self.tbMoney.setItem(row,3,QTableWidgetItem(str(m.date)))
            self.tbMoney.setItem(row,4,QTableWidgetItem(str(m.note)))

            row += 1

    def showMoney(self):
        money = select()
        if len(money) > 0:
            self.tbMoney.setRowCount(len(money))
            row = 0
            for m in money:
                add_data(
                    self,
                    row,
                    m.id,
                    m.income,
                    m.expenses,
                    m.date,
                    m.note
                )
                row += 1
        else:
                self.tbMoney.setRowCount(0)

            

    def clearData(self):
        self.txtIncome.setText('')
        self.txtExpenses.setText('')
        self.txtDate.setText('')
        self.txtNote.setText('')

        self.tbMoney.clearSelection()

        self.btnImport.setEnabled(True)
        self.btnUpdate.setEnabled(False)
        self.btnDelete.setEnabled(False)

        self.showMoney()



    def deleteMoney(self):

        row = self.tbMoney.currentRow()

        id = int(self.tbMoney.item(row,0).text())

        r = delete(id)

        if r > 0:
            QMessageBox.information(self,"Information","Delete Success")
        else:
            QMessageBox.warning(self,"Warning","Delete Failed")

        self.showMoney()
        self.clearData()


    def importMoney(self):
        income = int(self.txtIncome.text())
        expenses = int(self.txtExpenses.text())
        date = self.txtDate.text()
        note = self.txtNote.text()

        money = Money(id=0, income=income, expenses=expenses, date=date, note=note)
        row = insert(money=money)
        if row > 0:
            QMessageBox.information(self,'Information', 'Insert Money Successfully' )
            
        else:
            QMessageBox.warning(self,'warning', 'Unable to insert money' )

        self.clearData()
        self.showMoney()
    
    def selectedRow(self):
        row = self.tbMoney.currentRow()
        id = self.tbMoney.item(row, 0).text()
        income = self.tbMoney.item(row, 1).text()
        expenses = self.tbMoney.item(row, 2).text()
        date = self.tbMoney.item(row, 3).text()
        note = self.tbMoney.item(row, 4).text()

        
        self.txtIncome.setText(income)
        self.txtExpenses.setText(expenses)
        self.txtDate.setText(date)
        self.txtNote.setText(note)

        self.btnImport.setEnabled(False)
        self.btnUpdate.setEnabled(True)
        self.btnDelete.setEnabled(True)


    def updateMoney(self):

        row = self.tbMoney.currentRow()

        id = int(self.tbMoney.item(row,0).text())
        income = int(self.txtIncome.text())
        expenses = int(self.txtExpenses.text())
        date = self.txtDate.text()
        note = self.txtNote.text()

        money = Money(id=id, income=income, expenses=expenses, date=date, note=note)

        r = update(money)

        if r > 0:
            QMessageBox.information(self,"Information","Update Success")
        else:
            QMessageBox.warning(self,"Warning","Update Failed")

        self.showMoney()
        self.clearData()
    

    def getRow(self):
        row = self.tbMoney.currentRow()

        self.txtIncome.setText(self.tbMoney.item(row,1).text())
        self.txtExpenses.setText(self.tbMoney.item(row,2).text())
        self.txtDate.setText(self.tbMoney.item(row,3).text())
        self.txtNote.setText(self.tbMoney.item(row,4).text())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()