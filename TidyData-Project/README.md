# TidyData- Project
## Summary
For the TidyData Project, I followed Hadley Wickham's three [Tidy Data Principles](https://vita.had.co.nz/papers/tidy-data.pdf) using data from the U.S. Federal Research and Development (R&D) Budgets. This tidy data project contains descriptions, instructions, and visualizations. 

<hr>
<p align="center">
  <img src="https://assets.nationbuilder.com/drmikekatz/pages/21/attachments/original/1698609703/money_government_pic_10-29-23_b.jpg?1698609703" style="width: 35%;" />
<hr>

## Data

This data is pulled from **jonthegeek**'s [Federal Research and Development Spending by Agency] (https://pages.github.com/). The cleaned data set contains four variables, which include...

``Budget``: Research and Development in inflation-adjusted US dollars

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

``GDP``: Total US Gross Domestic Product in inflation-adjusted US dollars 

``Year``: Fiscal Year


## Instructions
First, download the Federal R&D Budget dataset in the ``data`` folder.

After downloading, open a Jupyter Notebook.

Then, import the following libraries:

``pandas`` for data wrangling

``seaborn`` for visualizations

``matplotlib.pyplot`` for visualizations

Run the coding block and you are set to explore the data!

## Cleaning Process 🫧
To clean this dataset according to the three [Tidy Data Principles](https://vita.had.co.nz/papers/tidy-data.pdf) we must...

**First, have each variable in its own column**. This means that variables such as "Year", "GDP", "Department", and "Budget" must be labeled at the top of the dataset.

**Second, have each observation in its own row**. This is the result of one treatment on one person.

**Third, have each type of observational form a table**. Good ordering makes it easier to scan raw values.

## Vizualizations

## References
*Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf*

*Tidy data: https://vita.had.co.nz/papers/tidy-data.pdf*

*Dataset: https://pages.github.com/*
