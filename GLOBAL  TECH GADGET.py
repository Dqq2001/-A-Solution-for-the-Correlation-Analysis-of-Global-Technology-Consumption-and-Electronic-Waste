import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA as OldARIMA
from scipy.stats import pearsonr
import os
import statsmodels.api as sm
path = r"C:\Users\Administrator\.cache\kagglehub\datasets\atharvasoundankar\global-tech-gadget-consumption-data-2015-2025\versions\1"
print(os.listdir(path))
# upload dataset
df = pd.read_csv(os.path.join(path,"Global_Tech_Gadget_Consumption.csv"))




# data preview and basic cleanprint("basic information：")
print(df.info())
print("\nThe first 5 rows：")
print(df.head())
# Electronic Waste Source Traceability: Correlation Analysis of Products and Waste
df['Year'] = pd.to_datetime(df['Year'], format='%Y') # Timeline
df = df.fillna({
    'Smartphone Sales (Millions)': df['Smartphone Sales (Millions)'].mean(),
    'Laptop Shipments (Millions)': df['Laptop Shipments (Millions)'].mean(),
    'E-Waste Generated (Metric Tons)': df['E-Waste Generated (Metric Tons)'].mean()
}) # if there is null use mean
#                """Analyze correlation between product sale"""
def analyze_e_waste_correlation(df, country):
    country_df = (
        df[df['Country'] == country]
        .sort_values('Year')
        .copy()
    )

    smartphone_lag_map = {'USA': 1, 'China': 2}
    smartphone_lag = smartphone_lag_map.get(country, 1)
    laptop_lag = 2

    country_df['Smartphone_Sales_Lag'] = (
        country_df['Smartphone Sales (Millions)'].shift(smartphone_lag)
    )
    country_df['Laptop_Shipments_Lag'] = (
        country_df['Laptop Shipments (Millions)'].shift(laptop_lag)
    )

    valid_df = country_df.dropna()

    corr_smartphone = pearsonr(
        valid_df['Smartphone_Sales_Lag'],
        valid_df['E-Waste Generated (Metric Tons)']
    )
    corr_laptop = pearsonr(
        valid_df['Laptop_Shipments_Lag'],
        valid_df['E-Waste Generated (Metric Tons)']
    )

    # ======== 画图 ========
    # ======== 画图 ========
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    years = valid_df['Year'].dt.year

    # --- Smartphone vs E-Waste ---
    ax1.plot(
        years,
        valid_df['Smartphone_Sales_Lag'],
        label=f'Smartphone Sales (lag {smartphone_lag} yr)',
        color='blue'
    )

    ax1_t = ax1.twinx()
    ax1_t.plot(
        years,
        valid_df['E-Waste Generated (Metric Tons)'],
        label='E-Waste',
        color='red'
    )

    ax1.set_title(f'{country} - Smartphone vs E-Waste')
    ax1.legend(loc='upper left')
    ax1_t.legend(loc='upper right')

    # --- Laptop vs E-Waste ---
    ax2.plot(
        years,
        valid_df['Laptop_Shipments_Lag'],
        label=f'Laptop Shipments (lag {laptop_lag} yr)',
        color='green'
    )

    ax2_t = ax2.twinx()
    ax2_t.plot(
        years,
        valid_df['E-Waste Generated (Metric Tons)'],
        label='E-Waste',
        color='red'
    )

    ax2.set_title(f'{country} - Laptop vs E-Waste')
    ax2.legend(loc='upper left')
    ax2_t.legend(loc='upper right')

    plt.tight_layout()
    plt.show()

    return corr_smartphone, corr_laptop
corr_smartphone, corr_laptop = analyze_e_waste_correlation(df, "China")

print("China_Smartphone correlation:", corr_smartphone)
print("China_Laptop correlation:", corr_laptop)
corr_smartphone, corr_laptop = analyze_e_waste_correlation(df, "USA")
print("USA_Smartphone correlation:", corr_smartphone)
print("USA_Laptop correlation:", corr_laptop)
# predict future Ewaste and visualization
def predict_e_waste_time_regression(df, country, forecast_years=3):
    country_df = df[df['Country'] == country].sort_values('Year')
    y = country_df['E-Waste Generated (Metric Tons)'].values
    years = country_df['Year'].dt.year.values

    t = np.arange(len(y))
    X = sm.add_constant(t)

    model = sm.OLS(y, X).fit()
    print(model.summary())

    t_future = np.arange(len(t), len(t) + forecast_years)
    X_future = sm.add_constant(t_future)

    pred = model.get_prediction(X_future)
    forecast_vals = pred.predicted_mean
    ci = pred.conf_int()

    forecast_years_list = [years.max() + i + 1 for i in range(forecast_years)]

    return pd.DataFrame({
        'Year': forecast_years_list,
        'Predicted_E_Waste': forecast_vals.round(2),
        'Lower_CI': ci[:, 0].round(2),
        'Upper_CI': ci[:, 1].round(2)
    })

china_forecast = predict_e_waste_time_regression(
        df,
        country="China",
        forecast_years=5
    )
usa_forecast = predict_e_waste_time_regression(
    df,
    country="USA",
    forecast_years=5
)
china_hist = df[df['Country'] == "China"].sort_values('Year')
usa_hist = df[df['Country'] == "USA"].sort_values('Year')
plt.figure(figsize=(10, 6))

# --- China ---
plt.plot(
    china_hist['Year'].dt.year,
    china_hist['E-Waste Generated (Metric Tons)'],
    label="China Historical",
    color='blue',
    marker='o'
)

plt.plot(
    china_forecast['Year'],
    china_forecast['Predicted_E_Waste'],
    linestyle='--',
    color = 'blue',
    label="China Forecast"
)

plt.fill_between(
    china_forecast['Year'],
    china_forecast['Lower_CI'],
    china_forecast['Upper_CI'],
    alpha=0.2
)

# --- USA ---
plt.plot(
    usa_hist['Year'].dt.year,
    usa_hist['E-Waste Generated (Metric Tons)'],
    label="USA Historical",
    marker='s',
    color='green'
)

plt.plot(
    usa_forecast['Year'],
    usa_forecast['Predicted_E_Waste'],
    linestyle='--',
    label="USA Forecast",
    color='green'
)

plt.fill_between(
    usa_forecast['Year'],
    usa_forecast['Lower_CI'],
    usa_forecast['Upper_CI'],
    alpha=0.2
)

plt.xlabel("Year")
plt.ylabel("E-Waste Generated (Metric Tons)")
plt.title("E-Waste Forecast: China vs USA (Time Regression)")
plt.legend()
plt.grid(True)
plt.show()
#            Recycle plan
def generate_recycling_plan_(df,country,forecast_df):
    country_df = df[df['Country'] == country].sort_values('Year')
    # recycling target
    smartphone_recycle_rate_target = 0.3  # smartphone 30%
    laptop_recycle_rate_target = 0.25  # laptop25%
    recycle_point_per_100k_tons = 5  # new point

    # historical recycling standard
    avg_smartphone_sales = country_df['Smartphone Sales (Millions)'].mean()
    avg_laptop_shipments = country_df['Laptop Shipments (Millions)'].mean()
    baseline_smartphone_recycle = avg_smartphone_sales * smartphone_recycle_rate_target
    baseline_laptop_recycle = avg_laptop_shipments * laptop_recycle_rate_target

    # plan
    plan_data = []
    for _, row in forecast_df.iterrows():
        year = row['Year']
        predicted_e_waste = row['Predicted_E_Waste']
        # new recycling point
        new_recycle_points = int(np.ceil(predicted_e_waste / 100 * recycle_point_per_100k_tons))
        # target
        waste_growth_rate = predicted_e_waste / country_df['E-Waste Generated (Metric Tons)'].mean()
        target_smartphone_recycle = baseline_smartphone_recycle * waste_growth_rate
        target_laptop_recycle = baseline_laptop_recycle * waste_growth_rate

        plan_data.append({
            'Country': country,
            'Year': year,
            'Predicted_E_Waste (KT)': round(predicted_e_waste, 2),
            'Target_Smartphone_Recycle (Million)': round(target_smartphone_recycle, 2),
            'Target_Laptop_Recycle (Million)': round(target_laptop_recycle, 2),
            'New_Recycle_Points': new_recycle_points,
            'Recycle_Budget (10k USD/CNY)': round(new_recycle_points * 20, 2)  # 每个回收点投入20万（美元/人民币）
        })

    plan_df = pd.DataFrame(plan_data)
    plt.figure(figsize=(12, 6))
    x = plan_df['Year']
    width = 0.25
    plt.bar(x - width, plan_df['Target_Smartphone_Recycle (Million)'], width, label='phone target(million)',
            color='blue')
    plt.bar(x, plan_df['Target_Laptop_Recycle (Million)'], width, label='laptop target(million)', color='green')
    plt.bar(x + width, plan_df['New_Recycle_Points'], width, label='new recycling point', color='orange')
    plt.title(f'{country} E-waste plan(future{len(forecast_df)}year)')
    plt.xlabel('years'), plt.ylabel('number')
    plt.legend(), plt.grid(True, alpha=0.3)
    plt.savefig(f'{country}_recycling_plan.png')
    plt.show()
    return  plan_df

# PLAN
usa_recycle_plan = generate_recycling_plan_(df, 'USA', usa_forecast)
china_recycle_plan = generate_recycling_plan_(df, 'China', china_forecast)

print("\nUSA recycling plan：")
print(usa_recycle_plan)
print("\nChina recycling plan：")
print(china_recycle_plan)


