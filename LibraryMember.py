# Python Programme to make a library database managament system from member side
# Importing Libraries
import pymysql as psql;
import datetime as dt;
import random as ran;
import matplotlib.pyplot as mat;
import time as time;
import tkinter as tki;

def titleScreen():
    "Function For clearing the screen and displaying title";
    for widgets in mainFrame.winfo_children():
        widgets.destroy();
    mainTitle = tki.Label(text = 'Astrata Library', font = 20);
    mainTitle.place(relx = 0.25, rely = 0.08, relheight = 0.05, relwidth = 0.5);    

def logInProcess(windowToGo = 'mainWindow', usernameH = None, passwordH = None, second = False):
    "Function For Log In Screen";
    def forgetPassword():
        titleScreen(); 
        def activate():
            backUpMatch = False;
            def change():
                newpasswordset = newpasswordsetEnt.get();
                setNewpasswordset = setNewpasswordsetEnt.get();
                
                if(newpasswordset != setNewpasswordset):
                    bookNameLbl = tki.Label(text = 'Passwords doesn\'t match');
                    bookNameLbl.place(relx = 0.3, rely = 0.8, relheight = 0.05, relwidth = 0.4);
                else:
                    cmd = 'UPDATE Members SET passwords = (%s) WHERE member_name = (%s)';
                    arg = (setNewpasswordset, userName);
                    cursor.execute(cmd, arg);
                    connection.commit();
                    logInProcess();
                    
            userName = usernameEnt.get();
            backUpCodes = backUpCodesEnt.get();
            backUpCodes = int(backUpCodes);
            
            cmd = 'SELECT buc_1, buc_2, buc_3, buc_4 FROM backUpCodes WHERE member_name = (%s)';
            arg = (userName);
            cursor.execute(cmd, arg);
            bucFetched = cursor.fetchone();
            if(bucFetched == None):
                bookNameLbl = tki.Label(text = 'No Backup Codes');
                bookNameLbl.place(relx = 0.3, rely = 0.8, relheight = 0.05, relwidth = 0.4);
            else:
                cmd = 'SELECT buc_1, buc_2, buc_3, buc_4 FROM backUpCodes WHERE member_name = (%s)';
                arg = (userName);
                cursor.execute(cmd, arg);
                bucFetched = cursor.fetchall();  
                bucFetched = bucFetched[0];
                for item in bucFetched:
                    if(item == backUpCodes):
                        backUpMatch = True; 
                        break;
                    
                if(backUpMatch == True):
                    titleScreen();
                    newpasswordsetLbl = tki.Label(mainFrame, text = 'Set New Password');
                    newpasswordsetLbl.place(relx = 0.09, rely = 0.3, relheight = 0.05, relwidth = 0.4);
                    newpasswordsetEnt = tki.Entry(mainFrame);
                    newpasswordsetEnt.place(relx = 0.4, rely = 0.3, relheight = 0.05, relwidth = 0.4);
                    
                    setNewpasswordsetLbl = tki.Label(mainFrame, text = 'Re-enter New Password');
                    setNewpasswordsetLbl.place(relx = 0.06, rely = 0.5, relheight = 0.05, relwidth = 0.4);
                    setNewpasswordsetEnt = tki.Entry(mainFrame);
                    setNewpasswordsetEnt.place(relx = 0.4, rely = 0.5, relheight = 0.05, relwidth = 0.4);
                    
                    changebtn = tki.Button(mainFrame, text = 'Change', command = change);
                    changebtn.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);
                    
                else:
                    bookNameLbl = tki.Label(text = 'Codes doesn\'t match');
                    bookNameLbl.place(relx = 0.3, rely = 0.8, relheight = 0.05, relwidth = 0.4);                    

        usernameLbl = tki.Label(mainFrame, text = 'Username');
        usernameLbl.place(relx = 0.1, rely = 0.3, relheight = 0.05, relwidth = 0.4);
        usernameEnt = tki.Entry(mainFrame);
        usernameEnt.place(relx = 0.4, rely = 0.3, relheight = 0.05, relwidth = 0.4);

        backUpCodeslbl = tki.Label(mainFrame, text = 'Back Up Codes');
        backUpCodeslbl.place(relx = 0.1, rely = 0.4, relheight = 0.05, relwidth = 0.4);
        backUpCodesEnt = tki.Entry(mainFrame);
        backUpCodesEnt.place(relx = 0.4, rely = 0.4, relheight = 0.05, relwidth = 0.4);

        logInBtn = tki.Button(mainFrame, text = 'Log in', command = activate);
        logInBtn.place(relx = 0.3, rely = 0.5, relheight = 0.05, relwidth = 0.4);

        signUpBtn = tki.Button(mainFrame, text = 'Sign Up', command = SignUp);
        signUpBtn.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);        

    def logIn():
        "Initialize logging in";
        invalidCount = 0;
        if(invalidCount < 3):
            username = usernameEnt.get();
            password = passwordEnt.get();
            if(username == '' or password == ''):
                bookNameLbl = tki.Label(text = 'Enter Details');
                bookNameLbl.place(relx = 0.3, rely = 0.8, relheight = 0.05, relwidth = 0.4); 
            else:
                cmd = 'SELECT member_id FROM Members WHERE member_name = (%s)';
                arg = (username);
                cursor.execute(cmd, arg);
                idFetchedCheck = cursor.fetchone();
                if(idFetchedCheck == None):
                    bookNameLbl = tki.Label(text = 'No Username In Database');
                    bookNameLbl.place(relx = 0.3, rely = 0.8, relheight = 0.05, relwidth = 0.4);
                else:          
                    cmd = 'SELECT member_id FROM Members WHERE member_name = (%s) AND passwords = (%s)';
                    arg = (username, password);
                    cursor.execute(cmd, arg);
                    dataFetched = cursor.fetchone();
                    if(dataFetched == None):
                        invalidCount = invalidCount + 1;                    
                        bookNameLbl = tki.Label(text = 'Incorrect Password');
                        bookNameLbl.place(relx = 0.3, rely = 0.8, relheight = 0.05, relwidth = 0.4);
                        
                        forgetPasswordBtn = tki.Button(mainFrame, text = 'Forget Password', command = forgetPassword);
                        forgetPasswordBtn.place(relx = 0.3, rely = 0.9, relheight = 0.05, relwidth = 0.4);
                    else:
                        cmd = 'SELECT MAX(log_number) FROM logInCredsMem';
                        cursor.execute(cmd);
                        logNumber = cursor.fetchone();
                        logNumber = logNumber [0];
                        if(logNumber == None):
                            logNumber = 1;
                        else:
                            logNumber = logNumber + 1;    
                        dateTime = dt.datetime.now();
                        date = dateTime.date();
                        time = dateTime.time();
                        cmd = 'INSERT INTO logInCredsMem VALUES (%s, %s, %s, %s)';
                        arg = (logNumber, username, date, time);
                        cursor.execute(cmd, arg);
                        connection.commit();
                        print('Logged In');

                        cmd = 'SELECT log_id FROM LogFromThisDeviceM WHERE member_name = (%s)';
                        arg = (username);
                        cursor.execute(cmd, arg);
                        logIdFetch =  cursor.fetchone();
                        if(logIdFetch == None):
                            cmd = 'SELECT MAX(log_id) FROM LogFromThisDeviceM';
                            cursor.execute(cmd);
                            logIdNew = cursor.fetchone();
                            logIdNew = logIdNew [0];
                            if(logIdNew == None):
                                logIdNew = 1;
                            else:
                                logIdNew = logIdNew + 1;    
                            logStatus = 'In';    
                            cmd = 'INSERT INTO LogFromThisDeviceM VALUES (%s, %s, %s, %s, %s)';
                            arg = (logIdNew, username, date, time, logStatus);
                            cursor.execute(cmd, arg);
                            connection.commit();
                            print('Logged In');
                            windowToGo(username);
                        else:
                            cmd = 'SELECT MAX(log_id) FROM LogFromThisDeviceM';
                            cursor.execute(cmd);
                            logId = cursor.fetchone();    
                            logId = logId [0];
                            if(logId == None):
                                logId = 1;
                            else:
                                logId = logId + 1;    
                            logStatus = 'In';
                            cmd = 'UPDATE LogFromThisDeviceM SET log_id = (%s), date_in = (%s), time_in = (%s), log_status = (%s) WHERE log_status = "Out" AND member_name = (%s)';
                            arg = (logId, date, time, logStatus, username);
                            cursor.execute(cmd, arg);
                            connection.commit();
                            print('Logged In');
                            windowToGo(username);
        else:
            usernameLbl = tki.Label(mainFrame, text = 'Account Locked');
            usernameLbl.place(relx = 0.3, rely = 0.8, relheight = 0.05, relwidth = 0.4);  
                          
    if(second == False):
        titleScreen();
        usernameLbl = tki.Label(mainFrame, text = 'Username');
        usernameLbl.place(relx = 0.1, rely = 0.3, relheight = 0.05, relwidth = 0.4);
        usernameEnt = tki.Entry(mainFrame);
        usernameEnt.place(relx = 0.4, rely = 0.3, relheight = 0.05, relwidth = 0.4);

        passwordLbl = tki.Label(mainFrame, text = 'Password');
        passwordLbl.place(relx = 0.1, rely = 0.4, relheight = 0.05, relwidth = 0.4);
        passwordEnt = tki.Entry(mainFrame);
        passwordEnt.place(relx = 0.4, rely = 0.4, relheight = 0.05, relwidth = 0.4);

        logInBtn = tki.Button(mainFrame, text = 'Log in', command = logIn);
        logInBtn.place(relx = 0.3, rely = 0.5, relheight = 0.05, relwidth = 0.4);

        signUpBtn = tki.Button(mainFrame, text = 'Sign Up', command = SignUp);
        signUpBtn.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);

    else:
        cmd = 'SELECT MAX(log_number) FROM logInCredsMem';
        cursor.execute(cmd);
        logNumber = cursor.fetchone();
        logNumber = logNumber [0];
        if(logNumber == None):
            logNumber = 1;
        else:
            logNumber = logNumber + 1;
             
        dateTime = dt.datetime.now();
        date = dateTime.date();
        time = dateTime.time();
        cmd = 'INSERT INTO logInCredsMem VALUES (%s, %s, %s, %s)';
        arg = (logNumber, usernameH, date, time);
        cursor.execute(cmd, arg);
        connection.commit();            
        print('Logged In');
        windowToGo(usernameH);    

def books():
    "Function to manage book purchase and returns";
    titleScreen();
    def takeBook():
        "For Taking a book from library databse";
        bookName = bookNameEnt.get();
        authorName = authorNameEnt.get();
        if(bookName == '' and authorName == ''):
            bookNameLbl = tki.Label(text = 'Please Fill the Details');
            bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);
        else:    
            cmd = 'SELECT book_status FROM BooksTaken WHERE book_name = (%s) AND book_status = "In Hold" AND taken_by = (%s)';
            arg = (bookName, userNameIn)
            cursor.execute(cmd, arg);
            statusCheck = cursor.fetchone();
            if(statusCheck == None):
                statusCheck = 'Empty';
            else:    
                statusCheck = statusCheck [0];
            if(statusCheck != 'In Hold'):
                cmd = 'SELECT book_id FROM Books WHERE book_name = (%s) AND author_name = (%s)';
                arg = (bookName, authorName);
                cursor.execute(cmd, arg);
                bookIdFetched = cursor.fetchone();
                if(bookIdFetched == None):
                    bookNameLbl = tki.Label(text = 'Sorry! No Book Found');
                    bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);
                else:
                    # Checking the number of book Stocks.
                    cmd = 'SELECT no_copies FROM Books WHERE book_name = (%s)';
                    arg = (bookName);
                    cursor.execute(cmd, arg);
                    noCopiesAvailable = cursor.fetchone();
                    noCopiesAvailable = noCopiesAvailable [0];
                    if(noCopiesAvailable > 0):
                        bookIdFetched = bookIdFetched [0];
                        dateTime = dt.datetime.now();
                        dateTaken = dateTime.date();
                        timeTaken = dateTime.time();
                        bookStatus = 'In Hold';
                        dateReturned = '1111-11-11';
                        timeReturned = '00:00:00';
                        deadLineDate = dateTaken + dt.timedelta(days = 30);
                        deadLineDate = str(deadLineDate);
                        print(deadLineDate);
                        fine = 0;
                        cmd = 'INSERT INTO BooksTaken VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)';
                        arg = (bookIdFetched, bookName, userNameIn, dateTaken, timeTaken, bookStatus, dateReturned, timeReturned, 
                               deadLineDate, fine);
                        cursor.execute(cmd, arg);
                        connection.commit();
                        bookNameLbl = tki.Label(text = 'Book Added');
                        bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);
                        newNoCopies = noCopiesAvailable - 1;
                        cmd = 'UPDATE Books SET no_copies = (%s) WHERE book_name = (%s)';
                        arg = (newNoCopies, bookName);
                        cursor.execute(cmd, arg);
                        connection.commit();
                        print('Passed -');                    
                    else:
                        bookNameLbl = tki.Label(text = 'Sorry, Book Out of stock');
                        bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);                            
            else:
                bookNameLbl = tki.Label(text = 'Book Already Added');
                bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);                        
    
    def returnBook():
        "For returning a book back into the library database";
        bookName = bookNameEnt.get();
        authorName = authorNameEnt.get();
        if(bookName == '' and authorName == ''):
            bookNameLbl = tki.Label(text = 'Please Fill the Details');
            bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);
        else:    
            cmd = 'SELECT time_taken FROM BooksTaken WHERE book_name = (%s) AND taken_by = (%s) AND book_status = "In Hold"';
            arg = (bookName, userNameIn);
            cursor.execute(cmd, arg);
            timefetched = cursor.fetchone();
            if(timefetched == None):
                bookNameLbl = tki.Label(text = 'Sorry! No Book Found');
                bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);
            else:
                cmd = 'SELECT date_taken FROM BooksTaken WHERE book_name = (%s) AND book_status = (%s) AND taken_by = (%s)';
                neededBookStatus = 'In Hold';
                arg = (bookName, neededBookStatus, userNameIn);
                cursor.execute(cmd, arg);
                resultFetched = cursor.fetchone();
                if(resultFetched == None):
                    bookNameLbl = tki.Label(text = 'Book Already Returned');
                    bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);
                else:                        
                    timefetched = timefetched [0];                
                    cmd = 'SELECT dead_line FROM BooksTaken WHERE time_taken = (%s) AND book_status = "In Hold" AND taken_by = (%s)';
                    arg = (timefetched, userNameIn)
                    cursor.execute(cmd, arg);
                    deadLineDate =  cursor.fetchone();
                    deadLineDate = deadLineDate [0];

                    dateTime = dt.datetime.now();
                    bookStatus = 'Returned';    
                    dateReturned = dateTime.date();
                    timeReturned = dateTime.time();
                    if(dateReturned > deadLineDate):
                        daysPast = dateReturned - deadLineDate;
                        daysPast = str(daysPast);
                        daysPast = daysPast[:2];
                        daysPast = int(daysPast);
                        fineToPay = daysPast * 10;
                        fineToPay = str(fineToPay);
                    else:
                        fineToPay = 'No Fine';    
                    cmd = 'UPDATE BooksTaken SET book_status = (%s), date_returned = (%s), time_returned = (%s), Fine = (%s) WHERE time_taken = (%s) AND taken_by = (%s)';
                    arg = (bookStatus, dateReturned, timeReturned, fineToPay, timefetched, userNameIn);
                    cursor.execute(cmd, arg);
                    connection.commit();
                    # Updating the number of copies
                    cmd = 'SELECT no_copies FROM Books WHERE book_name = (%s)';
                    arg = (bookName);
                    cursor.execute(cmd, arg);
                    newNoCopies = cursor.fetchone();
                    newNoCopies = newNoCopies [0] + 1;
                    cmd = 'UPDATE Books SET no_copies = (%s) WHERE book_name = (%s)';
                    arg = (newNoCopies, bookName);
                    cursor.execute(cmd, arg);
                    connection.commit();
                    print('Passed -');
                    bookNameLbl = tki.Label(text = 'Book Returned');
                    bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);    
    
    def searchBook():
        "For searching a book from the database"
        pass;
        
    def renewBook():
        "For nenewing a book which is about to expire";
        bookName = bookNameEnt.get();
        authorName = authorNameEnt.get();
        if(bookName == '' or authorName == ''):
            bookNameLbl = tki.Label(text = 'Please fill the details');
            bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);
        else:
            cmd = 'SELECT time_taken FROM BooksTaken WHERE book_name = (%s) AND book_status = "In Hold" AND taken_by = (%s)';
            arg = (bookName, userNameIn);
            cursor.execute(cmd, arg);
            timeFetched =  cursor.fetchone();    
            if(timeFetched == None):
                bookNameLbl = tki.Label(text = 'Sorry! No Book Found');
                bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);
            else:
                cmd = 'SELECT dead_line FROM BooksTaken WHERE book_name = (%s) AND book_status = (%s) AND taken_by = (%s)';
                bookStatus = 'In Hold';
                arg = (bookName, bookStatus, userNameIn);
                cursor.execute(cmd, arg);
                deadLineFetched = cursor.fetchone();
                deadLineFetched = deadLineFetched [0];
                renewedDate = deadLineFetched + dt.timedelta(days = 30);
                cmd = 'UPDATE BooksTaken SET dead_line = (%s) WHERE book_name = (%s) AND book_status = (%s) AND taken_by = (%s)';
                arg = (renewedDate, bookName, bookStatus, userNameIn);    
                cursor.execute(cmd, arg);
                connection.commit();
                print('Passed -');
                bookNameLbl = tki.Label(text = 'Book Renewed');
                bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);                
                
    def viewBooks():
        "For viewing the whole library books";
        titleScreen();
        cmd = 'SELECT * FROM Books';
        cursor.execute(cmd);
        allBooks = cursor.fetchall();
        y = allBooks = str(allBooks);
        bookNameLbl = tki.Label(text = y);
        bookNameLbl.place(relx = 0.1, rely = 0.2, relheight = 0.05, relwidth = 0.4);
        
        backBtn = tki.Button(mainFrame, text = 'Back', command = mainWindow);
        backBtn.place(relx = 0.3, rely = 0.9, relheight = 0.05, relwidth = 0.4);
    
    def addToFaviroutes():
        "For Adding Book to faviroutes";
        authorName = authorNameEnt.get();
        bookName = bookNameEnt.get();
        
        if(bookName == ""):
            bookNameLbl = tki.Label(text = 'Enter Book name');
            bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.5); 
        else:    
            cmd = 'SELECT book_id FROM Books WHERE book_name = (%s)';
            cursor.execute(cmd, bookName);
            bookIdFetched = cursor.fetchone();
            print(bookIdFetched);
            if(bookIdFetched == None):
                bookNameLbl = tki.Label(text = 'Book Not Found!');
                bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.5); 
            else:    
                cmd = 'SELECT added FROM faviroutes WHERE member_name = (%s) AND book_name = (%s)';
                arg = (userNameIn, bookName);
                cursor.execute(cmd, arg);
                addedStatus = cursor.fetchone();
                if(addedStatus == None):
                    addedStatus = 'Added';
                    cmd = 'INSERT INTO faviroutes VALUES (%s, %s, %s)';
                    arg = (userNameIn, bookName, addedStatus);
                    cursor.execute(cmd, arg);
                    connection.commit();
                    bookNameLbl = tki.Label(text = 'Book Added to Faviroutes');
                    bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);
                else:
                    cmd = 'DELETE FROM faviroutes WHERE book_name = (%s) AND member_name = (%s)';
                    arg = (bookName, userNameIn);
                    cursor.execute(cmd, arg);
                    connection.commit();
                    bookNameLbl = tki.Label(text = 'Book removed from Faviroutes');
                    bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.5);            
    
    bookNameLbl = tki.Label(text = 'Book Name ');
    bookNameLbl.place(relx = 0.07, rely = 0.2, relheight = 0.05, relwidth = 0.4);    
    bookNameEnt = tki.Entry(mainFrame);
    bookNameEnt.place(relx = 0.4, rely = 0.2, relheight = 0.05, relwidth = 0.4);   
     
    authorNameLbl = tki.Label(text = 'Author Name ');
    authorNameLbl.place(relx = 0.07, rely = 0.3, relheight = 0.05, relwidth = 0.4);    
    authorNameEnt = tki.Entry(mainFrame);
    authorNameEnt.place(relx = 0.4, rely = 0.3, relheight = 0.05, relwidth = 0.4);      
     
    takebtn = tki.Button(mainFrame, text = 'Take', command = takeBook);
    takebtn.place(relx = 0.2, rely = 0.4, relheight = 0.05, relwidth = 0.15);  
    
    returnBtn = tki.Button(mainFrame, text = 'Return', command = returnBook);
    returnBtn.place(relx = 0.4, rely = 0.4, relheight = 0.05, relwidth = 0.15);         

    searchBtn = tki.Button(mainFrame, text = 'Search', command = searchBook);
    searchBtn.place(relx = 0.6, rely = 0.4, relheight = 0.05, relwidth = 0.15);

    viewBtn = tki.Button(mainFrame, text = 'View all', command = viewBooks);
    viewBtn.place(relx = 0.2, rely = 0.5, relheight = 0.05, relwidth = 0.15);    

    renewBtn = tki.Button(mainFrame, text = 'Renew', command = renewBook);
    renewBtn.place(relx = 0.4, rely = 0.5, relheight = 0.05, relwidth = 0.15); 

    viewtableBtn = tki.Button(mainFrame, text = 'Add to fav', command = addToFaviroutes);
    viewtableBtn.place(relx = 0.6, rely = 0.5, relheight = 0.05, relwidth = 0.15);
    
    backBtn = tki.Button(mainFrame, text = 'Back', command = mainWindow);
    backBtn.place(relx = 0.3, rely = 0.9, relheight = 0.05, relwidth = 0.4);    
    
def SignUp():
    "Function to sign up a new member";
    titleScreen();
    dateTime = dt.datetime.now();
    date = dateTime.date();
    time = dateTime.time();
    def initializeProcess():
        userNameN = usernameEnt.get();
        phone = phoneEnt.get();
        passwordN = passwordEnt.get();                    
        try:
            phone = int(phone);
        except(ValueError):
            phone = 'Error';
        else:
            phone = int(phone);
            phoneS = str(phone);
        finally:            
            if(userNameN == '' or passwordN == '' or phone == ''):
                bookNameLbl = tki.Label(text = 'Invalid Details');
                bookNameLbl.place(relx = 0.3, rely = 0.8, relheight = 0.05, relwidth = 0.4);
            elif(type(phone) != int or len(phoneS) != 10):
                bookNameLbl = tki.Label(text = 'Invalid Phone Number');
                bookNameLbl.place(relx = 0.3, rely = 0.8, relheight = 0.05, relwidth = 0.4);   
            else:
                cmd = 'SELECT member_name FROM Members WHERE member_name = (%s)';
                arg = (userNameN);
                cursor.execute(cmd, arg);
                nameGot = cursor.fetchone();
                if(nameGot == None):
                    cmd = 'SELECT MAX(member_id) FROM Members';
                    cursor.execute(cmd);
                    memberId = cursor.fetchone();
                    memberId = memberId[0];
                    if(memberId == None):
                        memberId = 1;
                    else:
                        memberId = memberId + 1;    
                    cmd = 'INSERT INTO Members VALUES (%s, %s, %s, %s)';
                    arg = (memberId, userNameN, phone, passwordN);
                    cursor.execute(cmd, arg);
                    connection.commit();
                    print('Passed -');
                    cmd = 'SELECT MAX(log_id) FROM LogFromThisDeviceM';
                    cursor.execute(cmd);
                    logId = cursor.fetchone();    
                    logId = logId [0];
                    if(logId == None):
                        logId = 1;
                    else:
                        logId = logId + 1;    
                    logStatus = 'In';
                    cmd = 'INSERT INTO LogFromThisDeviceM VALUES (%s, %s, %s, %s, %s)';
                    arg = (logId, userNameN, date, time, logStatus);
                    cursor.execute(cmd, arg);
                    connection.commit();     
                    print('Passed -');               
                    #logInProcess(windowToGo = mainWindow, usernameH = userNameN, second = True);
                    bookNameLbl = tki.Label(text = 'Please Restart the app ');
                    bookNameLbl.place(relx = 0.3, rely = 0.8, relheight = 0.05, relwidth = 0.4);
                
    usernameLbl = tki.Label(mainFrame, text = 'Username');
    usernameLbl.place(relx = 0.1, rely = 0.3, relheight = 0.05, relwidth = 0.4);
    
    usernameEnt = tki.Entry(mainFrame);
    usernameEnt.place(relx = 0.4, rely = 0.3, relheight = 0.05, relwidth = 0.4)
    
    passwordLbl = tki.Label(mainFrame, text = 'Password');
    passwordLbl.place(relx = 0.1, rely = 0.4, relheight = 0.05, relwidth = 0.4);
    
    passwordEnt = tki.Entry(mainFrame);
    passwordEnt.place(relx = 0.4, rely = 0.4, relheight = 0.05, relwidth = 0.4)
    
    phoneLbl = tki.Label(mainFrame, text = 'Phone');
    phoneLbl.place(relx = 0.1, rely = 0.5, relheight = 0.05, relwidth = 0.4);
    
    phoneEnt = tki.Entry(mainFrame);
    phoneEnt.place(relx = 0.4, rely = 0.5, relheight = 0.05, relwidth = 0.4)
    
    signUpBtnI = tki.Button(mainFrame, text = 'Sign Up', command = initializeProcess);
    signUpBtnI.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);
                
    backbtn = tki.Button(mainFrame, text = 'Back', command = mainFrame.destroy);
    backbtn.place(relx = 0.3, rely = 0.7, relheight = 0.05, relwidth = 0.4);
    
def profile():
    "This function shows the profile of member and provides features to manage it";
    titleScreen();
    def changeSettings():
        "To change the settings of the accounts";
        titleScreen();
        dateTime = dt.datetime.now();
        date = dateTime.date();
        time = dateTime.time();
        def changePassword():
            "Function to change the password of the account";
            def initializeChange():
                "Initializing the process";
                currentPass = currentPassEnt.get();
                newPassword = newPasswordEnt.get();
                if(currentPass == '' or newPassword == ''):
                    bookNameLbl = tki.Label(text = 'Please Enter the details');
                    bookNameLbl.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);
                else:    
                    cmd = 'SELECT passwords FROM Members WHERE member_name = (%s)';
                    arg = (userNameInNow);
                    cursor.execute(cmd, arg);
                    passwordFetched = cursor.fetchone();
                    if(passwordFetched == None):
                        passwordFetched = 'Zero';
                    else:
                        passwordFetched = passwordFetched [0];    
                    if(passwordFetched == currentPass):
                        cmd = 'UPDATE Members SET passwords = (%s) WHERE member_name = (%s)';
                        arg = (newPassword, userNameInNow);
                        cursor.execute(cmd, arg);
                        connection.commit();   
                        print('Passed -');
                        bookNameLbl = tki.Label(text = 'Password Changed');
                        bookNameLbl.place(relx = 0.3, rely = 0.7, relheight = 0.05, relwidth = 0.4); 
                    else:
                        bookNameLbl = tki.Label(text = 'Incorrect Password');
                        bookNameLbl.place(relx = 0.3, rely = 0.7, relheight = 0.05, relwidth = 0.4);
            
            
            titleScreen();
            currentPassLbl = tki.Label(mainFrame, text = 'Current Password');
            currentPassLbl.place(relx = 0.1, rely = 0.3, relheight = 0.05, relwidth = 0.4);
            currentPassEnt = tki.Entry(mainFrame);
            currentPassEnt.place(relx = 0.4, rely = 0.3, relheight = 0.05, relwidth = 0.4);
            
            newPasswordLbl = tki.Label(mainFrame, text = 'New Password');
            newPasswordLbl.place(relx = 0.1, rely = 0.4, relheight = 0.05, relwidth = 0.4);
            newPasswordEnt = tki.Entry(mainFrame);
            newPasswordEnt.place(relx = 0.4, rely = 0.4, relheight = 0.05, relwidth = 0.4);
            
            changeUsernameBtn = tki.Button(mainFrame, text = 'Change', command = initializeChange);
            changeUsernameBtn.place(relx = 0.3, rely = 0.5, relheight = 0.05, relwidth = 0.4);
        
            changeUsernameBtn = tki.Button(mainFrame, text = 'Back', command = mainWindow);
            changeUsernameBtn.place(relx = 0.3, rely = 0.6, relheight = 0.05, relwidth = 0.4);     
        
        def setRemainder():
            messageLbl = tki.Label(mainFrame, text = 'This feature is under Development');
            messageLbl.place(relx = 0.3, rely = 0.7, relheight = 0.05, relwidth = 0.4);            
                 
        def autoClose():
            messageLbl = tki.Label(mainFrame, text = 'This feature is under Development');
            messageLbl.place(relx = 0.3, rely = 0.7, relheight = 0.05, relwidth = 0.4);   
               
        def timeSpend():
            titleScreen();
            cmd = 'SELECT date_time FROM openAccount WHERE member_name = (%s) ORDER BY date_in DESC, time_in DESC LIMIT 1';
            cursor.execute(cmd, userNameIn);
            dateTimeFetched = cursor.fetchone();
            dateTimeFetched = dateTimeFetched [0];
            
            dateTime = dt.datetime.now();    #
            date = dateTime.date();
            
            totalTimeSpend = dateTime - dateTimeFetched; # 
            seconds = totalTimeSpend.seconds;
            minutes = seconds / 60;
            hours = minutes / 60;

            cmd = 'SELECT minutes FROM totalTimesIn WHERE member_name = (%s) AND date_today = (%s)';
            arg = (userNameIn, date);
            cursor.execute(cmd, arg);
            hoursFetched = cursor.fetchone();
            if(hoursFetched == None):
                cmd = 'INSERT INTO totalTimesIn VALUES (%s, %s, %s, %s)';
                arg = (userNameIn, minutes, date, dateTime);
                cursor.execute(cmd, arg);
                connection.commit();
                print('Pass check 1');
            else:
                hoursFetched = hoursFetched [0];
                hours = hours + hoursFetched;  
                cmd = 'UPDATE totalTimesIn SET minutes = (%s) WHERE member_name = (%s) AND date_today = (%s)';
                arg = (minutes, userNameIn, date);
                cursor.execute(cmd, arg);
                connection.commit();  
                print('Pass check 2');
                
            cmd = 'SELECT date_time FROM totalTimesIn WHERE member_name = (%s) ORDER BY date_time ASC LIMIT 1'   
            cursor.execute(cmd, userNameIn);
            dateFetchedToDelete = cursor.fetchone();
            print('Pass check 3');
            
            if(dateFetchedToDelete == None):
                "Do Not Delete";
                pass;
            else:
                dateFetchedToDelete = dateFetchedToDelete[0];
                dateDifference = dateTime - dateFetchedToDelete;
                dateDifference = dateDifference.days;
                if(dateDifference >= 3):
                    cmd = 'SELECT COUNT(member_name) FROM totalTimesIn';
                    cursor.execute(cmd);
                    daysToDelete = cursor.fetchone();
                    daysToDelete = daysToDelete[0];
                    print(daysToDelete);
                    if(daysToDelete > 3):
                        for i in range(0, (daysToDelete - 3)):
                            cmd = 'DELETE FROM totalTimesIn WHERE member_name = (%s) ORDER BY date_time ASC LIMIT 1';
                            cursor.execute(cmd, userNameIn);
                            connection.commit();    
                            print('Pass check 4');                     
                            
            graphMinutes = [2, 30, 60];
            graphDays  = [];
            cmd = 'SELECT minutes FROM totalTimesIn ';
            cursor.execute(cmd);
            graphDaysFetched = cursor.fetchall();
            for i in range(0, 3):
                for x in range(0, 1):
                    graphDays.append(graphDaysFetched[i][x]);
            print(graphDays);
            
            mat.bar(graphDays, graphMinutes);
            mat.title('Library Usage');
            mat.xlabel('Day Before Yesterday            Yesterday               Today');
            mat.ylabel('Hours');
            mat.show();    

            autoCloseBtn = tki.Button(mainFrame, text = 'Auto Close', command = autoClose);
            autoCloseBtn.place(relx = 0.35, rely = 0.35, relheight = 0.05, relwidth = 0.3); 
                        
            setRemainderBtn = tki.Button(mainFrame, text = 'Set Remainder', command = setRemainder);
            setRemainderBtn.place(relx = 0.35, rely = 0.45, relheight = 0.05, relwidth = 0.3); 
            
            exitBtn = tki.Button(mainFrame, text = 'Back', command = mainWindow);
            exitBtn.place(relx = 0.35, rely = 0.55, relheight = 0.05, relwidth = 0.3); 
                        
        def switchAccounts():
            "For switching the accounts from one to another";
            # Not fully develpoed
            titleScreen();
            cmd = 'SELECT COUNT(member_name) FROM LogFromThisDeviceM WHERE log_status = "In"';
            cursor.execute(cmd);
            count = cursor.fetchone();
            if(count == None):
                count = 0;
            else:
                count = count[0];    
            cmd = 'SELECT member_name FROM LogFromThisDeviceM WHERE log_status = "In"';
            cursor.execute(cmd);
            otherAccounts = cursor.fetchall();
            if(otherAccounts == None):
                otherAccounts = ['No Accounts Logged In'];
            else:
                p = 0.2;                
                for i in range(0, count):
                    print(otherAccounts[i]);
                    name = tki.Button(mainFrame, text = otherAccounts[i], command = logInProcess);
                    name.place(relx = 0.3, rely = p, relheight = 0.05, relwidth = 0.4);
                    p = p + 0.1;
            
            print('Passed X');        
            signUpbtn = tki.Button(mainFrame, text = 'New account', command = SignUp);
            signUpbtn.place(relx = 0.3, rely = p , relheight = 0.05, relwidth = 0.4);            
            p = p + 0.1;
            signUpbtn = tki.Button(mainFrame, text = 'Log in', command = logInProcess);
            signUpbtn.place(relx = 0.3, rely = p , relheight = 0.05, relwidth = 0.4);
            
            signUpbtn = tki.Button(mainFrame, text = 'Exit', command = closeWindow);
            signUpbtn.place(relx = 0.3, rely = 0.8 , relheight = 0.05, relwidth = 0.4);
                        
        def signOut():
            "Function signs out the member from the database";
            print(userNameInNow)
            cmd = 'UPDATE LogFromThisDeviceM SET log_status = "Out" WHERE member_name = (%s) ORDER BY date_in, time_in DESC LIMIT 1';
            arg = (userNameInNow);
            cursor.execute(cmd, arg);
            connection.commit();
            print('Passed -');
            switchAccounts();
        
        def cancelMembership():
            "This function cancels the membership of the member from the library database";
            
            fromTableToDelete = ['LogFromThisDeviceM', 'logInCredsMem', 'BooksTaken', 'backUpCodes', 'faviroutes', 'openAccount', 'totalTimesIn', 'extraDetails', 'Members'];
            i = 1;
            for tables in fromTableToDelete:
                cmd1 = 'DELETE FROM ';
                if(tables == 'BooksTaken'):
                    cmd = 'WHERE taken_by = (%s)';
                else:    
                    cmd2 = ' WHERE member_name = (%s)';
                cmd = cmd1 + tables + cmd2;
                arg = (userNameInNow);
                cursor.execute(cmd, arg);
                connection.commit();
                print('Passed', i);
                i = i + 1;
            switchAccounts();

        def security():
            titleScreen();
            def submit():       
                def submitChange():
                    emailFN = emailEntFN.get();
                    if(emailFN.endswith('mail.com')):
                        cmd = 'UPDATE extraDetails SET email = (%s)';
                        arg = (emailFN);
                        cursor.execute(cmd, arg);
                        connection.commit();        
                        errorlbl = tki.Label(mainFrame, text = 'Email Updated');
                        errorlbl.place(relx = 0.35, rely = 0.3, relheight = 0.05, relwidth = 0.3);   
                        print('Updated'); 
                    else:
                        errorlbl = tki.Label(mainFrame, text = 'Enter a valid email');
                        errorlbl.place(relx = 0.35, rely = 0.3, relheight = 0.05, relwidth = 0.3);   
        
                if(submitOrChange == 'Submit'):
                    emailF = emailEntF.get();
                    if(emailF == ''):
                        errorlbl = tki.Label(mainFrame, text = 'Enter Email');
                        errorlbl.place(relx = 0.2, rely = 0.3, relheight = 0.05, relwidth = 0.3);
                    else:
                        if(emailF.endswith('mail.com')):
                            cmd = 'INSERT INTO extraDetails VALUES (%s, %s)';
                            arg = (userNameInNow, emailF);
                            cursor.execute(cmd, arg);
                            connection.commit();
                            errorlbl = tki.Label(mainFrame, text = 'Email Saved');
                            errorlbl.place(relx = 0.35, rely = 0.3, relheight = 0.05, relwidth = 0.3);
                        else:
                            errorlbl = tki.Label(mainFrame, text = 'Enter a valid email');
                            errorlbl.place(relx = 0.35, rely = 0.3, relheight = 0.05, relwidth = 0.3);    
                else:
                    emailLbl = tki.Label(mainFrame, text = 'Email');
                    emailLbl.place(relx = 0.2, rely = 0.2, relheight = 0.05, relwidth = 0.3);
                    emailEntFN = tki.Entry(mainFrame);
                    emailEntFN.place(relx = 0.4, rely = 0.2, relheight = 0.05, relwidth = 0.3);
                    submitBtn = tki.Button(mainFrame, text = 'Change Email', command = submitChange);
                    submitBtn.place(relx = 0.35, rely = 0.45, relheight = 0.05, relwidth = 0.3);
                                                                                   
            def generateBackUpCodes():
                cmd = 'SELECT buc_1, buc_2, buc_3, buc_4 FROM backUpCodes WHERE member_name = (%s)';
                arg = (userNameInNow);
                cursor.execute(cmd, arg);
                codesFetched = cursor.fetchone();
                if(codesFetched == None):
                    backUpCodeList = [];
                    for i in range(0, 4):
                        backUpCodeList.append(ran.randrange(1000, 9999));

                    if(len(backUpCodeList) == 4):
                        cmd = 'INSERT INTO backUpCodes VALUES (%s, %s, %s, %s, %s)';
                        arg = (userNameInNow, backUpCodeList[0], backUpCodeList[1], backUpCodeList[2], backUpCodeList[3]);
                        cursor.execute(cmd, arg);
                        connection.commit();
                        errorlbl = tki.Label(mainFrame, text = backUpCodeList);
                        errorlbl.place(relx = 0.35, rely = 0.3, relheight = 0.05, relwidth = 0.3);
                    else:
                        errorlbl = tki.Label(mainFrame, text = 'Something went wrong');
                        errorlbl.place(relx = 0.2, rely = 0.3, relheight = 0.05, relwidth = 0.3);
                        
                else:      
                    cmd = 'SELECT buc_1, buc_2, buc_3, buc_4 FROM backUpCodes WHERE member_name = (%s)';
                    arg = (userNameInNow);
                    cursor.execute(cmd, arg);
                    codesFetched = cursor.fetchall();                    
                    errorlbl = tki.Label(mainFrame, text = codesFetched);
                    errorlbl.place(relx = 0.35, rely = 0.3, relheight = 0.05, relwidth = 0.3);
            
            cmd = 'SELECT email FROM extraDetails WHERE member_name = (%s)';
            arg = (userNameInNow);
            cursor.execute(cmd, arg);
            emailFetched = cursor.fetchone();
            emailLbl = tki.Label(mainFrame, text = 'Email');
            emailLbl.place(relx = 0.2, rely = 0.2, relheight = 0.05, relwidth = 0.3);
            if(emailFetched == None):
                emailEntF = tki.Entry(mainFrame);
                emailEntF.place(relx = 0.4, rely = 0.2, relheight = 0.05, relwidth = 0.3);
                submitOrChange = 'Submit';
            else:    
                emailFetched = emailFetched[0];
                emailLbl = tki.Label(mainFrame, text = emailFetched);
                emailLbl.place(relx = 0.4, rely = 0.2, relheight = 0.05, relwidth = 0.3);
                submitOrChange = 'Change Email';
            
            submitBtn = tki.Button(mainFrame, text = submitOrChange, command = submit);
            submitBtn.place(relx = 0.35, rely = 0.45, relheight = 0.05, relwidth = 0.3);

            backupCodesbtn = tki.Button(mainFrame, text = 'Back Up Codes', command = generateBackUpCodes);
            backupCodesbtn.place(relx = 0.35, rely = 0.55, relheight = 0.05, relwidth = 0.3);

            backBtn = tki.Button(mainFrame, text = 'Back', command = mainWindow);
            backBtn.place(relx = 0.35, rely = 0.65, relheight = 0.05, relwidth = 0.3);            
        
        profileBtn = tki.Button(mainFrame, text = 'Change Password', command = changePassword);
        profileBtn.place(relx = 0.35, rely = 0.25, relheight = 0.05, relwidth = 0.3);      

        bookBtn = tki.Button(mainFrame, text = 'Switch Account', command = switchAccounts);
        bookBtn.place(relx = 0.35, rely = 0.35, relheight = 0.05, relwidth = 0.3);

        profileBtn = tki.Button(mainFrame, text = 'Sign Out', command = signOut);
        profileBtn.place(relx = 0.35, rely = 0.45, relheight = 0.05, relwidth = 0.3);      
        
        securityBtn = tki.Button(mainFrame, text = 'Security', command = security);
        securityBtn.place(relx = 0.35, rely = 0.55, relheight = 0.05, relwidth = 0.3);

        profileBtn = tki.Button(mainFrame, text = 'Cancel Membership', command = cancelMembership);
        profileBtn.place(relx = 0.35, rely = 0.65, relheight = 0.05, relwidth = 0.3);

        timeSpendBtn = tki.Button(mainFrame, text = 'Time Spend', command = timeSpend);
        timeSpendBtn.place(relx = 0.35, rely = 0.75, relheight = 0.05, relwidth = 0.3);

        exitBtn = tki.Button(mainFrame, text = 'Back', command = mainWindow);
        exitBtn.place(relx = 0.35, rely = 0.85, relheight = 0.05, relwidth = 0.3);

    if(userNameIn == None):
        cmd = 'SELECT member_name FROM LogFromThisDeviceM WHERE log_status = "In" ORDER BY date_in DESC, time_in DESC LIMIT 1';
        cursor.execute(cmd);
        userNameInNow = cursor.fetchone();
        userNameInNow = userNameInNow[0];
        print('Here : ', userNameInNow);
    else:    
        userNameInNow = userNameIn;
    cmd = 'SELECT member_id FROM Members WHERE member_name = (%s)';
    arg = (userNameInNow);
    cursor.execute(cmd, arg);
    idFetch = cursor.fetchone();
    cmd = 'SELECT member_phone FROM Members WHERE member_name = (%s)';
    arg = (userNameInNow);
    cursor.execute(cmd, arg);
    memberPhone = cursor.fetchone();
    memberPhone = memberPhone [0];
    memberPhone = str(memberPhone);
    idFetch = idFetch [0];
    idFetch = str(idFetch);
    nameFetched = 'Username : ' + userNameInNow;
    idFetch = 'Member Id : ' + idFetch;
    memberPhone = 'Phone : ' + memberPhone;
    print('Passed -');
    currentPassLbl = tki.Label(mainFrame, text = nameFetched);
    currentPassLbl.place(relx = 0.35, rely = 0.3, relheight = 0.05, relwidth = 0.3);
    
    currentPassLbl = tki.Label(mainFrame, text = idFetch);
    currentPassLbl.place(relx = 0.35, rely = 0.4, relheight = 0.05, relwidth = 0.3);
    
    currentPassLbl = tki.Label(mainFrame, text = memberPhone);
    currentPassLbl.place(relx = 0.35, rely = 0.5, relheight = 0.05, relwidth = 0.3);    
    
    changeSettingsBtn = tki.Button(mainFrame, text = 'Settings', command = changeSettings);
    changeSettingsBtn.place(relx = 0.35, rely = 0.6, relheight = 0.05, relwidth = 0.3);
    
    backBtn = tki.Button(mainFrame, text = 'Back', command = mainWindow);
    backBtn.place(relx = 0.35, rely = 0.7, relheight = 0.05, relwidth = 0.3);    

def closeWindow():
    "Function called to close a window";
    mainFrame.destroy();
    def closeConnection():
        "For closing the connection between database and programme";
        connection.close();
        print('Connection Closed');
    closeConnection();    
    
def mainWindow(mainWindowUsername = ''):
    "This function provides the main window for the application that have buttons and labels";
    titleScreen();
    if(mainWindowUsername == ''):
        mainWindowUsername = userNameIn;
    
    cmd = 'SELECT in_id FROM openAccount WHERE member_name = (%s) ORDER BY date_in DESC, time_in DESC LIMIT 1 ';
    cursor.execute(cmd, userNameIn);
    inId = cursor.fetchone();
    print('->',inId);
    if(inId == None):
        inId = 1;
    else:
        inId = inId [0] + 1;
            
    dateTime = dt.datetime.now();
    dateNow = dateTime.date();
    timeNow = dateTime.time(); 
    
    cmd = 'INSERT INTO openAccount VALUES (%s, %s, %s, %s, %s)';    
    arg = (inId, userNameIn, timeNow, dateNow, dateTime);
    cursor.execute(cmd, arg);
    connection.commit();
    
    print('Passed -');    
    newPasswordLbl = tki.Label(mainFrame, text = mainWindowUsername, font = 10);
    newPasswordLbl.place(relx = 0.3, rely = 0.2, relheight = 0.05, relwidth = 0.4);
    bookBtn = tki.Button(mainFrame, text = 'Books', command = books);
    bookBtn.place(relx = 0.35, rely = 0.35, relheight = 0.05, relwidth = 0.3);
    
    profileBtn = tki.Button(mainFrame, text = 'Profile', command = profile);
    profileBtn.place(relx = 0.35, rely = 0.45, relheight = 0.05, relwidth = 0.3);      
        
    exitBtn = tki.Button(mainFrame, text = 'Exit', command = closeWindow);
    exitBtn.place(relx = 0.35, rely = 0.55, relheight = 0.05, relwidth = 0.3);    

# Creating the frame for the application.
mainFrame = tki.Tk();
mainFrame.geometry("500x600");
mainFrame.title('Library');

# Arguments for Database Connection.
host = 'localhost';
user = 'root';
password = '';
database = 'Xio';

# Establishing Connection.
try:
    connection = psql.connect(host = host, user = user, password = password, database = database);
    cursor = connection.cursor();
    print('Connection Established');
except(RuntimeError):
    print('Connection Failed');
else:    
    # To check if the user is already logged in, in the device.
    cmd = 'SELECT member_name FROM LogFromThisDeviceM WHERE log_status = "In" ORDER BY date_in DESC, time_in DESC LIMIT 1';
    cursor.execute(cmd);
    userNameIn = cursor.fetchone();
    if(userNameIn == None):
        print(userNameIn);
        logInProcess(windowToGo = mainWindow);
        autoLogin = False;
    else:
        userNameIn = userNameIn [0];    
        autoLogin = True;
        mainWindow();
    print('Logging In');           
    mainFrame.mainloop();
finally:
    print('Connection Terminated');    
# Programme Terminates    
    