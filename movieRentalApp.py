import movieStore

#Store1 = movieStore.MovieStore("Nawaf's Store",9,10,3.95,5.99)
#print(Store1)

def run():
    while True:

        Store1 = movieStore.MovieStore()

        name = input('Enter Name: ')
        print(f'hello {name}, Welcome to Nawafs Movie Store\n What are you looking for: \n1) Rent Movies \n2) Return Movies \n3) Calculate Late Fees\n4) Exit)')
        selection = int(input('Select Option (1, 2, 3)'))

        if  selection == 1:
            Rent_Movies = int(input('Enter the number of movies you would like to rent:'))
            while Store1.rentMovie(Rent_Movies) < 0:
                print('Invalid Option')
                continue
            Rent_Movies = int(input('Enter the number of movies you would like to rent: '))

        elif selection == 2:
            Return_Movies = int(input('Enter the number of movies you would like to return: '))
            while Return_Movies < 1:
                print('Cannot Return Movie that does not exist')
                Return_Movies = int(input('Enter the number of movies you would like to return:'))

        elif selection == 3:
            Books_Past_due = input("How many books are past Due?")
            if Books_Past_due > 1:
                return 


run()