import pandas as pd

# Scrape the HTML data
url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2023"
tables = pd.read_html(url)


tables
print('abc')

# # Extract the relevant table from the scraped HTML data
# treasury_yield = tables[1].iloc[1:4]

# # Parse the table data and insert it into the database
# date = treasury_yield.iloc[0][0]
# bc_1month = float(treasury_yield.iloc[0][1])
# bc_2month = float(treasury_yield.iloc[1][1])
# bc30year = float(treasury_yield.iloc[2][1])