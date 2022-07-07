import os


# creating a class customer which stores all the details of a user/customer
class customer:
    name = str()
    customer_id = int()
    dob = str()

    phone_no = 0
    account_creation_date = str()
    password = str()
    confirm_password = str()

    def set_data(self):
        pass
        self.name = input("Enter your name :\n")
        self.dob = input("Enter your date of birth :\n")
        self.phone_no = input("Enter your phone no :\n")

        # this function is for checking the length of phone no and re enter if invalid
        if len(str(self.phone_no)) != 10:
            while len(str(self.phone_no)) != 10:
                self.phone_no = input(" please enter a valid  phone no of 10 digits:\n")

        # getting values from user
        self.account_creation_date = input("Enter today's date or account creation date :\n")
        self.password = input("Enter your password\n")
        self.confirm_password = input("Renter your password to confirm\n")

        # checking the validity of confirm_password
        if self.password != self.confirm_password or len(self.password) < 6:
            while self.password != self.confirm_password or len(self.password) < 6:
                if len(self.password) < 6:
                    print("Your confirm_password requirement is minimum 6 characters ")

                else:
                    print("Your both the passwords do not match please try again !!!\n")
                self.password = input("Enter your confirm_password\n")
                self.confirm_password = input("Renter your  password to confirm\n")

        self.create_account()

    # function to enter data of user in file
    def create_account(self):

        customer_data = open("customer data file", "a")
        self.customer_id = generate_customer_id()
        customer_data.write(
            f"{self.customer_id}@{self.password}@{self.name}@{self.dob}@{self.phone_no}@{self.account_creation_date}@\n")

        print("your account is created successfully")
        print("your customer id is : ", self.customer_id)


#          class to store admin details
class admin(customer):
    username = str()

    def check_username(self):
        self.username = input("please enter a unique username for you\n")
        try:
            admin_data = open("admin data")
        except:
            admin_data = open("admin data", "a+")
        finally:

            admin_data_string = admin_data.readline()

            while admin_data_string != "":

                admin_data_list = admin_data_string.split("@")
                if admin_data_list[0] == self.username:
                    print("username has been already used please try with another username")
                    return False
                admin_data_string = admin_data.readline()

            return True

    def create_account(self):
        flag = self.check_username()

        while flag != True:
            flag = self.check_username()

        if self.check_username():
            admin_data = open("admin data", "a")
            admin_data.write(f"{self.username}@{self.password}@{self.name}@{self.dob}@{self.phone_no}@"
                             f"{self.account_creation_date}@\n")
            admin_data.close()
            print("admin account created successfully ")


#   Creating a class book which can store details of each book specifically
class books:
    book_name = str()
    book_serial_no = int()
    book_author_name = str()
    date_of_registration = str()

    def set_book_data(self):
        self.book_name = input("Enter the name of book\n")
        self.book_author_name = input("enter the author name\n")
        self.date_of_registration = input("Enter the date for registration of this book\n")
        self.add_book()

    def add_book(self):
        book_data = open("library books", "a")
        book_data1 = open("available books", "a")
        book_record = open("book records", "a")

        self.serial_id = generate_serial_id()
        book_data.write(f"{self.book_name}%{self.serial_id}%{self.book_author_name}%{self.date_of_registration}%\n")
        book_data1.write(f"{self.book_name}%{self.serial_id}%{self.book_author_name}%{self.date_of_registration}%\n")
        book_record.write(f"{self.book_name}%{self.serial_id}%book added to library \n")

        print("your book is added successfully")
        print("serial id  of this book is : ", self.serial_id)

        book_data.close()
        book_data1.close()
        book_record.close()


# ******************************      CREATING VARIOUS FUNCTIONS
# *************************************************


# function created to generate a unique customer id for every new customer          *************************************
def generate_customer_id():
    customer_data = open("customer data file")
    customer_id = 1
    while customer_data.readline() != "":
        customer_id += 1

    customer_data.close()
    return customer_id


# function to get the data of users           *********************************************************
def get_data(id):
    customer_data = open("customer data file")
    customer_data_string = customer_data.readline()

    while customer_data_string != "":
        customer_data_list = customer_data_string.split("@")

        if customer_data_list[0] == str(id):
            print(f'''customer name : {customer_data_list[2]}
customer date of birth : {customer_data_list[3]}
customer phone no : {customer_data_list[4]}
customer account creation date : {customer_data_list[5]}\n''')

            customer_data.close()
            break
        customer_data_string = customer_data.readline()


def get_all_user_data():
    customer_data = open("customer data file")
    customer_data_string = customer_data.readline()

    while customer_data_string != "":
        customer_data_list = customer_data_string.split("@")

        print(f'''customer name : {customer_data_list[2]}
customer date of birth : {customer_data_list[3]}
customer phone no : {customer_data_list[4]}
customer account creation date : {customer_data_list[5]}\n''')

        customer_data_string = customer_data.readline()
        customer_data.close()


# function to generate a unique id for all the books        *****************************************************
def generate_serial_id():
    book_data = open("library books", "a")
    book_data.close()

    book_data = open("library books")
    serial_id = 1
    while book_data.readline() != "":
        serial_id += 1

    book_data.close()
    return serial_id


# ******************              function to check if user exists in file or not          ***************************
def check_login(customer_id, customer_password):
    customer_data = open("customer data file", "r")
    customer_id = str(customer_id)
    line_data = customer_data.readline()
    data_list = line_data.split("@")

    while line_data != "":

        if data_list[0] == customer_id and data_list[1] == customer_password:
            print("you are logged in")
            return True

        line_data = customer_data.readline()
        data_list = line_data.split("@")

    print("invalid username or confirm_password !!!")
    return False


# Function to check if specific book is available in library or not
def check_book_available(serial_id):
    book_data1 = open("available books")
    data_string = book_data1.readline()

    while data_string != "":
        data_list = data_string.split("%")

        if data_list[1] == serial_id:
            print("hurray the book is available in library")
            return True
        data_string = book_data1.readline()

    return False


# function to issue a book to any user after logging in
def issue_book(serial_id, customer_id):
    print("entered in issue books")
    available_books = open("available books")
    raw_available_books = open("raw available books", "a+")
    issued_books = open("issued books", "a+")
    costumer_issued_book_data = open("costumer issued book data", 'a+')
    book_name = str()
    book_record = open("book records", "a")

    if check_book_available(serial_id):

        available_books_string = available_books.readline()
        available_books_list = available_books_string.split("%")
        date_of_issuing = input("Enter the date of issuing this book\n")

        while available_books_string != "":
            if available_books_list[1] == str(serial_id):
                book_name = available_books_list[0]
                issued_books.write(available_books_string)
                book_record.write(f"{book_name}%{serial_id}%book issued to user id {customer_id}%\n")

            else:
                raw_available_books.write(available_books_string)

            available_books_string = available_books.readline()
            available_books_list = available_books_string.split("%")

        available_books.close()
        raw_available_books.close()
        book_record.close()

        os.remove("available books")
        os.renames("raw available books", "available books")

        costumer_issued_book_data.write(f"{customer_id}%{book_name}%{date_of_issuing}%{serial_id}%\n")

        print("The book has been issued successfully")

    else:
        print("The book has been issued already ")


#  3 in one function to check the list of total books registered in library , available books at the time , issued books
def see_all_books(number=1):
    if number == 1:
        books_data = open("available books")
    elif number == 2:
        books_data = open("issued books")

    elif number == 3:
        books_data = open("library books")

    book_string = books_data.readline()

    while book_string != "":
        book_list = book_string.split("%")
        print(f"Name of book : {book_list[0]}\nAuthor name : {book_list[2]}\nSerial no : {book_list[1]}\n")
        book_string = books_data.readline()


#    Function to return a book           *************************************************************
def return_book(customer_id):
    serial_id = input("please enter the serial no. of book you wanted to return\n")

    issued_books = open("issued books")
    raw_issued_books = open("raw issued books", "a")
    available_books = open("available books", "a")
    issued_books_string = issued_books.readline()
    book_record = open("book records", "a")

    while issued_books_string != "":
        issued_books_list = issued_books_string.split("%")

        if issued_books_list[1] == serial_id:
            available_books.write(issued_books_string)
            book_record.write(f"{issued_books_list[0]}%{serial_id}%book returned by user")

        else:
            raw_issued_books.write(issued_books_string)

        issued_books_string = issued_books.readline()

    issued_books.close()
    raw_issued_books.close()
    available_books.close()
    book_record.close()

    os.remove("issued books")
    os.renames("raw issued books", "issued books")

    customer_issued_data = open("costumer issued book data")
    raw_customer_issued_data = open("raw costumer issued book data", "a")

    customer_issued_data_string = customer_issued_data.readline()

    while customer_issued_data_string != "":

        customer_issued_data_list = customer_issued_data_string.split("%")

        if customer_issued_data_list[3] != serial_id:
            raw_customer_issued_data.write(customer_issued_data_string)
        customer_issued_data_string = customer_issued_data.readline()

    raw_customer_issued_data.close()
    customer_issued_data.close()
    os.remove("costumer issued book data")
    os.renames("raw costumer issued book data", "costumer issued book data")

    print("your book has been returned successfully")


#      function to check all the books issued by the user      ***********************************************
def get_issued_books(id, usage=0, password=""):
    customer_issued_book_data = open("costumer issued book data")
    print("showing the issued books : \n ")
    line_no = 0
    index = 0

    while True:

        customer_issued_book_data_string = customer_issued_book_data.readline()
        customer_issued_book_data_list = customer_issued_book_data_string.split("%")

        if customer_issued_book_data_list[0] == str(id):
            print(customer_issued_book_data_list[1])
            print("Date of issuing : ", customer_issued_book_data_list[2] + "\n")
            index = 1
        if customer_issued_book_data_string == "":
            break

    if index != 1 and usage == 0:
        print("you havent issued any book !!!")

    #   Function to check if there are any books issued under the name of user
    if usage != 0 and index == 1:
        print("Failed to delete your account \n"
              "You have some books issued under your name first return it then try later")
        return False

    elif usage != 0 and index != 1:
        print("processing your account details..........")

        raw_password = input("please re-enter your confirm_password to CONFIRM \n")

        if raw_password == password:
            customer_issued_book_data.close()
            print("confirm_password check done")
            return True
    customer_issued_book_data.close()


# ***********     Function to delete the account of the user **********************
def delete_account(id):
    id = str(id)
    data_file = open("customer data file")
    raw_data_file = open("raw customer data file", "a")

    data_string = data_file.readline()

    while data_string != "":
        data_list = data_string.split("@")

        if data_list[0] != id:
            raw_data_file.write(data_string)
        data_string = data_file.readline()

    raw_data_file.close()
    data_file.close()

    os.remove("customer data file")
    os.renames("raw customer data file", "customer data file")

    print("Your account has been deleted successfully")


# function to check the login of the admin
def check_admin_login():
    admin_username = input("enter your username\n")
    admin_password = input("enter your confirm_password\n")

    customer_data = open("admin data", "r")
    line_data = customer_data.readline()
    data_list = line_data.split("@")

    while line_data != "":

        if data_list[0] == admin_username and data_list[1] == admin_password:
            print("you are logged in")
            return True
        else:
            print("confirm_password mismatch")
        line_data = customer_data.readline()
        data_list = line_data.split("@")

    print("invalid username or confirm_password !!!")
    return False


def create_all_files():
    file1 = open("customer data file", "a+")
    file2 = open("library books", "a+")
    file3 = open("issued books", "a+")
    file4 = open("available books", "a+")
    file5 = open("admin data", "a+")
    file6 = open("costumer issued book data", "a+")
    file7 = open("book records", "a+")

    file6.close()
    file5.close()
    file4.close()
    file3.close()
    file2.close()
    file1.close()
    file7.close()


def get_book_records():
    book_record = open("book records")
    records_string = book_record.readline()

    while records_string != "":
        record_list = records_string.split("%")
        print(f'''Book name : {record_list[0]}
Serial id : {record_list[1]}
status : {record_list[2]}\n''')
        records_string = book_record.readline()

    book_record.close()


# **********************************************   MAIN PROGRAM REGION   ************************************************
print("welcome to the library management system")
create_all_files()

while True:

    buffer = input("Press any key to continue")
    print('''\nENTER your choice 
    1. create a customer account in library 
    2. login to your account 
    3. Add book to library 
    4. see all the available books in library 
    5. ADMIN LOGIN
    PLEASE ENTER "0" TO EXIT !!!
    ''')

    first_choice = int(input())

    if first_choice == 1:

        user = customer()
        user.set_data()

        del user

    elif first_choice == 2:

        print("please enter your customer id")
        customer_id1 = input()
        print("please enter your confirm_password")
        customer_password = input()

        if (check_login(customer_id1, customer_password)):

            while True:

                buffer = input("Press any key to continue")
                print('''\nEnter your choice 
                    1. see your account details
                    2. issue a book for your self
                    3. see all issued books by you
                    4. return a book 
                    5. delete your account
                    6. see available books
                    7. update your details
                    8. change your confirm_password
                    PRESS '0' to LOGOUT 
                    ''')

                second_choice = int(input())

                if second_choice == 1:
                    get_data(customer_id1)

                elif second_choice == 2:
                    serial_id1 = input("enter the serial id of book\n")
                    issue_book(serial_id1, customer_id1)

                elif second_choice == 3:
                    get_issued_books(customer_id1)

                elif second_choice == 4:
                    return_book(customer_id1)


                elif second_choice == 5:
                    if get_issued_books(customer_id1, 1, customer_password):
                        delete_account(customer_id1)
                        break

                elif second_choice == 6:
                    see_all_books()
                    break

                elif second_choice == 0:
                    break

                else:
                    print("please enter a valid choice")

    elif first_choice == 3:
        book1 = books()
        book1.set_book_data()
        del book1

    elif first_choice == 4:
        see_all_books()

    elif first_choice == 5:
        print('''
        1. sign up/create acoount  
        2. login
        PRESS "0" to go back''')

        third_choice = int(input())

        if third_choice == 1:
            admin1 = admin()
            admin1.set_data()

            del admin1

        elif third_choice == 2:

            if check_admin_login():
                while True:
                    print('''Enter your choice :
                    1. see the details of all the users
                    2. issue a book for user
                    3. see all the books registered in library
                    4. see all the books issued to customers currently
                    5. see records of all the books

                    PRESS "0" TO EXIT / LOGOUT
                    ''')

                    fourth_choice = int(input())

                    if fourth_choice == 1:
                        get_all_user_data()

                    elif fourth_choice == 2:
                        pass

                        serial_id = input("enter the book serial id\n")
                        customer_id = input("enter the book customer id\n")

                        issue_book(serial_id, customer_id)

                    elif fourth_choice == 3:
                        see_all_books(3)

                    elif fourth_choice == 4:
                        see_all_books(2)

                    elif fourth_choice == 5:
                        get_book_records()

                    elif fourth_choice == 0:
                        break
                    else:
                        print("Enter a valid choice")

        elif third_choice == 0:
            break
        else:
            print("enter a valid choice")


    elif first_choice == 0:
        break

    else:
        print("please enter a valid option")
