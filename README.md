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

