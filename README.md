**Devixo Solutions – AI/ML Internship Program**

**Task 01:** Python Programming, Data Analysis \& Visualization

**Dataset:** Hotel Booking Dataset



**Project Objective:**

Take a raw, real-world dataset through a complete data-analysis pipeline (loading, cleaning, EDA, statistical analysis, visualization and insight generation) to understand booking behaviour, pricing and cancellations in hotels.



**Dataset Description:**

Booking records for a City Hotel and a Resort Hotel in Portugal (arrivals July 2015 – August 2017). Each row is one booking with lead time, stay length, guests, price, booking channel, deposit type and cancellation status.



&#x20;             **Rows**  | **Columns** |

&#x20;    **Rows**  | 119,390 | 32      |

&#x20; **Columns** | 87,221  | 35      |



**Dataset Source:**

Kaggle – Hotel Booking Dataset (Antonio, Almeida \& Nunes, Data in Brief, 2019).



**Technologies Used:**

Python 3, Google Colab / Jupyter Notebook, Streamlit (bonus dashboard), GitHub.



**Libraries Used:**

Pandas, NumPy, Matplotlib, Seaborn, Plotly (dashboard only), Streamlit, pyngrok (to run the dashboard from Colab).



**Project Workflow:**

Dataset Selection → Data Loading → Data Understanding → Data Cleaning → Exploratory Data Analysis → Statistical Analysis → Data Visualization → Insights \& Findings → Conclusion → Documentation → GitHub



**Cleaning Summary:** dropped the nearly empty `company` column (94% missing); filled `agent`, `country`, `children`; removed 32,001 duplicate rows and 168 invalid rows (negative/extreme price, zero guests); fixed data types; renamed columns.



**Major Findings:**

\- About 27.5% of bookings are cancelled; the City Hotel cancels more (30.1%) than the Resort Hotel (23.5%).

\- Lead time is the strongest numeric driver of cancellation (median 80 days for cancelled vs 38 for kept bookings).

\- Prices are seasonal: August (153) is about twice as expensive as January (72).

\- Non-Refundable bookings are cancelled 94.7% of the time, an unexpected result.

\- Guests with parking or special requests rarely cancel.



**Visualizations:**

10 charts are in the `images/` folder, for example:



!\[Visualization 1 – Histogram: Distribution of Lead Time](images/visualization\_01.png)

!\[Visualization 2 – Bar Chart: Average Price per Night by Month](images/visualization\_02.png)

!\[Visualization 3 – Pie Chart: Booking Cancellation Share](images/visualization\_03.png)

!\[Visualization 4 – Scatter Plot: Lead Time vs. Average Daily Rate](images/visualization\_04.png)

!\[Visualization 5 – Line Chart: Monthly Bookings Over Time](images/visualization\_05.png)

!\[Visualization 6 – Box Plot: Price by Customer Type](images/visualization\_06.png)

!\[Visualization 7 – Correlation Heatmap](images/visualization\_07.png)

!\[Visualization 8 – Count Plot: Bookings by Deposit Type and Cancellation](images/visualization\_08.png)

!\[Visualization 9 – Pair Plot](images/visualization\_09.png)

!\[Visualization 10 – Violin Plot: Lead Time by Cancellation Status](images/visualization\_10.png)



**Project Structure:**



Task\_01\_AI\_ML/

├── dataset/        hotel\_bookings.csv, hotel\_bookings\_cleaned.csv

├── notebook/       Task\_01\_Data\_Analysis.ipynb

├── images/         visualization\_01.png ... visualization\_10.png

├── report/         Task\_01\_Report.pdf

├── app/            app.py  (Streamlit dashboard)

└── README.md



**How to Run the Project:**

1\. Open `notebook/Task\_01\_Data\_Analysis.ipynb` in Google Colab (upload it, or use "Open in Colab" from GitHub).

2\. Click Runtime → Run all. The dataset downloads automatically; if it fails, upload `hotel\_bookings.csv` when asked.

3\. (Optional dashboard) Paste your free ngrok authtoken into the `NGROK\_TOKEN` line in the bonus cell, run it, and open the printed link (click Visit Site on the ngrok warning page).



**To run the dashboard locally instead:**

bash

pip install streamlit plotly pandas

streamlit run app/app.py


**Student Name:** Aman Siddiqui


