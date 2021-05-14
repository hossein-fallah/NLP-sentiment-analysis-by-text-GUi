# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emotionprocessing.ui'
#
# Created by: Hossein Fallah - PyQt5 UI code generator 5.15.2


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import re
import os
from nested_lookup import nested_lookup
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report,classification,accuracy_score


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(719, 345)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 701, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pardazesh = QtWidgets.QPushButton(self.frame)
        self.pardazesh.setEnabled(True)
        self.pardazesh.setGeometry(QtCore.QRect(470, 30, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pardazesh.setFont(font)
        self.pardazesh.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pardazesh.setAutoFillBackground(False)
        self.pardazesh.setAutoDefault(False)
        self.pardazesh.setDefault(False)
        self.pardazesh.setObjectName("pardazesh")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 0, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.browse = QtWidgets.QPushButton(self.frame)
        self.browse.setGeometry(QtCore.QRect(470, 130, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.browse.setFont(font)
        self.browse.setObjectName("browse")
        self.showtext = QtWidgets.QTextEdit(self.frame)
        self.showtext.setGeometry(QtCore.QRect(10, 30, 451, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.showtext.setFont(font)
        self.showtext.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.showtext.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.showtext.setObjectName("showtext")
        self.clean = QtWidgets.QPushButton(self.frame)
        self.clean.setGeometry(QtCore.QRect(470, 80, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.clean.setFont(font)
        self.clean.setObjectName("clean")
        self.Preparation = QtWidgets.QPushButton(self.frame)
        self.Preparation.setEnabled(True)
        self.Preparation.setGeometry(QtCore.QRect(580, 80, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Preparation.setFont(font)
        self.Preparation.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Preparation.setAutoFillBackground(False)
        self.Preparation.setAutoDefault(False)
        self.Preparation.setDefault(False)
        self.Preparation.setObjectName("Preparation")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(580, 120, 111, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressbar")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 200, 701, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 441, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textEdit.setFont(font)
        self.textEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.textEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.textEdit.setObjectName("textEdit")
        self.mosbat_lable = QtWidgets.QLabel(self.frame_2)
        self.mosbat_lable.setGeometry(QtCore.QRect(610, 40, 67, 17))
        self.mosbat_lable.setObjectName("mosbat_lable")
        self.manfi = QtWidgets.QProgressBar(self.frame_2)
        self.manfi.setGeometry(QtCore.QRect(480, 60, 118, 16))
        self.manfi.setProperty("value", 0)
        self.manfi.setTextVisible(False)
        self.manfi.setFormat("")
        self.manfi.setObjectName("manfi")
        self.mosbat = QtWidgets.QProgressBar(self.frame_2)
        self.mosbat.setGeometry(QtCore.QRect(480, 40, 118, 16))
        self.mosbat.setAutoFillBackground(True)
        self.mosbat.setProperty("value", 0)
        self.mosbat.setTextVisible(False)
        self.mosbat.setFormat("")
        self.mosbat.setObjectName("mosbat")
        self.manfi_lable = QtWidgets.QLabel(self.frame_2)
        self.manfi_lable.setGeometry(QtCore.QRect(610, 60, 67, 17))
        self.manfi_lable.setObjectName("manfi_lable")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(470, 0, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondfs = QtWidgets.QAction(MainWindow)
        self.actiondfs.setObjectName("actiondfs")
        self.actionfs = QtWidgets.QAction(MainWindow)
        self.actionfs.setObjectName("actionfs")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    
    def vectorize_tfidf(self,df_X):
        tf_idf_vectorizer = TfidfVectorizer(lowercase=False)
        tf_idf_X = tf_idf_vectorizer.fit_transform(df_X)
        tf_idf_df = pd.DataFrame(data=tf_idf_X.toarray(),columns=[tf_idf_vectorizer.get_feature_names()])
        return tf_idf_df, tf_idf_vectorizer
    
    def split_data(self,X,y,test_size):
        return train_test_split(X, y, test_size=test_size)
 
    def prepare(self):
        #train and test
        stopwords = []
        file = open('stopwords.txt', encoding='utf-8').read()
        [stopwords.append(x) for x in file.split()]
        stopwords = set(stopwords)
        self.progressBar.setValue(10)
            
        with open('sample_dataset.json',encoding='utf-8-sig', errors='ignore') as file:
            json_file = json.load(file) 
        self.progressBar.setValue(20)   
            
        lst_cmnts = nested_lookup('comment', json_file)
        lst_sentiments = nested_lookup('sentiment', json_file)
        self.progressBar.setValue(30)    
        dic = {}
        for i,cmnt in enumerate(lst_cmnts):
            dic[cmnt] = lst_sentiments[i]
        self.progressBar.setValue(35)
        df = pd.DataFrame(list(dic.items()), columns=['comment','sentiment'])
        self.progressBar.setValue(45)
        dic ={0:'مثبت',1:'منفی'}

        df["sentiment"].value_counts()
        tf_idf_df, tf_idf_model = self.vectorize_tfidf(df['comment'])
        X_train, X_test, y_train, y_test = self.split_data(tf_idf_df,df['sentiment'],.3)
        self.progressBar.setValue(50)
        self.progressBar.setValue(60)
        self.progressBar.setValue(70)
        from sklearn.ensemble import RandomForestClassifier
        self.progressBar.setValue(80)
        self.rfc = RandomForestClassifier(n_estimators=1000).fit(X_train, y_train)
        self.progressBar.setValue(90)
        self.rfc_pred = self.rfc.predict(X_test)
        self.progressBar.setValue(100)
        return tf_idf_model


    
    def submit(self,tf_idf_model):
        self.dic ={0:'مثبت',1:'منفی'}
        self.final_text=self.showtext.toPlainText()
        self.sample = tf_idf_model.transform([self.final_text]).toarray()
        self.sentiment = self.rfc.predict(self.sample)
        self.final_text, self.dic[self.sentiment[0]]
        
    def cleaning(self):
        self.showtext.clear()
        self.textEdit.clear()
        self.mosbat.setValue(0)
        self.manfi.setValue(0)
        
    def browsefile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'text File', '.' , 'text file(*.txt)')
        f = open(fileName, 'r', encoding='utf-8')
        self.showtext.append(f.read())
        f.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hossein Fallah NLP"))
        self.pardazesh.setText(_translate("MainWindow", "پردازش"))
        self.pardazesh.clicked.connect(self.submit)
        self.label.setText(_translate("MainWindow", "بعد از آماده سازی سیستم متن خود جهت پردازش را وارد نمایید"))
        self.browse.setText(_translate("MainWindow", "پیدا کردن فایل"))
        self.browse.clicked.connect(self.browsefile)
        self.clean.setText(_translate("MainWindow", "پاکسازی"))
        self.clean.clicked.connect(self.cleaning)
        self.Preparation.setText(_translate("MainWindow", "آماده سازی"))
        self.Preparation.clicked.connect(self.prepare)
        self.mosbat_lable.setText(_translate("MainWindow", "نتیجه مثبت"))
        self.manfi_lable.setText(_translate("MainWindow", "نتیجه منفی"))
        self.label_2.setText(_translate("MainWindow", "نتیجه پردازش متن:"))
        self.actiondfs.setText(_translate("MainWindow", "dfs"))
        self.actionfs.setText(_translate("MainWindow", "fs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
