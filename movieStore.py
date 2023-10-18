

class MovieStore:

    #constructor
    def __init__(self,store_name,total_number_of_movies_available,rental_fee_per_movie,late_fee_per_day):
            self._storeName = store_name
            self._totalNumberOfMovies = total_number_of_movies_available
            self._numberOfAvailableMovies = total_number_of_movies_available
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
    def setStoreName(self,storeName):
        self._storeName = storeName
    
    def setTotalNumberofMovies(self,totalNumberOfMovies):
        self._totalNumberOfMovies = totalNumberOfMovies
    
    def setNumberOfAvailableMovies(self,numberOfAvailableMovies):
        self._numberOfAvailableMovies = numberOfAvailableMovies
    
    def setRentalFee(self,rentalFeePermovie):
        self._rentalFeePerMovie = rentalFeePermovie
    
    def setLateFeePerDay(self,lateFeePerDay):
        self._lateFeePerDay = lateFeePerDay

    
    
