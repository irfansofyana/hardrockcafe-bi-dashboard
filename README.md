# hardrockcafe-bi-dashboard

BI Development. Study Case: Hard Rock Cafe

This is an assignment for IF4044 Big Data Technology Course

## Documentation

The development process of this project can be seen under [docs folder](/docs). The documentation however is 
only available in Indonesian. 

## How to generate fake data for data warehouse

- Run the [docker-compose file](mysql-phpmyadmin.yml) to host MySQL DB and PhpMyAdmin.
- Setup the connection to DB by setting the right connection string under a file named `.env`.
  
    - a.k.a you only need to create `.env` file then copy the content of [sample.env](scripts/sample.env)
    to `.env` file then put the right values for connection string to connect to your DB.
- Run the [main.py](scripts/main.py) file.
- Your fake data now is available under your database!

## Links

- The BI dashboard created can be found public at this [link](https://public.tableau.com/profile/irfan.sofyana.putra#!/vizhome/TBD_Tubes_16159056805820/LivePerformanceVisitorinHardRockCafes)

## Credit

Credit to my team!
- 13517078 - Irfan Sofyana Putra (me)
- 13516109 - Kevin Fernaldy
