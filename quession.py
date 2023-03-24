from connection import db_connection
import csv


class QuessionAnswer(object):
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
        db_connection.close()

    def ViewData(self):
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
        for row in results:
            # Do something with each row of data
            print(row)

        # Close the cursor and connection
        cursor.close()
        db_connection.close()

        return results

    def quiz(self):
        # Define the SQL query
        query = "select q.QsTable_id_n,q.PaperTable_Id,q.Q_No,q.Quession,ans.Answer_Id,ans.Answer_No,Answer,Is_Correct from queion q INNER JOIN answer ans on q.QsTable_id_n = ans.QsTable_id_n"
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
        db_connection.close()

        return results
