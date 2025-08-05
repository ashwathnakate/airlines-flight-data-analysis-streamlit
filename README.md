
# ✈️ Airlines Flights Data Analysis Dashboard

Deployment can be found at 👉 https://airlines-flight-data-analysis.streamlit.app/

This project presents a professional Streamlit dashboard built for analyzing airline flights data. It provides interactive and insightful visualizations to uncover trends, understand flight pricing, and support strategic decisions in the airline industry.

---

## 📦 Dataset Overview

The dataset contains records of flights including the following columns:

- `airline`: Airline operating the flight  
- `flight`: Flight number  
- `source_city`: Origin city  
- `departure_time`: Category of departure time (Morning, Evening, etc.)  
- `stops`: Number of stops (Non-stop, 1 Stop, etc.)  
- `arrival_time`: Category of arrival time  
- `destination_city`: Destination city  
- `class`: Travel class (Economy/Business)  
- `duration`: Total travel time  
- `days_left`: Days left for the flight from the booking date  
- `price`: Ticket price in local currency

---

## 🚀 Features

- ✅ General data overview: record count, airline count, and city count  
- 📈 Airline vs Average Price bar chart  
- 🕒 Duration vs Price line chart  
- ⏱️ Departure Time Category vs Average Price bar chart  
- 🛫 Source and Destination vs Price box plots  
- 🧠 Correlation Heatmap  
- 🎯 Fully interactive filters

---

## 🧰 Tech Stack

- **Python 3.8+**
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Seaborn**

---

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/airlines-flights-dashboard.git
cd airlines-flights-dashboard
```

### 2. Install Requirements

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Launch the Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
airlines-flights-dashboard/
│
├── dataset/
│   └── airlines_flights_data.csv       # Dataset file 
├── app.py                              # Streamlit app script
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation

```

---

## 📝 Requirements

Save this as `requirements.txt`:

```
streamlit
pandas
matplotlib
seaborn
```

---

## 📄 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this project with attribution.

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Seaborn](https://seaborn.pydata.org/)
- Dataset inspired by public airline data available on [Kaggle](https://www.kaggle.com)

---

