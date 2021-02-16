#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <Tankokhwee>
#Group Name: <KGN>
#Class: <PN2004J>
#Date: <9/2/2021>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################


#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
	def __init__(self):

		#load excel data (CSV format) to dataframe - 'df'
		dataframe = pd.read_csv('MonthyVisitors.csv')
		#show specific country dataframe
		sortCountry(dataframe)


#########################################################################
#CLASS Branch: End of Code
#########################################################################


#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

	#print number of rows in dataframe
  print("There are " + str(len(df)) + " data rows read. \n")

	#display dataframe (rows and columns)
  print("The following dataframe are read as follows: \n")

  select_country = (df[['Year', 'Month', ' Brunei Darussalam ', ' Indonesia ', ' Malaysia ', ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ']][216:348])
  print(select_country)


  select_country[' Myanmar '] = pd.to_numeric(select_country[' Myanmar '],errors='coerce')

  select_country = select_country.dropna(subset=[' Myanmar '])


  select_country[' Myanmar '] = select_country[' Myanmar '].astype(int)
  select_country[' Brunei Darussalam '] = select_country[' Brunei Darussalam '].astype(int)
  select_country[' Indonesia '] = select_country[' Indonesia '].astype(int)
  select_country[' Malaysia '] = select_country[' Malaysia '].astype(int)
  select_country[' Thailand '] = select_country[' Thailand '].astype(int)
  select_country[' Viet Nam '] = select_country[' Viet Nam '].astype(int)
  select_country[' Philippines '] = select_country[' Philippines '].astype(int)


  

  
  new = select_country.drop(['Year', 'Month'], axis =1)

  total = new.sum()

  sortedvalue = total.sort_values(ascending=False)

  print("\n" +"The Top 3 countries of visitors That have visited Singapore from 1996 to 2006 over the span of 10 years:")
  print(sortedvalue.head(n=3))

  



  













  #Display the top 3 countries that visited Singapore over the span of 10 years
	#print("\n" +"The Top 3 countries of visitors to Singapore from the selected region over the span of 10 years:")
	#print(select_country.iloc[216:348 , 3:8].sum(axis=0).sort_values(ascending=False).nlargest(3))


  return


#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':

	#Project Title
	print('######################################')
	print('# Data Analysis App - PYTHON Project #')
	print('######################################')

	#perform data analysis on specific excel (CSV) file
	DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################
