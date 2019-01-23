def main():

    def quest1():
# Create a function with the variable below. After you create the variable do the instructions below that.
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]

        def testFunction():
            array= ["Kenn", "Kevin","Erin","Meka"] #array of names
            print(array[2])                        # a) Print the 3rd element of the numberList.
            print(array.__len__())                     # b) Print the size of the array
            array.remove("Kevin")                  # c) Delete the second element.
            print(array[2])                        # d) Print the 3rd element.
        testFunction()

    def quest2():
#Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
        def endlessloop(): #function for loop
            tired_of_this_question=""
            while(tired_of_this_question!='q'):
                tired_of_this_question= input("Please enter 'q' or 'Q' to leave exit the loop. ")
                tired_of_this_question= tired_of_this_question.lower()   #makes input lowercase
        endlessloop()                                                    tou#call loop


    def quest3():
# Create a function that contains a collection of information for the following. After you create the collection do the instructions below that.
# Jonathan/John
# Michael/Mike
# William/Bill
# Robert/Rob
        def listofNicks(): #functions for nicknames
            nicknames = {"Jonathan":"John","Michael":"Mike","William":"Bill","Robert":"Rob"}
            print(nicknames)                                           # a) Print the collection
            print(nicknames["William"])                                # b) Print William's nickname;
        listofNicks() #calls nicknames

    def quest4():
#Create an array of 5 numbers. Using a loop, print the elements in the array reverse order. Do not use a function
        arrayofNums=[2,5,4,7,8]
        for x in range(arrayofNums.__len__()):             #prints from index 0 to index arraylength -1
            print(arrayofNums[x])
        print("-----------------")
        for y in range (arrayofNums.__len__()-1,-1,-1):    #reverse from index arraylength -1 to index 0
            print(arrayofNums[y])

    def quest5():
#Create a function that will have a hard coded array then ask the user for a number. Use the userInput to state how
# many numbers in an array are higher, lower, or equal to it.
        def numduplicateFuncion():  #function to track duplicates
            array=[1,2,3,4,5,3,2,1]
            equalcount=0   #tracks equal amounts
            highcount=0    #tracks greater than amounts
            lowcount=0     #tracks less than amounts
            userNum= int(input("Enter a number. The program will tell you have many numbers are higher, lower or are equal to your number. "))
            for x in range(array.__len__()):    #for-loop through all indices
                if userNum == array[x]:  #equal
                    equalcount+=1
                elif userNum < array[x]:  #greater than input
                    highcount+=1
                elif userNum > array[x]:   #lower than input
                    lowcount+=1
            print("Numbers higher than user input:" ,highcount)
            print("Numbers lower than user input:" ,lowcount)
            print("Numbers equal to user input:" ,equalcount)
        numduplicateFuncion()  #calls function




    #quest1()
    #quest2()
    #quest3()
    #quest4()
    #quest5()

if __name__ == '__main__':
    main()