# Simulating Portfolios with Brazilian Assets

## Content:
+ risk_kit.py: library for investment management developed in the course **Introduction to Portfolio Construction and Analysis with Python**.
+ simulation.py: script in python to simulate, compute some basic stats, and analyse asset weight behavior over time.
<br>
**OBS**: In addition, we also utilize the library python-bcb, which facilitates collecting the data from the Central Bank of Brazil. This library was developed by [Wilson Freitas](https://www.linkedin.com/in/wilson-freitas/?locale=pt_BR), an great Brazillian quant.

## Assets used in the Simulation

+ BOVA11: proxy for the Brazillian Stock Market performance.
+ IVV: proxy for the USA Stock Market performance.
+ CDI rate: the Brazilian interbank deposit rate, which is an average of interbank overnight rates in Brazil.
+ IMA-B 5: basket of goverment bonds that give a cupon + inflation rate, with less than 5 years of maturity.
+ IMA-B 5+: basket of goverment bonds that give a cupon + inflation rate, with more than 5 years of maturity.

## Portfolio

The chosen portfolio is composed of:
| Assets | Weights |
| ----------- | ----------- |
| BOVA11 | 20% |
| IVV | 30% |
| CDI | 20% |
| IMA-B 5 | 10% |
| IMA-B 5+ | 20% |

## Historical Performance of Individual Assets and the Portfolios
### Plotting Cumulative Return
![Alt text](plots/aggregated_return.png?raw=true "Title")

### Portfolio Metrics
|                          |   Annualized Return |   Annualized Vol |   Skewness |   Kurtosis |   Cornish-Fisher VaR (5%) |   Historic CVaR (5%) |   Sharpe Ratio |   Max Drawdown |
|:-------------------------|--------------------:|-----------------:|-----------:|-----------:|--------------------------:|---------------------:|---------------:|---------------:|
| BOVA                     |           0.103875  |       0.255146   |  -0.657562 |   15.2042  |               0.0248238   |          0.0362012   |    0.0737549   |     -0.469317  |
| IVV                      |           0.169149  |       0.221214   |   0.337609 |    8.11282 |               0.0193944   |          0.0300408   |    0.357503    |     -0.315595  |
| CDI                      |           0.0834811 |       0.00259073 |  -0.131444 |    1.70739 |              -3.95591e-05 |         -5.36506e-05 |    5.05456e-05 |      0         |
| IMAB-5+                  |           0.110605  |       0.114774   |  -1.18561  |   44.6065  |               0.00762286  |          0.0156972   |    0.218166    |     -0.187056  |
| IMAB-5                   |           0.107143  |       0.0315055  |  -3.01491  |   45.0537  |               0.0025355   |          0.00435255  |    0.693397    |     -0.0537667 |
| Portfolio Rebalanced     |           0.130641  |       0.096355   |  -0.457169 |   15.5435  |               0.00870436  |          0.0133886   |    0.451858    |     -0.193758  |
| Portfolio Not-Rebalanced |           0.124293  |       0.108614   |  -0.378992 |   14.1007  |               0.0099491   |          0.0152618   |    0.346898    |     -0.208792  |

## Portfolio Asset's Weight Behavior Over Time

### Not-rebalanced Portfolio
![Alt text](plots/weights_non-rabalanced.png?raw=true "Title")

### Rebalanced Portfolio
![Alt text](plots/weights_rabalanced.png?raw=true "Title")


## Conclusion

We can see that the Rebalanced Portfolio has the biggest Sharp ratio over the period, which means it had the best relationship between return and risk.
<br>
There are many ways to rebalance asset portfolios, and the MOOC course on Coursera _Investment Management with Python and Machine Learning Specialization_ introduce many of them, I strongly recommend it. 
<br>
A simple and disciplined asset allocation methodology should be the way to go for the majority of the investors.
