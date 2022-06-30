import mysql.connector

class user(object):

    user_id = 0
    new_user is None
    #Private variables
    __id = 0
    __username = ""
    __email = ""

    #QUERY self.user_id from DB and set all instance variables
    #e.g. self.name = row['name']
    db = mysql.connector.connect(host ='localhost',
                                 database = 'gamiccount',
                                 user= 'main',
                                 password = 'pynative@#29')

    #creating a Cursor Object
    cursor = db.cursor()

    def __init__(self,user_id):
        if user_id == -1:
            self.new_user is None
        else:
            self.new_user is not None
        pass

    def delete(self):
        if self.new_user is None:
            return False
        pass

    #This function populates new user data
    def _populate(self):

        # For adding new users
        mySql_insert_query = """INSERT INTO user(id, name, email, registered_date)
                                VALUES  (%s, %s, %s, %s)"""

        try:
            record = (id, name,email,registered_date)
            #Key in SQL commands to insert new data with variables
            cursor.execute(mySql_insert_query,record)
            #saves DB state
            user.commit()
            #Closes cursor
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to create user {}".format(error))

        finally:
            if db.is_connected():
                cursor.close()
                db.close()
                print("Account Created.")

        pass

    def commit(self):
        db.commit()
     pass