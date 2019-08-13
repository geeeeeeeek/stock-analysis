import warnings
import tushare as ts
warnings.filterwarnings("ignore")

token = "4907b8834a0cecb6af0613e29bf71847206c41ddc3e598b9a25a0203"

ts.set_token(token)

pro = ts.pro_api()

# all
# data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

# single
data = df = pro.query('daily', ts_code='000001.SZ', start_date='20190701', end_date='20190711')

print(data)
