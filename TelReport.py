import sys
from PyQt5 import QtWidgets
import reportUI
import datetime
import pyodbc
import pandas

INITDATE = datetime.date(1899, 12, 30)


class ReportApp(QtWidgets.QMainWindow, reportUI.Ui_Form):

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.startDateUI.dateChanged.connect(self.correct_date2)
        self.saveButtonUI.clicked.connect(self.get_report)

    def correct_date2(self):
        self.endDateUI.setDate(self.startDateUI.date())

    def get_report(self):

        date1qt = self.startDateUI.date()
        date2qt = self.endDateUI.date()

        date1 = date1qt.toPyDate()
        date2 = date2qt.toPyDate()

        archidate1 = date1 - INITDATE
        archidate2 = date2 - INITDATE

        conn = pyodbc.connect(
                                'Driver={SQL Server};'
                                'Server=192.168.88.250;'
                                'Database=ArchiMed;'
                                'Trusted_Connection=no;'
                                'UID=reporter;'
                                'PWD=HCreporter1'
                                )

        report_query_from_ecalls = '''
                            select
                                dbo.FormatDateTime('dd.MM.yyyy',
                                e.CREATIONDATETIME) as  'Дата',
                                dbo.FormatDateTime('hh:mm',
                                e.CREATIONDATETIME) as  'Время',
                                u.NAME              as  'Принял',
                                e.PHONENUMBER       as  'Номер телефона',
                                e.FULLNAME          as  'Ф.И.О. пациента',
                                i.NAME              as  'Источник информации',
                                ecp.NAME            as  'Результат переговоров',
                                --rt.NAME           as  'Тип обращения',
                                e.INFO              as  'Примечание',
                                ecaqs.ANSWER        as  'Направление'                                                           
                            from
                                ENTERING_CALLS e                                                           
                            left join
                                USERS u                   
                                    on  u.id=e.GETUSERID                                                          
                            left join
                                INFORMATION_SOURCES i     
                                    on  i.ID=e.INFORMATIONSOURCE                                                          
                            left join
                                ENTERING_CALL_PURPOSE ecp 
                                    on  ecp.ID=e.CALLPURPOSE                                                          
                            left join
                                RECEPTION_TYPES rt        
                                    on  rt.ID=e.TYPERECEPTION                                                          
                            left join
                                (
                                    select
                                        *                                                                                           
                                    from
                                        ENTERING_CALLS_ADDITIONAL_QUESTION ecaq                                                                                          
                                    where
                                        ecaq.QUESTIONID=2                                                                                  
                                )ecaqs                                              
                                    on ecaqs.CALLID=e.ID                                                           
                            where
                                FLOOR(e.CREATIONDATETIME) between {0} and {1}                                                                          
                                AND e.ENABLED=1 
                            '''.format(archidate1.days, archidate2.days)

        report_query_from_talons = '''
                            WITH Numbered AS 
                            (
                                SELECT
                                    *,
                                    ROW_NUMBER() OVER (PARTITION BY t.MCID ORDER BY t.NUMBER) rn
                                FROM
                                    TALONS t
                                WHERE
                                    floor(CREATIONDATETIME) BETWEEN {0} AND {1}
                            )
                            SELECT 
                                n.NUMBER 
                                    AS 'номер талона',
                                dbo.FormatDateTime('dd.MM.yyyy', CREATIONDATETIME) 
                                    AS 'дата создания талона',
                                mc.NUMBER 
                                    AS 'номер карты',
                                mc.FULLNAME 
                                    AS 'пациент',
                                d.FULLNAME 
                                    AS 'врач',
                                dt.NAME 
                                    AS 'специальность',
                                ins.NAME
                                    AS 'источник информации',  
                                n.INFO 
                                    AS 'комментарий'
                            FROM 
                                Numbered n
                            LEFT JOIN
                                MEDCARDS mc 
                                    ON mc.ID=n.MCID
                            LEFT JOIN
                                DOCTORS d 
                                    ON d.ID=n.DOCID
                            LEFT JOIN
                                DOCTORTYPES dt 
                                    ON  dt.ID=d.TYPE
                            LEFT JOIN
                                INFORMATION_SOURCES ins
                                    ON ins.ID=n.INFORMATIONSOURCE
                            WHERE
                                n.rn=1
                                --AND mc.CREATIONDATE BETWEEN 43952 AND 43982
                                AND mc.CREATIONDATE BETWEEN {0} AND {1}
                            ORDER BY
                                n.ID
                            '''.format(archidate1.days, archidate2.days)

        pandas.read_sql(report_query_from_ecalls, conn).to_excel(
            'Отчет по телефонии (звонки) с {0} по {1}.xlsx'.format(date1, date2), index=False)
        pandas.read_sql(report_query_from_talons, conn).to_excel(
            'Отчет по телефонии (талоны) с {0} по {1}.xlsx'.format(date1, date2), index=False)
        self.errorLabelUI.setText('OK')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ReportApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
