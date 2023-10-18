

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
    

    def calculateLateFee(self):
        numberOfDays = input("Input the Number of Days: ")
        return numberOfDays * self._lateFeePerDay
    
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
        return "Store name: {} | Total Number of Movies: {} | Number of available Movies: {} | Rental Fee Per Movie:  {} | Late Fee Per Day {}".format(self._storeName,self._totalNumberOfMovies,self._numberOfAvailableMovies,self._rentalFeePerMovie,self._lateFeePerDay) 

    

def run():
    Store1 = MovieStore("Nawaf's Store",9,10,3.95,5.99)
    

              

    

