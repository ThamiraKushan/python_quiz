from connection import db_connection
import csv


class QuessionAnswer(object):

    def __init__(self, User_ID):

        self.User_ID = User_ID
        self.db_connection = db_connection
        self.cursor = self.db_connection.cursor()

        sql0 = "SELECT max(PaperTable_Id) FROM paper"
        self.cursor.execute(sql0)
        result = self.cursor.fetchone()
        # for item in result:
        #     self.LatestPaper = item[0]
        # print(result[0])
        self.LatestPaper = result[0]
        # print(self.User_ID)

    def Insert_Data(self, filepath):
        print("a")
        file_Path = filepath
        workbook_file = open(file_Path, "r")
        workbook_reader = csv.reader(workbook_file)
        paper = []
        quession = []
        Answer = []
        current_quession = ""

        # create a cursor object
        cursor = db_connection.cursor()
        try:
            for i, row in enumerate(workbook_reader):
                if i < 1:

                    # execute an INSERT statement
                    sql1 = "INSERT INTO paper (Paper_No, Subject_Name) VALUES (%s, %s)"
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
            # commit the transaction
            db_connection.commit()
            # return a success message
            return "Data inserted successfully."
        except Exception as e:
            # rollback the changes if there was an error
            db_connection.rollback()

            # return a reject message with the error information
            # return f"Error inserting data: {str(e)}"
            return f"Incorrect file format! Please select a correctly formatted file."

        workbook_file.close()
        print("as")
        # close the cursor and database connection
        cursor.close()

    def InsertMaks(self, correct_, incorrect_, Paper_Id):

        print("im in insertmask\\")

        try:

            sql1 = "INSERT INTO marks (Student_id, Paper_id_n,Correct_Answers,Wrong_Answers) VALUES (%s, %s, %s, %s)"
            values = (self.User_ID, Paper_Id, correct_, incorrect_)
            # print(values)
            self.cursor.execute(sql1, values)

            self.db_connection.commit()

            # close the cursor and database connection
            self.cursor.close()
            return "Data inserted successfully."
        except Exception as e:
            # rollback the changes if there was an error
            db_connection.rollback()

            # return a reject message with the error information
            # return f"Error inserting data: {str(e)}"
            return f"Incorrect file format! Please select a correctly formatted file."
            # self.db_connection.close()

    def ViewCorrectAnswer(self, Paper_Id):

        # Define the SQL query
        query = f"select * from queion q \
                INNER JOIN answer ans on q.QsTable_id_n = ans.QsTable_id_n \
                WHERE ans.Is_Correct=1 and q.PaperTable_Id = {Paper_Id} "

        print(query)
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

    def ViewStudentsMarks(self, StudentID, Paper_Id):
        # sql = "select * from queion"

        # Define the SQL query
        print(StudentID)
        query = f"select * from marks where Student_id={StudentID} AND Paper_id_n ={Paper_Id}"
        print(query)
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

    def quiz(self, Paper_Id):
        # Define the SQL query
        query = f"select q.QsTable_id_n,q.PaperTable_Id,q.Q_No,q.Quession,ans.Answer_Id,ans.Answer_No,Answer,Is_Correct\
                from queion q \
                INNER JOIN answer ans on q.QsTable_id_n = ans.QsTable_id_n\
                where  q.PaperTable_Id = {Paper_Id}"
        cursor = db_connection.cursor()
        # Execute the query
        cursor.execute(query)

        # Fetch the results
        results = cursor.fetchall()
        # print(query)
        cursor.close()
        # db_connection.close()

        return results

    def ActivePaper(self):
        # Define the SQL query
        query = "select * from paper where Active=1"
        cursor = db_connection.cursor()
        # Execute the query
        cursor.execute(query)

        # Fetch the results
        results = cursor.fetchall()

        cursor.close()
        # db_connection.close()

        return results

    def IsComplted(self, Paper_Id):
       # Define the SQL query
        query = f"SELECT CASE WHEN EXISTS (SELECT * FROM marks where Student_id={self.User_ID} and Paper_id_n={Paper_Id}) THEN 1 ELSE 0 END AS hasRecords"

        cursor = db_connection.cursor(dictionary=True)

        # Execute the query
        cursor.execute(query)

        # Fetch the results
        results = cursor.fetchone()

        cursor.close()
        # db_connection.close()

        return results['hasRecords']
