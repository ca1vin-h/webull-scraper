This readme applies to everyminute.zip

Webull One Minute Data
	Contains the oldest available data - when webull locked down their api
	Data is organized into candlesticks
		/USA49k1d/ contains one day candlesticks
		All other folders contain one second candlesticks

TICKERIDKEY.xlsx 
	Contains all of the TickerIDs, stock names, company names, and other information.
		Column A: TickerID: Unique number provided by webull used to indentify individual files
		Column B: Ticker: Code used to represent company on stock market
		Column C: Full Company Name
		Column D: Currency
		Column E: Exchange
		Column F: security type
		Column G: Country code

	Consists of 12 tabs, each containing rows of stocks and securities
	Each tab is associated with a folder in /everyminute/
		TickerID92K: Full list of all stocks and securities available
		idlist: ten test tickers
		priorityID: important stocks and ETFs
		lowvolaetf: low volatility etfs
		forex: Foreign currency exchange
		Invesco: all tickers found on webull associated with Invesco
		Ishares: all tickers found on webull associated with Ishares
		goldman: all tickers found on webull associated with goldman
		jpmorgan: all tickers found on webull associated with jpmorgan
		MorganStanley: all tickers found on webull associated with MorganStanley
		black: all tickers found on webull associated with black
		mainstay: all tickers found on webull associated with mainstay
		
File Naming:
	Each tab of TICKERIDKEY.xlsx is associated with a folder in /everyminute/
	Files are contained within each folder
	
	

	Finding a file
		Files are named by TickerID, 
		To find a stock search TICKERIDKEY.xlsx for the ticker or company you are looking for and copy the ticker ID in column a 
		Search /everyminute/ for the ID
		Ensure data is in one minute intervals (60 seconds)

Data:
	Data is in CSV format with the following columns. Data is in one minute candlestick format
	NOTE: Some of the data is in one day, one hour, or one minute format. Each folder is named to hint what it is but I will come back and fix this at another time with all of the folder names
		0: Timestamp
			Unix timestamp in seconds
				1694793040 is Fri Sep 15 2023 11:50:40 GMT-0400 (Eastern Daylight Time)
			Data is in one minute intervals (60 seconds)
		1: Open
		2: Close
		3: High
		4: Low
		6: Unknown*
		7: Volume
		8: Unknown*
	*Data can be viewed if you visit https://app.webull.com/trade, open devtools>network, then scroll through data on page 
