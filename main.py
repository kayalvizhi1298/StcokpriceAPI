#Worked on july 07-07-2023 by C.kayal vizhi

from fastapi import FastAPI
import requests
# import uvicorn
from bs4 import BeautifulSoup
app = FastAPI()
@app.get('/stock')
def analytics_scrapper(ticker:str):
   
    url = f'https://www.screener.in/company/{ticker}/'
    response = requests.get(url)
    
    soup=BeautifulSoup(response.text,'html.parser')
    
    companys = soup.find_all('li',class_='flex flex-space-between')
    analysis={}
    for company in companys:
        company_name = company.find('span',class_='name').text
        company_value = company.find('span',class_='nowrap value').text
        key=company_name.replace('\n',"").strip()
        value=company_value.replace('\n',"") 
        firstvalue=value.split()
        secondvalue=' '.join(firstvalue)
        analysis[key] = secondvalue
    return analysis
@app.get('/get_stock')
def get_data():
    tickers = ['ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV', 'BHARTIARTL', 'BPCL',
               'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFCBANK',
               'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'HDFC', 'ICICIBANK', 'INDUSINDBK', 'INFY', 'ITC',
               'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NESTLEIND', 'NTPC', 'ONGC', 'POWERGRID', 'RELIANCE',
               'SBILIFE', 'SHREECEM', 'SBIN', 'SUNPHARMA', 'TCS', 'TATAMOTORS', 'TATASTEEL', 'TATACONSUM', 'TECHM', 'TITAN',
               'ULTRACEMCO', 'UPL', 'WIPRO']
    data = {}
    import json
    for ticker in tickers:
        analysis = analytics_scrapper(ticker)
        data[ticker] = analysis
    
    return data


# if __name__           == "__main__":
#     uvicorn.run("main.app",host ='0.0.0.0',reload=True,port ='8000')

# tickers=['ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV', 'BHARTIARTL', 'BPCL', 
#           'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFCBANK', 
#           'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'HDFC', 'ICICIBANK', 'INDUSINDBK', 'INFY', 'ITC',
#           'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NESTLEIND', 'NTPC', 'ONGC', 'POWERGRID', 'RELIANCE',
#           'SBILIFE', 'SHREECEM', 'SBIN', 'SUNPHARMA', 'TCS', 'TATAMOTORS', 'TATASTEEL', 'TATACONSUM', 'TECHM', 'TITAN',
#           'ULTRACEMCO', 'UPL', 'WIPRO']
# data={}
# for ticker in tickers:
#     User = analytics_scrapper(ticker)
#     keys=ticker
#     if keys not in data:
#         data[keys]= User
    
# json.dump(User,open('D:/FINANCE ANALAYIS/data.json','wt'),indent=4)
# dataset=json.load(open('D:/FINANCE ANALAYIS/data.json','rt'))
# print(dataset)
# nifty_50 = {
#     'Adani Ports and Special Economic Zone Ltd.': 'ADANIPORTS.NS','Asian Paints Ltd.': 'ASIANPAINT.NS','Axis Bank Ltd.': 'AXISBANK.NS','Bajaj Auto Ltd.': 'BAJAJ-AUTO.NS','Bajaj Finance Ltd.': 'BAJFINANCE.NS',
#     'Bajaj Finserv Ltd': 'BAJAJFINSV.NS','Bharti Airtel Ltd.': 'BHARTIARTL.NS','Bharat Petroleum Corporation Ltd.': 'BPCL.NS','Britannia Industries Ltd.': 'BRITANNIA.NS',
#     'Cipla Ltd': 'CIPLA.NS','Coal India Ltd.': 'COALINDIA.NS','Divi\'s Laboratories Ltd.': 'DIVISLAB.NS','Dr. Reddy\'s Laboratories Ltd.': 'DRREDDY.NS',
#     'Eicher Motors Ltd': 'EICHERMOT.NS','Grasim Industries Ltd.': 'GRASIM.NS','HCL Technologies Ltd.': 'HCLTECH.NS',
#     'HDFC Bank Ltd': 'HDFCBANK.NS','HDFC Life Insurance Company Ltd.': 'HDFCLIFE.NS','Hero MotoCorp Ltd.': 'HEROMOTOCO.NS','Hindalco Industries Ltd.': 'HINDALCO.NS','Hindustan Unilever Ltd.': 'HINDUNILVR.NS','Housing Development Finance Corporation Ltd. (HDFC)': 'HDFC.NS',
#     'ICICI Bank Ltd': 'ICICIBANK.NS','IndusInd Bank Ltd.': 'INDUSINDBK.NS','Infosys Ltd.': 'INFY.NS','ITC Ltd.': 'ITC.NS',
#     'JSW Steel Ltd': 'JSWSTEEL.NS','Kotak Mahindra Bank Ltd.': 'KOTAKBANK.NS','Larsen & Toubro Ltd. (L&T)': 'LT.NS','Mahindra & Mahindra Ltd. (M&M)': 'M&M.NS',
#     'Maruti Suzuki India Ltd': 'MARUTI.NS','Nestle India Ltd.': 'NESTLEIND.NS','NTPC Ltd.': 'NTPC.NS','Oil and Natural Gas Corporation Ltd. (ONGC)': 'ONGC.NS',
#     'Power Grid Corporation of India Ltd.': 'POWERGRID.NS', 'Reliance Industries Ltd.': 'RELIANCE.NS','SBI Life Insurance Company Ltd.': 'SBILIFE.NS','Shree Cement Ltd.': 'SHREECEM.NS',
#     'State Bank of India (SBI)': 'SBIN.NS','Sun Pharmaceutical Industries Ltd.': 'SUNPHARMA.NS','Tata Consultancy Services Ltd. (TCS)': 'TCS.NS','Tata Motors Ltd.': 'TATAMOTORS.NS',
#     'Tata Steel Ltd.': 'TATASTEEL.NS','Tata Consumer Products Ltd.': 'TATACONSUM.NS','Tech Mahindra Ltd.': 'TECHM.NS','Titan Company Ltd.': 'TITAN.NS',
#     'UltraTech Cement Ltd.': 'ULTRACEMCO.NS','UPL Ltd.': 'UPL.NS','Wipro Ltd.': 'WIPRO.NS'
# }
