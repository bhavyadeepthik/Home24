# SenAnalistCSH24

Given
  - MarketPriceSampleCaseStudy.csv : sample data of current market prices

Goal
  - Price multiplier for other countries considering DE as baseline for each Category and sub-category

Assumptions:
  - 'id' column in MarketPriceSampleCaseStudy.csv is assumed to be <..>_<..>_<country>_<..>
  - country label with 'DE' is considerd as base price
  - country label other than 'DE' is considerd to calculate price multiplier for each country, category and sub-category
  - price for each country is estimated by taking mean of all valid occurances in both 'google_shopping_price' and 'priceAPI' 
  

  
Output:
  - ./Data/New_multipliers.csv is generated from scirpt './Script/country_multiplier.py'
