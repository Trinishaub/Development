import csv     # imports the csv module
import sys      # imports the sys module


####################### set the dictionary with the key values on how the function is going to be sorted######################
orderList = {}
orderList["Managing Director"] = 0
orderList["Senior Vice-President"] = 1
orderList["Vice-President"] = 2
orderList["Senior Wealth Advisor"] = 3
orderList["Wealth Advisor"] = 4
orderList["Associate Wealth Advisor"] = 5
orderList["Senior Investment Advisor"] = 6
orderList["Investment Advisor"] = 7
orderList["Associate Investment Advisor"] = 8
orderList["Portfolio Manager"] = 9 
orderList["Associate Portfolio Manager"] = 10
orderList["Branch Manager"] = 11 
orderList["Assistant Branch Manager"] =12
orderList["Financial Planner"] = 13

#############################

def openCSV(inputFile,outputFile):
  f = open(inputFile, 'rb') # opens the csv file
  w = open(outputFile,'wb') # opens the csv write file
  try:
      reader = csv.reader(f)
      writer = csv.writer(w)  # creates the reader object
      for row in reader:   # iterates the rows of the file in orders
         
          row[1] = sortRow(stringToList(row[1])) #sort the function at the Title location in the CSV 
          writer.writerow(row) #write the newly sorted row into csv file.
                   
  finally:
      f.close()      # closing
      w.close()  


def stringToList(string):
  
  return string.split(",")

def sortRow(lstring):
  sortedList =[] ## list that the values are going to be sorted.
  for s in lstring:
    if (s not in orderList):
     orderList[s] = [len(orderList),s]
    
    sortedList.append([orderList[s],s])
  
  sortedList = sorted(sortedList)
  sortedString = ""
  for i in xrange(0,len(sortedList)):
    if (len(sortedList)-1 ==i):
      sortedString = sortedString + sortedList[i][1] 
    else:
    
      sortedString = sortedString + sortedList[i][1] + ","


  return sortedString


def main(argv):

  openCSV(argv[0],argv[1])

if __name__ == "__main__":
    main(sys.argv)
  