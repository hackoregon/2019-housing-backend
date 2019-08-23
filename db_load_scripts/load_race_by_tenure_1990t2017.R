##### Load libraries, set working directory #####
if(!require(pacman)){install.packages("pacman");library(pacman)}
p_load(tidyverse, RPostgreSQL)

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

##### Posting to PostGRES database #####
# source the postgresql password
source("../server_password.R") # pw <- {'PASSWORD'}

race_by_tenure_1990t2017 <- readRDS("../data/cleaned_data/race_by_tenure_1990t2017.RDS")

# loads the PostgreSQL driver
drv <- dbDriver("PostgreSQL")
# creates a connection to the postgres database
# note that "con" will be used later in each connection to the database
con <- dbConnect(drv, dbname = "housing-2019-staging",
                 host = "housing-2019-staging.caicgny9d8nv.us-west-2.rds.amazonaws.com", port = 5432,
                 user = "housing2019", password = pw)
rm(pw) # removes the password

# dbSendQuery(con, "DROP TABLE race_by_tenure_1990t2010")

if (!(dbExistsTable(con, "race_by_tenure_1990t2017"))) {
  dbWriteTable(con, "race_by_tenure_1990t2017", race_by_tenure_1990t2017, row.names = FALSE)
} else {
  print("Table already in database")
}
