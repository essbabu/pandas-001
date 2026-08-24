
import urllib.request
import pandas as pd
url="https://en.wikipedia.org/wiki/list_of_countries_and_dependencies_by_population"
request=urllib.request.Request( url,headers={"User-Agent":"Mozilla/5.0 ("}, )
response=urllib.request.urlopen(request)

tables=pd.read_html(response.read())
print(f'Total tables: {len(tables)}')
df=tables[0]
df.to_csv("a.csv")
print(df)

