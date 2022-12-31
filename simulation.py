'''
Script to simulate the porftolio
'''

import yfinance as yf
import datetime 
import pandas as pd
import numpy as np
from datetime import timedelta
from bcb import sgs
from bcb import currency
import risk_kit
import matplotlib.pyplot as plt

plt.style.context('ggplot')

def rebalance_portfolio(lista_capital, lista_weights):
  '''
  Given a list with different amounts of capital, and a list with weights, 
  it returns a list with the capitals rebalenced given the weights.
  '''
  if len(lista_weights) != len(lista_capital):
    raise Exception('The length of the lista_capital must be the same of the lista weights')

  total_capital = 0
  for capital in lista_capital:
    total_capital += capital

  new_lista_capital = []
  for weigth in lista_weights:
    new_value = total_capital*weigth
    new_lista_capital.append(new_value)

  return new_lista_capital


def compute_historic_return(portfolio, lista_weights, rebalance = True, aggregated=True):
  '''
  It computes the historical return of a portfolio (dataframe), given a list of weights.
  input:
    portfolio:
      - df with the daily returns, and each asset in a different column
    lista_weights:
      - list with weights in decimal format
    rebalance
      - if true, it rebalances every month, coming back to the original weights
    aggregated
      - if aggregated is false, then it returns the historical performance for each asset
  '''
  df = portfolio.copy()
  df = df.fillna(0)

  start_pat = 1000
  historic_pat = [[start_pat*weight for weight in lista_weights]]

  month_before = df.iloc[0].name.month
  for index_row in range(df.shape[0]):
    row = df.iloc[index_row]
    month = row.name.month
    
    lista_row = []
    i_column = 0
    if month != month_before and rebalance:
      #If it changed the month, the portfolio is rebalanced

      #Get the latest list with the capitals in each asset
      actual_list_capital = historic_pat[-1]

      #Rebalance the list of capitals for each asset given a list of weights
      rebalenced_capital = rebalance_portfolio(actual_list_capital, lista_weights)
      historic_pat[-1] = rebalenced_capital

      #The old month becomes the new month
      month_before = month

    for asset in row.index:
      return_ = row[asset]
      pat_before = historic_pat[index_row][i_column]
      #print(asset, pat_before)
      value = pat_before*(1+return_)
      lista_row.append(value)
      i_column+=1

    historic_pat.append(lista_row)

  #Create the DataFrame with the results
  start_day = df.index[0] - timedelta(days=1)
  historic_pat = pd.DataFrame(historic_pat)
  historic_pat.columns = df.columns
  historic_pat.index = [start_day] + list(df.index)

  if aggregated == False:
    return historic_pat
  
  aggregated = historic_pat.sum(axis=1)

  return aggregated.pct_change()[1:]


def create_stock_portfolio(lista_assets, start_date = None):
  '''
  It Returns a dataframe with the assets given in the list
  '''
  all_data = []
  start_dates = []
  for stock in lista_assets:
    data = yf.download(stock, interval='1d').Close
    start_dates.append(data.index[0])
    all_data.append(data)

  if start_date == None:
    max_start_date = max(start_dates)
  else:
    max_start_date = start_date

  df = pd.concat(all_data, axis = 1)
  df.columns = lista_assets
  df.resample('1D').ffill()

  df.fillna(method='ffill', inplace=True)

  #Slices the df
  sliced_df = df[max_start_date:]

  #for the nan values, it fills with the previous value
  sliced_df.fillna(method='bfill', inplace=True)
    
  return sliced_df


#Collect data BOVA
bova = create_stock_portfolio(['BOVA11.SA'])['2015':]
bova = bova.pct_change()[1:]

#Collect IVV data in dollars, transform it in reais, and compute its return
ivv_raw  = pd.DataFrame(yf.download('IVV', interval='1d').Close)['2015':]
ivv_raw.columns = ['IVV']
cy = currency.get(['USD'], start='2015-1-01', end='2022-12-30')
ivv_and_dollar = pd.concat([ivv_raw, cy], axis=1)
ivv_and_dollar.fillna(method='ffill', inplace=True)
ivv_real = ivv_and_dollar["IVV"].multiply(ivv_and_dollar["USD"], axis="index")
ivv_real = ivv_real.pct_change()[1:]
ivv_real = pd.DataFrame(ivv_real)
ivv_real.columns = ['IVV']

cdi = sgs.get({'cdi':12}, start = '2015-01-01')/100

ipca_long = sgs.get({'ima_b_5_more':12468}, start = '2015-01-01')
ipca_long_ret = ipca_long.pct_change()[1:]

ipca_short = sgs.get({'ima_b_5':12467}, start = '2015-01-01')
ipca_short_ret = ipca_short.pct_change()[1:]

lista_assets = [bova, ivv_real, cdi, ipca_long_ret, ipca_short_ret]

port = pd.concat(lista_assets, axis =1)
port.columns = ['BOVA','IVV', 'CDI', 'IMAB-5+', 'IMAB-5']
port = port.fillna(0)

port_rebalanced = compute_historic_return(port, [0.2, 0.3, 0.2,0.1,0.2])
port_no_rebalance = compute_historic_return(port, [0.2, 0.3, 0.2,0.1,0.2], rebalance=False)

testing = pd.concat([port, port_rebalanced, port_no_rebalance], axis = 1)
testing.columns = list(port.columns) + ['Portfolio Rebalanced', 'Portfolio Not-Rebalanced']
stats = risk_kit.summary_stats(testing, riskfree_rate=0.083481, periods_per_year=252)
print(stats)

ax = ((testing+1).cumprod()-1).plot(title='Accumulated Return for Individual Assets and Portfolios')
fig = ax.get_figure()
fig.savefig('plots/aggregated_return.png')

# Analyse weights over time
port_rebalanced = compute_historic_return(port, [0.2, 0.3, 0.2,0.1,0.2],aggregated=False)
port_no_rebalance = compute_historic_return(port, [0.2, 0.3, 0.2,0.1,0.2], rebalance=False,aggregated=False)

def weight_over_time(portfolio):
  '''
  Function that return the weight of the asset in a given porftolio (dataframe) over time 
  where each asset is in a column, and the portfolio is in capital not in RETURNS.
  '''
  df = portfolio.copy()
  df['Total'] = df.sum(axis=1)

  result = df[portfolio.columns].div(df.Total, axis=0)

  return   result

ax = weight_over_time(port_rebalanced).plot(title = 'Weight over Time Rebalanced Portfolio')
fig = ax.get_figure()
fig.savefig('plots/weights_rabalanced.png')

ax = weight_over_time(port_no_rebalance).plot(title = 'Weight over Time Not-Rebalanced Portfolio')
fig = ax.get_figure()
fig.savefig('plots/weights_non-rabalanced.png')

