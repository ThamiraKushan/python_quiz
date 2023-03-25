from connection import db_connection
import csv


class QuessionAnswer(object):

    def __init__(self):

        self.correct_ = 0
        self.incorrect_ = 0
        self.db_connection = db_connection
        self.cursor = self.db_connection.cursor()

        sql0 = "SELECT max(PaperTable_Id) FROM paper"
        self.cursor.execute(sql0)
        result = self.cursor.fetchone()
        # for item in result:
        #     self.LatestPaper = item[0]
        # print(result[0])
        self.LatestPaper= result[0]

    def Insert_Data(self):
        print("a")

        workbook_file = open(
            r"C:\Users\Shyamal\Desktop\msc it\4.1 Advanced Programming\Untitled Folder\upload.csv",
            "r",
        )
        workbook_reader = csv.reader(workbook_file)
        paper = []
        quession = []
        Answer = []
        current_quession = ""

        # create a cursor object
        cursor = db_connection.cursor()

        for i, row in enumerate(workbook_reader):
            if i < 1:

                # execute an INSERT statement
                sql1 = "INSERT INTO paper (Paper_No, Subject_Id) VALUES (%s, %s)"
                values = (row[1], row[3])
                cursor.execute(sql1, values)

                # get the last inserted id
                last_insert_id = cursor.lastrowid
            elif 1 < i:
                if current_quession != row[0]:

                    sql2 = "INSERT INTO queion (PaperTable_Id, Q_No,Quession) VALUES (%s, %s,%s)"
                    values = (last_insert_id, row[0], row[1])
                    cursor.execute(sql2, values)

                    last_Quession_id = cursor.lastrowid

                    current_quession = row[0]
                #       ass Insert Answer data
                sql3 = "INSERT INTO answer(QsTable_id_n,Answer_No,Answer,Is_Correct) VALUES(%s, %s,%s,%s)"

                values = (last_Quession_id, row[2], row[3], row[4])
                cursor.execute(sql3, values)

        workbook_file.close()

        # commit the transaction
        db_connection.commit()

        # close the cursor and database connection
        cursor.close()
        # db_connection.close()

    def InsertMaks(self,Maks,UserID):

        print("im in insertmask\\")
        print(Maks)
        print(UserID)
        for i,item in enumerate(self.ViewCorrectAnswer()):
            if item[8] == Maks[i]:
                self.correct_ += 1
            else:
                self.incorrect_ +=1 
        

        sql1 = "INSERT INTO marks (Student_id, Paper_id_n,Correct_Answers,Wrong_Answers) VALUES (%s, %s, %s, %s)"
        values = (UserID, self.LatestPaper,self.correct_,self.incorrect_)
        print(values)
        self.cursor.execute(sql1, values)

        self.db_connection.commit()

        # close the cursor and database connection
        self.cursor.close()
        # self.db_connection.close()

      
        

    def ViewCorrectAnswer(self):
        # sql = "select * from queion"

        # Define the SQL query
        query = "select * from queion q \
                INNER JOIN answer ans on q.QsTable_id_n = ans.QsTable_id_n \
                WHERE ans.Is_Correct=1"
        cursor = db_connection.cursor()
        # Execute the query
        cursor.execute(query)

        # Fetch the results
        results = cursor.fetchall()

        # Process the results
        # for row in results:
            # Do something with each row of data
            # print(row)

        # Close the cursor and connection
        # cursor.close()
        # db_connection.close()

        return results
    
    def ViewStudentsMarks(self,StudentID):
        # sql = "select * from queion"

        # Define the SQL query
        query = f"select * from marks where Student_id={StudentID} AND Paper_id_n ={self.LatestPaper}"
        # cursor = db_connection.cursor()
        # Execute the query
        self.cursor.execute(query)

        # Fetch the results
        results = self.cursor.fetchall()

        # Process the results
        # for row in results:
        #     # Do something with each row of data
        #     print(row)

        # Close the cursor and connection
        self.cursor.close()
        # db_connection.close()

        return results

    def quiz(self):
        # Define the SQL query
        query = "select q.QsTable_id_n,q.PaperTable_Id,q.Q_No,q.Quession,ans.Answer_Id,ans.Answer_No,Answer,Is_Correct\
                from queion q \
                INNER JOIN answer ans on q.QsTable_id_n = ans.QsTable_id_n\
                where  q.PaperTable_Id = (SELECT MAX(PaperTable_Id) FROM paper )\
                order by q.PaperTable_Id,ans.Answer_Id"
        cursor = db_connection.cursor()
        # Execute the query
        cursor.execute(query)

        # Fetch the results
        results = cursor.fetchall()

        # Process the results
        # for row in results:
        #     # Do something with each row of data
        #     print(row)

        # Close the cursor and connection
        cursor.close()
        # db_connection.close()

        return results
