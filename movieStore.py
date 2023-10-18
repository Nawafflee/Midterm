

class MovieStore:

    #constructor
    def __init__(self,store_name,total_number_of_movies_available,number_of_available_movies,rental_fee_per_movie,late_fee_per_day):
            self._storeName = store_name
            self._totalNumberOfMovies = total_number_of_movies_available
            self._numberOfAvailableMovies = number_of_available_movies
            self._rentalFeePerMovie = rental_fee_per_movie
            self._lateFeePerDay = late_fee_per_day


    #Getters
    def getStoreName(self):
        return self._storeName
    
    def getTotalNumberOfMovies(self):
        return self._totalNumberOfMovies
    
    def getNumberOfAvailableMovies(self):
        return self._numberOfAvailableMovies
    
    def getRentalFeePerMovie(self):
        return self._rentalFeePerMovie
    
    def getLateFeePerDay(self):
        return self._lateFeePerDay
    
    #setters
    
    def setRentalFee(self,rentalFeePermovie):
            if rentalFeePermovie < 0:
                return "Rejected Variable"
            else:
                return rentalFeePermovie
    

    def calculateLateFee(self,numberOfDays,lateFee):
        return numberOfDays * lateFee
    
    def rentMovie(self,moviesToRent,numberOfAvailableMovies):
        moviesToRent = moviesToRent - numberOfAvailableMovies     
        if moviesToRent > numberOfAvailableMovies :
            return True
        else:
             return False
    
    def returnMovie(self,numberOfMoviesReturned,numberOfAvailableMovies):
        number_of_overdue_days = input("Number of Overdue days: ")
        lateFee = None
        if number_of_overdue_days > 0:
            number_of_overdue_days * lateFee
            numberOfMoviesReturned +=1
            numberOfAvailableMovies +=1
    
    def __str__(self):
        return "Store name: {} | Total Number of Movies: {} | Rental Fee Per Movie:  {} | Late Fee Per Day {}".format(self._storeName,self._totalNumberOfMovies,self._rentalFeePerMovie,self._lateFeePerDay) 


Store1 = MovieStore("Nawaf's Store",9,10,3.95,5.99)
#print(Store1)
"""
def run():
    while True:

            Store1 = MovieStore()

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


            elif selection == 4:
                quit()


run()
"""