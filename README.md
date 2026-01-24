# -A-Solution-for-the-Correlation-Analysis-of-Global-Technology-Consumption-and-Electronic-Waste

## 1.Executive Summary 
As global consumption of smartphones and laptops continues to rise, the management of electronic waste (e-waste) has become a central challenge within the ESG strategies of technology companies. This report integrates technology consumption data from the United States and China spanning 2015–2025—including smartphone sales and laptop shipments—with corresponding e-waste generation data. Focusing on two core product categories, smartphones and laptops, the analysis investigates the relationship between product sales and e-waste generation. By applying time-lag correlation analysis and time-series regression, the study addresses the challenge of predicting growth trends and further develops predictive recycling  strategies.

## 2.Environmental dimension: sale and E-waste correlation analyse 

### 2.1 Set lag and find possible trend
To assess the environmental impact of consumer behavior, we employed time-lag correlation analysis. Considering the average lifespan of electronic products, the lag was predicted by using the cross-correlation function (CCF):

Smartphone： Set 1-2 year lag（USA: 1year, China: 2year）

<img width="190" height="165" alt="13d8ac0b75933e75752eec898d0efa4c" src="https://github.com/user-attachments/assets/476957ba-f762-4eb1-928d-b8993d12ec9d" />
<img width="195" height="163" alt="5ba2cf66580ce4ad72aa129d420b2a91" src="https://github.com/user-attachments/assets/c3885ae7-f079-403f-b750-d82ffb8ebd19" />


Laptop： Set 2 year lag

<img width="190" height="169" alt="81d9db6dba7967aa41942658d864bee7" src="https://github.com/user-attachments/assets/e95091e1-a464-49df-81ff-15a4200f6e5e" />
<img width="190" height="160" alt="43a3841df10a286e4e90fe94510a1c53" src="https://github.com/user-attachments/assets/4477536a-e129-4d0c-9c2b-6610dbaaa7ed" />
                                                              
                                                            


The chart analysis reveals markedly different e-waste generation patterns in China and the United States. In the Chinese market, a strong two-year lagged correlation is observed between smartphone sales and e-waste generation. In contrast, the U.S. market exhibits greater behavioral complexity, where the relationship between sales and disposal is likely influenced by additional factors beyond direct purchasing behavior.
<p>
<img width="1200" height="500" alt="Figure_2" src="https://github.com/user-attachments/assets/e2e69312-db5a-49bf-b66d-bda4e41d6dad" />
<img width="1200" height="500" alt="Figure_1" src="https://github.com/user-attachments/assets/d20be47b-da96-493a-8188-a49c4385d0c9" />
  </p>
<p>
  <img width="1034" height="100" alt="pearson" src="https://github.com/user-attachments/assets/27bb8786-e912-461e-8246-2a3b9ebf0bb2" />
  </p>

In China:Smartphones are the primary source of environmental pressure: a positive correlation coefficient of 0.51 supports the “sales-as-pollution” hypothesis.
Laptop data exhibit decoupling: a correlation coefficient of −0.03 indicates no direct relationship between laptop sales volume and e-waste generation.

In USA:When new device sales increase, The Pearson result correlation coefficients were negative number. Possible explanations include:
Well-established trade-in systems: The U.S. market has a mature trade-in mechanism. During periods of strong growth in new laptop sales (as indicated by the green peaks in the lower-left figure), older devices are often collected by retailers for export or refurbishment, rather than being immediately recorded as domestic e-waste in the same year.
“Hoarding effect” and inventory clearance: The negative correlation may indicate that e-waste generation is driven more by inventory-clearing behavior than by new purchases. That is, consumers may store old devices in drawers when buying new ones—resulting in lower observed e-waste—while disposal tends to occur in batches during economic downturns or large-scale cleanups.(largely independent of current sales volumes.)

### 2.2 E-waste growth forecast (2025-2030)
Establishing a time regression model using ordinary least squares (OLS)：

$$Y_{waste} = \beta_0 + \beta_1 \cdot Year + \epsilon$$

<p>
  <img width="1000" height="600" alt="Figure_3" src="https://github.com/user-attachments/assets/1f942eb0-af5c-40a5-8916-77441763ded8" />

</p>

## 3. Social & Governance: Recycling Strategy Planning
### 3.1 Dynamic Recycling Target Setting
Based on the projected increase in electronic waste, We set annual recycling KPIs:
Smartphone target: 30% of baseline sales are set as the compliant recycling target.
Laptop target: 25% of baseline shipment volume is designated for compliant recycling.
### 3.2 Infrastructure and Budget Allocation
To support the above targets, the governance model estimates the required infrastructure investment:
Infrastructure standard: For every additional 100,000 metric tons of forecasting e-waste, five standardized recycling points are required.
Budget estimation: Each recycling point is allocated a budget of 200,000, covering construction, operation, and public outreach costs.


### 3.3 Estimation for next 5 years
<P>
  <img width="1200" height="600" alt="Figure_4" src="https://github.com/user-attachments/assets/f249e29d-51cf-4abe-83fd-045c410d164b" />
  <img width="1200" height="600" alt="Figure_5" src="https://github.com/user-attachments/assets/517e0be4-139f-4ca6-abf3-238bafbefbf3" />


</P>

## 4.Conclusion
### 4.1.Recommendation: Establish a Resilient Recycling and Governance System
In response to the risks revealed by the data, this study proposes a quantified recycling strategy:
Targeted deployment: In China, efforts should prioritize smartphone recycling, and use sales data to forecast processing demand two years in advance. In contrast, the United States should focus on activating “drawer stock,” leveraging incentive-based policies to break the negative correlation between sales volume and waste generation.
Flexible budgeting: Given the uncertainty inherent in the forecasts, the governance framework allocates dynamic recycling points (New Recycle Points) and budgets for the period 2026–2030. Enterprises are advised to establish redundant recycling capacity sufficient to cover the upper bound of the confidence interval, thereby mitigating potential extreme waste-emission scenarios.

### 4.2 Shortcomings
This project used a time-series regression approach, which resulted in a nearly constant forecast of U.S. e-waste generation over the next five years. Consequently, the proposed recycling plan also remained across the forecast horizon. This outcome suggests that, under the current model specification, the correlation between time and e-waste generation in the United States is relatively weak. Therefore, future research should explore alternative modeling approaches to better capture the underlying dynamics and improve the explanatory power of the analysis.


