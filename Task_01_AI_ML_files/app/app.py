import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Hotel Booking Dashboard", layout="wide")
st.title("🏨 Hotel Booking Demand Dashboard")

@st.cache_data
def load():
    return pd.read_csv("dataset/hotel_bookings_cleaned.csv", parse_dates=["arrival_date"])

df = load()

st.sidebar.header("Filters")
hotel = st.sidebar.multiselect("Hotel", df["hotel"].unique(), default=list(df["hotel"].unique()))
year = st.sidebar.multiselect("Arrival Year", sorted(df["arrival_year"].unique()), default=list(sorted(df["arrival_year"].unique())))
seg = st.sidebar.multiselect("Market Segment", df["market_segment"].unique(), default=list(df["market_segment"].unique()))
f = df[df["hotel"].isin(hotel) & df["arrival_year"].isin(year) & df["market_segment"].isin(seg)]

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Records", f"{len(f):,}")
c2.metric("Total Columns", df.shape[1])
c3.metric("Cancellation Rate", f"{f['is_cancelled'].mean()*100:.1f}%")
c4.metric("Avg Daily Rate", f"{f.loc[f['average_daily_rate']>0,'average_daily_rate'].mean():.0f}")
c5.metric("Avg Lead Time", f"{f['lead_time'].mean():.0f} days")

a, b = st.columns(2)
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
price = f[f["average_daily_rate"] > 0].groupby("arrival_month")["average_daily_rate"].mean().reindex(months).reset_index()
a.plotly_chart(px.bar(price, x="arrival_month", y="average_daily_rate", title="Average Daily Rate by Month"), use_container_width=True)
canc = f.groupby("market_segment")["is_cancelled"].mean().mul(100).reset_index()
b.plotly_chart(px.bar(canc, x="market_segment", y="is_cancelled", title="Cancellation Rate (%) by Market Segment"), use_container_width=True)

st.plotly_chart(px.histogram(f, x="lead_time", nbins=50, color="hotel", title="Lead Time Distribution"), use_container_width=True)

st.subheader("Correlation")
cols = ["is_cancelled","lead_time","average_daily_rate","total_nights","special_requests","parking_spaces","booking_changes"]
st.plotly_chart(px.imshow(f[cols].corr().round(2), text_auto=True, color_continuous_scale="RdBu_r", zmin=-1, zmax=1), use_container_width=True)

st.subheader("Summary Statistics")
st.dataframe(f[["lead_time","average_daily_rate","total_nights","special_requests"]].describe().round(2))

st.subheader("Key Insights")
st.markdown("""
- About 1 in 4 bookings is cancelled; longer lead time means a higher cancellation risk.
- Prices peak in summer (August) and are lowest in winter.
- Online TA bookings cancel most; Corporate and Direct cancel least.
- Guests with parking or special requests rarely cancel.
""")
