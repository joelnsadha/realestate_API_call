# realestate_API_call

## The API call
In this project, we use Python, SQL and Tableau.

## Extract Package
The extract package is where we do the data extraction. In the module, there is the extract.py module that we use to achieve this.
We make an API call to jiji.ug, a real estate site using the requests library in Python. 
We get properties listed for sale including houses, Apartments.

## Transform Package
Once we have the data extracted, we utilize the transform package to make a few transformations using the transform module.
We remove missing bedrooms and bathrooms. Alternatively, you could fill these with the mean.

## Postgres database configuration
Using the config package, we configure a database engine using SQL Alchemy. 
For this project, you can use any other database for storage. The data is stored in staging. 
Using SQL, we make a few more transformations and create summary Views for key metrics.

## Visualization - Tableau
Using Tableau desktop, we have a few visuals tracking locations, and listing prices.
