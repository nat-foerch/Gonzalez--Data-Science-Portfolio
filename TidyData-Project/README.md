# TidyData- Project 🧹
## Project Overview
For the TidyData Project, I followed Hadley Wickham's three [Tidy Data Principles](https://vita.had.co.nz/papers/tidy-data.pdf) using data from the U.S. Federal Research and Development (R&D) Budgets. This tidy data project contains descriptions, instructions, and visualizations that will help you do the same with your datasets! Come clean with me!

## How To Clean Your Data! 🫧
(1) Check that you have downloaded Jupyter Notebook or VS Code. Then download the following libraries and packages!
- [Federal R&D Budget](https://github.com/nat-foerch/Gonzalez--Data-Science-Portfolio/blob/main/TidyData-Project/fed_rd_year%26gdp.csv)
- pandas==2.2.3
- seaborn==0.13.2
- matplotlib==3.10.1

(2) Copy and paste the [code](https://github.com/nat-foerch/Gonzalez--Data-Science-Portfolio/blob/main/TidyData-Project/Main.ipynb) from the TidyData Folder into your environment.

(3) Run code, and your data is ready for EDA!

## What's In The Data? 🧐

 This dataset includes thirteen federal departments (listed below) and their spending budgets. It includes the corresponding year and GDP rates. This data is pulled from [jonthegeek's](https://pages.github.com/) _Federal Research and Development Spending by Agency_.

``Budget``: Research and Development in inflation-adjusted US dollars

``GDP``: Total US Gross Domestic Product in inflation-adjusted US dollars 

``Year``: Fiscal Year

``Department``: US Agency/Department
<details>
<summary>Select to see a list of all departments included</summary>

  
**DHS** - Department of Homeland Security 🚔

**DOC** - Department of Commerce 📈

**DOD** - Department of Defense 🗽

**DOE** - Department of Energy ⚡️

**DOT** - Department of Transportation 🚗

**EPA** - Environmental Protection Agency 🌳

**HHS** - Department of Health and Human Services 👩🏻‍⚕️

**Interior** - Department of the Interior 🦬

**NASA** - National Aeronautics and Space Administration 🪐

**NIH** - National Institutes of Health 💉

**NSF** - National Science Foundation 🧪

**USDA** - U.S. Department of Agriculture 🌽

**VA** - Department of Veteran Affairs 🎖️
</details>


## Principles In Action 🎬
### To clean this dataset according to the three [Tidy Data Principles](https://vita.had.co.nz/papers/tidy-data.pdf), we must...

(1) Have each variable in its own column**. This means that variables such as "Department", "Budget", "Year", and "GDP" must be labeled at the top of the dataset.

(2) Have each observation in its own row**. This is the result of one treatment on one person.

(3) Have each type of observational form a table**. Good ordering makes it easier to scan raw values.

## What's Possible?

### Create a clean line plot! 📈
<hr>
<p align="center">
  <img src="https://github.com/nat-foerch/Gonzalez--Data-Science-Portfolio/blob/main/TidyData-Project/Images/lineplot.png" width="50%" /> 
  
_This line plot demonstrates how each department's budget changed over time. The Department of Defense (DOD) receives the most money each year._

### Create a spectacular Bar Chart! 📊
<hr>
<p align="center">
  <img src="https://github.com/nat-foerch/Gonzalez--Data-Science-Portfolio/blob/main/TidyData-Project/Images/barplot.png" width="50%;">
</p>

_This bar chart demonstrates the year-to-year budget allocated to all departments. The total budget has steadily increased each year, although it has generally decreased since 2011._


## References
*Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf*

*Tidy data: https://vita.had.co.nz/papers/tidy-data.pdf*

*Dataset: https://pages.github.com/*
