# computer project
# library management system

def addbklst():#to add new books to the library
    import pickle
    f=open('book.dat','ab')
    pw=input('Enter your password')
    if pw=='lib@123':
        x=int(input('Enter the number of entries'))
    else:
        print('Wrong password: access denied')
        x=0
    for i in range(x):
        Id=input('Enter the book id')
        nm=input('Enter the name of the book')
        aut=input('Enter the name of the author')
        pub=input('Enter the name of the publisher')
        cop=int(input('Enter the number of copies'))
        L=[Id,nm,aut,pub,cop]
        pickle.dump(L,f)
    f.close()
    print()
    ch=input('Do you want to continue accessing the library:y/n')
    print()
    if ch.upper()=='Y':
        main()
    else:
        print()
        print('**********Thank you for visiting**********')
        print('☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺')


        
def search():
    '''To search for a particular book by its name'''
    import pickle
    f=open('book.dat','rb')
    ch=input('Enter the book id')
    c=0
    try:
        while True:
            r=pickle.load(f)
            if r[0]==ch:
                    c+=1
                    print()
                    print('******************************************************************************************************************')
                    print('Book id:',r[0],'\t','Name of the book:',r[1],'\t','Author:',r[2],'\t','Publisher:',r[3],'\t','No. of copies:',r[4])
                    print('******************************************************************************************************************')

    except EOFError:
        pass
    if c==0:
        print('The book is not available')
    f.close()
    print()
    ch=input('Do you want to continue accessing the library:y/n')
    print()
    if ch.upper()=='Y':
        main()
    else:
        print()
        print('**********Thank you for visiting**********')
        print('☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺')
def issue():
    '''To issue a book by its name
    and change the no of books available for issued book'''

    import pickle
    import os
    from datetime import date,datetime,timedelta
    nm=input('Enter the name of the book to be issued or book id')
    cdno=input('Enter your card number')
    
    f1=open('new.dat','wb')
    x=nm.upper()
    dtnow=date.today()
    duedt=dtnow+timedelta(days=7)
    
    try:
        f=open('book.dat','rb')
        c=0
        while True:
            r=pickle.load(f)
            if r[1]==x or r[0]==x:
                c+=1
                if r[4]!=0:
                    r[4]-=1
            
                    print()
                    print('******Munazza\'s and Ananya\'s Library********')
                    print('^^^^^^^^^^^^^ RECIEPT ^^^^^^^^^^^^^')
                    print()
                    print('Book id:',r[0])
                    print('Name of the book:',r[1])
                    print('Author:',r[2])
                    print('Publisher:',r[3])
                    print('The issuing date is:',dtnow)
                    print('The due date is:',duedt)
                
                    print('The book has been issued to the card number',cdno)
                    print('✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔')
                pickle.dump(r,f1)
            else:
                pickle.dump(r,f1)
        
    except EOFError:
        pass
    if c==0:
            print('The book is not available')
    f.close()
    f1.close()
    os.rename('book.dat','ofile.dat') #making new file with updated details
    os.rename('new.dat','book.dat')
    os.remove('ofile.dat')

    #asking if still want to continue accessing library
    ch=input('Do you want to continue accessing the library:y/n')
    print()
    if ch.upper()=='Y':
        main()
    else:
        print()
        print('**********Thank you for visiting**********')
        print('☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺')


def edit():
    import pickle
    import os
    f=open('new.dat','wb')
    pw=input('Enter your password')
    if pw=='lib@123':
        cn=input('Are you sure you want to make changes?')
        if cn.upper()=='Y' or cn.upper()=='YES':
            y=input('Enter the book id of the record you want to make changes to')
            c=0
        else:
            y=''
            c=''
    else:
        print('Wrong password: access denied')
        y=''
        c=''
    try:
        f1=open('book.dat','rb')
        while True:
            r=pickle.load(f1)
            #print(r)
            if r[0]==y:
                c+=1
                ch=input('Choose what you want to update: book name, author name, publisher name, no of copies')
                if ch.upper()=='BOOK NAME':
                    bnm=input('Enter new name of the book')
                    r[1]=bnm
                    pickle.dump(r,f)
                elif ch.upper()=='AUTHOR NAME':
                    anm=input('Enter new name of the author')
                    r[2]=anm
                    pickle.dump(r,f)
                elif ch.upper()=='PUBLISHER NAME':
                    pnm=input('Enter new name of the publisher')
                    r[3]=pnm
                    pickle.dump(r,f)
                elif ch.upper()=='NO OF COPIES':
                    nc=int(input('Enter new number of copies'))
                    r[4]=nc
                    pickle.dump(r,f)
            elif r[0]!=y:
                pickle.dump(r,f)
    except EOFError:
        pass
    if c==0:
            print('invalid input')
    f.close()
    f1.close()
    
    os.rename('book.dat','ofile.dat')
    os.rename('new.dat','book.dat')
    os.remove('ofile.dat')
    ch1=input('Do you want to continue accessing the library:y/n')
    print()
    if ch1.upper()=='Y':
        main()
    else:
        print()
        print('**********Thank you for visiting**********')
        print('☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺')

        
        
def viewbklst():
    '''To view the books available in the library'''
    
    import pickle
    f=open('book.dat','rb')
    print('---------------##############################---------------------')
    try:
        while True:
            r=pickle.load(f)
            print()
            print('Book id:',r[0],'\t','Name of the book:',(r[1].ljust(30)),'Author:',(r[2].ljust(20)),
                  'Publisher:',(r[3].ljust(20)),'No. of copies:',r[4])
    except EOFError:
        pass
    f.close()
    print()

    #asking if still want to continue accessing library
    ch=input('Do you want to continue accessing the library:y/n')
    print()
    if ch.upper()=='Y':
        main()
    else:
        print()
        print('**********Thank you for visiting**********')
        print('☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺')

        
def main():
    '''The Menu of the program'''
    import pickle
    print('************____Munazza\'s and Ananya\'s Library____************')
    print()
    f=open('main_opt.dat','wb')
    L=['1.View books available','2.Search for a boook','3.Issue a book','4.Add a new book','5.Edit an existing record']
    pickle.dump(L,f)
    f.close()
    f=open('main_opt.dat','rb')
    r=pickle.load(f)
    for i in r:
        print(i)

    ch=int(input('Enter what do you want to do:1/2/3/4/5'))
    if ch==1:
        viewbklst()
    elif ch==2:
        search()
    elif ch==4:
        addbklst()
    elif ch==3:
        issue()
    elif ch==5:
        edit()
        
    f.close()
    
'''calling the menu'''   
main()





