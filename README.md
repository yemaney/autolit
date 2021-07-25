# autolit v0.01 [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/yemaney/autolit/main/main.py/)

Streamlining explanatory data analysis and machine-learning of tabular information, and wrapping it in a streamlit app.

`Click streamlit badge above to use app.` [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/yemaney/autolit/main/main.py/)

---
## Work flow of app
- Upload Data
  - Choose where to get your data.
    - Toy data sets available:
      - Iris dataset for classification
      - Boston housing dataset for regression
    - Upload your own from local machine
    - Insert a link to data set on the  internet
  - Confirm file type and import
    - Supports both xls and csv file types
- Explore Data
  - Observe interesting plots
    - Ranked by skew for distribution plots
    - Randked by correlation for scatterplots
  - Count data entries and missing values
  - Correlation matrix
  - Optional boxplots and countplots for further examination 
- Modeling
  - Construct pipeline to predict on data
  - Plot feature importance
  - Plot learning curve
---

```
│   .gitignore
│   Dockerfile
│   LICENSE
│   main.py
│   README.md
│   requirements.txt
│   
│       
├───autolit
│          alt_plotter.py
│          autopipe.py
│          data_reader.py
│          file_importer.py
│          lr_plot.py
│          slide.py
│           sns_plotter.py
│      
│ 
│
└───src
        script.js
        slide.html
        style.css
```