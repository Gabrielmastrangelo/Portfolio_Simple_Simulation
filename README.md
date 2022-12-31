# Simulating Portfolios with Brazilian assets

## Content:
+ risk_kit.py: library for investment management developed in the course **Introduction to Portfolio Construction and Analysis with Python**.
+ simulation.py: script in python to simulate, compute some basic stats, and analyse asset weight behavior over time.
<br>
**Obs:** In addition, we also utilize the library python-bcb, which facilitates collecting the data from the Central Bank of Brazil.

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
![alt text](h[ttp://url/to/img.png](https://github.com/Gabrielmastrangelo/Portfolio_Simple_Simulation/blob/main/plots/aggregated_return.png))

