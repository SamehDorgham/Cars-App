from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

import sys
import os
from os import path

import mysql.connector
from mysql.connector import errorcode

form_class, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))


class MainApp(QMainWindow, form_class):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUI()
        self.Handel_buttons()
        self.Handel_DataBase_Connection()

    def InitUI(self):
        self.setWindowTitle("برنامج إدارة السيارات")
        self.tabWidget.tabBar().setVisible(False)

    def Handel_DataBase_Connection(self):

        try:
            self.cnx = mysql.connector.connect(user='root', password='',
                                               host='127.0.0.1',
                                               database='mydb')
            self.cursor = self.cnx.cursor()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        # else:
        #   cnx.close()

    def Handel_buttons(self):
        self.btn_Add_Car_Info.clicked.connect(self.Add_Car_Info)
        self.btn_Update_Car_Info.clicked.connect(self.Update_Car_Info)
        self.btn_Delete_Car_Info.clicked.connect(self.Delete_Car_Info)

        self.btn_Add_Fuel_Info.clicked.connect(self.Update_Fuel_Info)
        self.btn_Update_Fuel_Info.clicked.connect(self.Update_Fuel_Info)

        self.btn_Add_Maintenance_Info.clicked.connect(self.Update_Maintenance_Info)
        self.btn_Update_Maintenance_Info.clicked.connect(self.Update_Maintenance_Info)

        self.btn_Add_Licence_Info.clicked.connect(self.Update_Licence_Info)
        self.btn_Update_Licence_Info.clicked.connect(self.Update_Licence_Info)

        self.btn_Add_Revenu_Info.clicked.connect(self.Update_Revenu_Info)
        self.btn_Update_Revenu_Info.clicked.connect(self.Update_Revenu_Info)

        self.btn_Add_Rent_Info.clicked.connect(self.Update_Rent_Info)
        self.btn_Update_Rent_Info.clicked.connect(self.Update_Rent_Info)

        self.btn_Add_ElectricityWater_Info.clicked.connect(self.Update_ele_water_Info)
        self.btn_Update_ElectricityWater_Info.clicked.connect(self.Update_ele_water_Info)

        self.btn_Search_For_CarData_By_CarNo.clicked.connect(self.Search)




    ###############################################################
    ############## Add Search Car ... For Every Tab ##############

    def Search(self):

        ######################## Tab 0 ###########################

        if self.listWidget.row(self.listWidget.currentItem()) == 0:

            sql = ''' SELECT * FROM car_info WHERE car_number = %s'''
            car_number = self.txt_Search_For_CarData_By_CarNo.text()

            self.cursor.execute(sql,[(car_number)])
            data = self.cursor.fetchall()

            for row in data:
                print(row)

                self.txt_Car_Car_Number.setText(str(row[1]))
                self.txt_Car_Owner_Company.setText(row[2])
                self.txt_Car_Branch.setText(row[3])
                self.cbo_Car_Service_Mode.setCurrentIndex(int(row[4]))
                self.txt_Car_Shaceh_Number.setText(row[5])
                self.txt_Car_Motor_Number.setText(row[6])
                self.cbo_Car_Fuel_Type.setCurrentIndex(int(row[7]))
                self.txt_Car_Car_Type.setText(row[8])
                self.txt_Car_Car_Model.setText(str(row[9]))
                self.txt_Car_Car_Load.setText(str(row[10]))
                self.txt_Car_Car_Wieght.setText(str(row[11]))
                self.txt_Car_Car_Shape.setText(row[12])
                self.txt_Car_Car_Color.setText(row[13])


        ######################## Tab 1 ###########################

        if self.listWidget.row(self.listWidget.currentItem()) == 1:

            sql = ''' SELECT * FROM fuel_info WHERE car_number = %s'''
            car_number = self.txt_Search_For_CarData_By_CarNo.text()

            self.cursor.execute(sql, [(car_number)])

            data = self.cursor.fetchall()

            for row in data:
                print(row)
                self.liter_number.setText(str(row[1]))
                self.meter_reading.setText(str(row[2]))
                self.tips.setText(str(row[3]))
                self.liter_price.setText(str(row[4]))
                self.lcdtotal_fuel.display((row[5]))




        ######################## Tab 2 ###########################

        if self.listWidget.row(self.listWidget.currentItem()) == 2:

            sql = ''' SELECT * FROM maintenance_info WHERE car_number = %s'''
            car_number = self.txt_Search_For_CarData_By_CarNo.text()

            self.cursor.execute(sql, [(car_number)])

            data = self.cursor.fetchall()

            for row in data:
                print(row)
                self.txt_engine_amra.setText(row[1])
                self.txt_mechanics.setText(row[2])
                self.txt_electricity.setText(row[3])
                self.txt_samkara.setText(row[4])
                self.txt_afsha.setText(row[5])
                self.txt_periodic_maintenance.setText(row[6])
                self.txt_cooling.setText(row[7])
                self.txt_glass.setText(row[8])
                self.txt_notes.setPlainText(row[9])





        ######################## Tab 3 ###########################


        if self.listWidget.row(self.listWidget.currentItem()) == 3:

            sql = ''' SELECT * FROM licence_info WHERE car_number = %s'''
            car_number = self.txt_Search_For_CarData_By_CarNo.text()

            self.cursor.execute(sql, [(car_number)])

            data = self.cursor.fetchall()

            for row in data:
                print(row)
                self.txt_annual_renew.setText(row[1])
                self.txt_newcar_licence.setText(row[2])
                self.txt_renew_permission.setText(row[3])
                self.txt_infraction_info.setText(row[4])
                self.txt_annual_infraction.setText(row[5])
                self.txt_stamping_receipts.setText(row[6])
                self.txt_withdrawn_licence.setText(row[7])
                self.txt_withdrawn_infraction.setText(row[8])



        ######################## Tab 4 ###########################

        if self.listWidget.row(self.listWidget.currentItem()) == 4:

            sql = ''' SELECT * FROM revenue_info WHERE car_number = %s'''
            car_number = self.txt_Search_For_CarData_By_CarNo.text()

            self.cursor.execute(sql, [(car_number)])

            data = self.cursor.fetchall()

            for row in data:
                print(row)

                self.txt_kohna_selling.setText(row[1])
                self.txt_insurance_compensation.setText(row[2])
                self.txt_accedint_compensation.setText(row[3])



        ######################## Tab 5 ###########################

        if self.listWidget.row(self.listWidget.currentItem()) == 5:

            sql = ''' SELECT * FROM rent_info WHERE car_number = %s'''
            car_number = self.txt_Search_For_CarData_By_CarNo.text()

            self.cursor.execute(sql, [(car_number)])

            data = self.cursor.fetchall()

            for row in data:
                print(row)
                self.txt_monthly_revenu.setText(row[1])
                self.txt_arab_ghofra.setText(row[2])




        ######################## Tab 6 ###########################

        if self.listWidget.row(self.listWidget.currentItem()) == 6:

            sql = ''' SELECT * FROM WAEL_info WHERE car_number = %s'''
            car_number = self.txt_Search_For_CarData_By_CarNo.text()

            self.cursor.execute(sql, [(car_number)])

            data = self.cursor.fetchall()

            for row in data:
                print(row)
                self.txt_electricity_expenses.setText(row[1])
                self.txt_water_expenses.setText(row[2])




    ###############################################################
    ############## Car Info  ##############

    # Add Car
    def Add_Car_Info(self):
        car_number = self.txt_Car_Car_Number.text()
        owner_company = self.txt_Car_Owner_Company.text()
        branch = self.txt_Car_Branch.text()
        service_mode = self.cbo_Car_Service_Mode.currentIndex()
        shaceh_number = self.txt_Car_Shaceh_Number.text()
        motor_number = self.txt_Car_Motor_Number.text()
        fuel_type = self.cbo_Car_Fuel_Type.currentIndex()
        car_type = self.txt_Car_Car_Type.text()
        car_model = self.txt_Car_Car_Model.text()
        car_load = self.txt_Car_Car_Load.text()
        car_weight = self.txt_Car_Car_Wieght.text()
        car_shape = self.txt_Car_Car_Shape.text()
        car_color = self.txt_Car_Car_Color.text()

        # Execute the SQL command
        self.cursor.execute("""INSERT INTO car_info(car_number,owner_company,branch,service_mode,shaceh_number,motor_number,fuel_type,car_type,car_model,car_load,car_weight,car_shape,car_color)
                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            car_number, owner_company, branch, service_mode, shaceh_number, motor_number, fuel_type, car_type,
            car_model, car_load, car_weight, car_shape, car_color))



        #Insert car_number into all Related Tables

        self.cursor.execute(""" INSERT INTO fuel_info(car_number)VALUES(%s)""",(car_number,))
        self.cursor.execute(""" INSERT INTO licence_info(car_number)VALUES(%s)""",(car_number,))
        self.cursor.execute(""" INSERT INTO maintenance_info(car_number)VALUES(%s)""", (car_number,))
        self.cursor.execute(""" INSERT INTO rent_info(car_number)VALUES(%s)""", (car_number,))
        self.cursor.execute(""" INSERT INTO revenue_info(car_number)VALUES(%s)""", (car_number,))
        self.cursor.execute(""" INSERT INTO WAEL_info(car_number)VALUES(%s)""", (car_number,))


        self.cnx.commit()

        print("Insertion Data Into DataBase Is Done")

        #Erase All Controls Contents

        self.txt_Car_Car_Number.setText("")
        self.txt_Car_Owner_Company.setText("")
        self.txt_Car_Branch.setText("")
        self.cbo_Car_Service_Mode.setCurrentIndex(0)
        self.txt_Car_Shaceh_Number.setText("")
        self.txt_Car_Motor_Number.setText("")
        self.cbo_Car_Fuel_Type.setCurrentIndex(0)
        self.txt_Car_Car_Type.setText("")
        self.txt_Car_Car_Model.setText("")
        self.txt_Car_Car_Load.setText("")
        self.txt_Car_Car_Wieght.setText("")
        self.txt_Car_Car_Shape.setText("")
        self.txt_Car_Car_Color.setText("")


        #Show Successfully Add Data into Tables on StatusBar

        self.statusbar.showMessage("تم إضافة المعلومات بنجاح")



    # Update Car

    def Update_Car_Info(self):

        car_number = self.txt_Car_Car_Number.text()

        owner_company = self.txt_Car_Owner_Company.text()
        branch = self.txt_Car_Branch.text()
        service_mode = self.cbo_Car_Service_Mode.currentIndex()
        shaceh_number = self.txt_Car_Shaceh_Number.text()
        motor_number = self.txt_Car_Motor_Number.text()
        fuel_type = self.cbo_Car_Fuel_Type.currentIndex()
        car_type = self.txt_Car_Car_Type.text()
        car_model = self.txt_Car_Car_Model.text()
        car_load = self.txt_Car_Car_Load.text()
        car_weight = self.txt_Car_Car_Wieght.text()
        car_shape = self.txt_Car_Car_Shape.text()
        car_color = self.txt_Car_Car_Color.text()

        # Execute the SQL command

        self.cursor.execute(
            """ UPDATE car_info SET car_number = %s,owner_company = %s,branch= %s,service_mode = %s,shaceh_number = %s,
            motor_number = %s,fuel_type = %s,car_type = %s,car_model = %s,car_load = %s,car_weight =%s,car_shape=%s,
            car_color=%s WHERE car_number=%s """,
            (car_number, owner_company, branch, service_mode, shaceh_number, motor_number, fuel_type, car_type,car_model, car_load, car_weight, car_shape, car_color,car_number))


        self.cnx.commit()



        # Erase All Controls Contents

        self.txt_Car_Car_Number.setText("")
        self.txt_Car_Owner_Company.setText("")
        self.txt_Car_Branch.setText("")
        self.cbo_Car_Service_Mode.setCurrentIndex(0)
        self.txt_Car_Shaceh_Number.setText("")
        self.txt_Car_Motor_Number.setText("")
        self.cbo_Car_Fuel_Type.setCurrentIndex(0)
        self.txt_Car_Car_Type.setText("")
        self.txt_Car_Car_Model.setText("")
        self.txt_Car_Car_Load.setText("")
        self.txt_Car_Car_Wieght.setText("")
        self.txt_Car_Car_Shape.setText("")
        self.txt_Car_Car_Color.setText("")

        # Show Successfully Add Data into Tables on StatusBar

        self.statusbar.showMessage("تم تعديل البيانات بنجاح")



    # Delete Car

    def Delete_Car_Info(self):

        car_number = self.txt_Search_For_CarData_By_CarNo.text()

        self.cursor.execute(""" DELETE FROM car_info WHERE car_number = %s""", (car_number,))

        self.cursor.execute(""" DELETE FROM fuel_info WHERE car_number = %s""", (car_number,))
        self.cursor.execute(""" DELETE FROM licence_info WHERE car_number = %s""", (car_number,))
        self.cursor.execute(""" DELETE FROM maintenance_info WHERE car_number = %s""", (car_number,))
        self.cursor.execute(""" DELETE FROM rent_info WHERE car_number = %s""", (car_number,))
        self.cursor.execute(""" DELETE FROM revenue_info WHERE car_number = %s""", (car_number,))
        self.cursor.execute(""" DELETE FROM WAEL_info WHERE car_number = %s""", (car_number,))

        self.cnx.commit()

        self.statusbar.showMessage("تم حذف البيانات بنجاح")

        # Erase All Controls Contents

        self.txt_Car_Car_Number.setText("")
        self.txt_Car_Owner_Company.setText("")
        self.txt_Car_Branch.setText("")
        self.cbo_Car_Service_Mode.setCurrentIndex(0)
        self.txt_Car_Shaceh_Number.setText("")
        self.txt_Car_Motor_Number.setText("")
        self.cbo_Car_Fuel_Type.setCurrentIndex(0)
        self.txt_Car_Car_Type.setText("")
        self.txt_Car_Car_Model.setText("")
        self.txt_Car_Car_Load.setText("")
        self.txt_Car_Car_Wieght.setText("")
        self.txt_Car_Car_Shape.setText("")
        self.txt_Car_Car_Color.setText("")



    ###############################################################
    ###############################################################
    ############## Fuel Info  ##############

    # Add Fuel

    def Update_Fuel_Info(self):

        car_number = self.txt_Search_For_CarData_By_CarNo.text()

        liter_number = float(self.liter_number.text())
        meter_reading = float(self.meter_reading.text())
        tips = float(self.tips.text())
        liter_price = float(self.liter_price.text())

        total = (liter_number * liter_price) + tips

        self.lcdtotal_fuel.display(total)

        # Execute the SQL command

        self.cursor.execute("""UPDATE fuel_info SET liter_number = %s,counter_reading = %s,tips = %s,liter_price = %s,total = %s WHERE car_number = %s""",(liter_number, meter_reading, tips, liter_price, total, car_number))

        self.cnx.commit()

        self.statusbar.showMessage("تم إضافة المعلومات بنجاح")




    ###############################################################
    ############## Maintenance Info  ##############


    def Update_Maintenance_Info(self):

        car_number = self.txt_Search_For_CarData_By_CarNo.text()

        engine_amra = self.txt_engine_amra.text()
        mechanics = self.txt_mechanics.text()
        electricity = self.txt_electricity.text()
        samkara = self.txt_samkara.text()
        afsha = self.txt_afsha.text()
        periodic_maintenance = self.txt_periodic_maintenance.text()
        cooling = self.txt_cooling.text()
        glass = self.txt_glass.text()
        notes = self.txt_notes.toPlainText()


        self.cursor.execute(""" UPDATE maintenance_info SET engine_amra = %s , mechanics = %s , electricity = %s ,samkara = %s , afsha = %s , periodic_maintenance = %s , cooling = %s , glass = %s , notes = %s WHERE car_number = %s """,
        (engine_amra , mechanics ,electricity , samkara , afsha , periodic_maintenance , cooling , glass , notes , car_number  ))

        self.cnx.commit()

        self.statusbar.showMessage("تم إضافة المعلومات بنجاح")







    ###############################################################
    ############## Licence Info  ##############



    def Update_Licence_Info(self):

        car_number = self.txt_Search_For_CarData_By_CarNo.text()

        annual_renew = self.txt_annual_renew.text()
        newcar_licence = self.txt_newcar_licence.text()
        renew_permission = self.txt_renew_permission.text()
        infraction_info = self.txt_infraction_info.text()
        annual_infraction = self.txt_annual_infraction.text()
        stamping_receipts = self.txt_stamping_receipts.text()
        withdrawn_licence = self.txt_withdrawn_licence.text()
        withdrawn_infraction = self.txt_withdrawn_infraction.text()

        self.cursor.execute(""" UPDATE licence_info SET annual_renew = %s ,newcar_licence = %s , renew_permission = %s ,infraction_info = %s , annual_infraction = %s , stamping_receipts = %s , withdrawn_licence = %s , withdrawn_infraction = %s WHERE car_number = %s """ ,
        (annual_renew , newcar_licence , renew_permission , infraction_info , annual_infraction ,stamping_receipts , withdrawn_licence , withdrawn_infraction , car_number))

        self.cnx.commit()

        self.statusbar.showMessage("تم إضافة المعلومات بنجاح")




    ###############################################################
    ############## Revenu Info  ##############


    def Update_Revenu_Info(self):

        car_number = self.txt_Search_For_CarData_By_CarNo.text()

        kohna_selling = self.txt_kohna_selling.text()
        insurance_compensation = self.txt_insurance_compensation.text()
        accedint_compensation = self.txt_accedint_compensation.text()

        self.cursor.execute(
            """ UPDATE revenue_info SET kohna_selling = %s ,insurance_compensation = %s , accedint_compensation = %s WHERE car_number = %s """,
            (kohna_selling, insurance_compensation, accedint_compensation , car_number))

        self.cnx.commit()

        self.statusbar.showMessage("تم إضافة المعلومات بنجاح")





    ###############################################################
    ############## Rent Info  ##############


    def Update_Rent_Info(self):

        car_number = self.txt_Search_For_CarData_By_CarNo.text()

        monthly_revenu = self.txt_monthly_revenu.text()
        arab_ghofra = self.txt_arab_ghofra.text()


        self.cursor.execute(
            """ UPDATE rent_info SET monthly_revenu = %s ,arab_ghofra = %s WHERE car_number = %s """,
            (monthly_revenu, arab_ghofra , car_number))

        self.cnx.commit()

        self.statusbar.showMessage("تم إضافة المعلومات بنجاح")

    ###############################################################
    ############## Electricity & Water Info  ##############


    def Update_ele_water_Info(self):

        car_number = self.txt_Search_For_CarData_By_CarNo.text()

        electricity_expenses = self.txt_electricity_expenses.text()
        water_expenses = self.txt_water_expenses.text()

        self.cursor.execute(
            """ UPDATE WAEL_info SET electricity_expenses = %s ,water_expenses = %s WHERE car_number = %s """,
            (electricity_expenses, water_expenses, car_number))

        self.cnx.commit()

        self.statusbar.showMessage("تم إضافة المعلومات بنجاح")



    ###############################################################


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
