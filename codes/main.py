import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class window(QWidget):
   def __init__(self, parent = None):
      super(window, self).__init__(parent)
      self.resize(1280,720)
      self.setWindowTitle("App with PyQt5")
      self.label1 = QLabel(self)
      self.label1.setText("First Text!")
      self.label2 = QLabel(self)
      self.label2.setText("Second text!")
      self.label3 = QLabel(self)
      self.label3.setText("Third text.")
      font = QFont()
      font.setFamily("Arial")
      font.setPointSize(16)
      self.label1.setFont(font)
      self.label2.setFont(font)
      self.label3.setFont(font)
      self.label1.move(620,100)
      self.label2.move(610,200)
      self.label3.move(620,300)
def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   main()