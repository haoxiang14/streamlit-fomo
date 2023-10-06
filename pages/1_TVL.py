import streamlit as st
import streamlit.components.v1 as components
import requests

response = requests.get("https://api.llama.fi/protocol/solana")
print(response.json())


st.header("Solana TVL")
# components.html("""
# <script src="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"></script>
# <coingecko-coin-price-chart-widget currency="usd" coin-id="solana" locale="en" height="300"></coingecko-coin-price-chart-widget>""")



# components.iframe("https://defillama.com/chart/chain/Solana?&theme=dark", width=300, height=300, scrolling=False)
st.write("Source: https://defillama.com/chain/Solana")