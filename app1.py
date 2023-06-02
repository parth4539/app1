

start = '2010-01-01'
end = '2019-12-31'

st.title('STOCK TREND PRDICTION')

user_input = st.text_input('Enter Stock Ticker','AAPL')
df = data.DataReader(user_input,'yahoo',start,end)

#describe Data
st.subheader('Data from 2010-2019')
st.write(df.describe())

