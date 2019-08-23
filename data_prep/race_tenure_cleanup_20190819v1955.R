##### Load libraries, set working directory #####
if(!require(pacman)){install.packages("pacman");library(pacman)}
p_load(tidyverse)

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

pdx_msa_definition <- c('41005', '41009', '41051', '41067', '41071', '53011', '53059')

### Data came from NHGIS from an extract from Nick Kobel; includes three tables at the
## Census tract level (standardized to 2010): Tables CN1 and CY5 and CZ6
race_tenure <- read_csv("../raw_data/nhgis0026_csv.zip")

race_tenure.pdx <- race_tenure %>%
  mutate(county_fips = paste0(STATEA, COUNTYA),
         tract_fips = paste0(county_fips, TRACTA)) %>%
  filter(county_fips %in% pdx_msa_definition) %>%
  mutate(total_hh = CN1AA + CN1AB,
         total_own = CN1AA,
         share_own = total_own / total_hh, # Share of households that are owners
         
         total_hh_white = CY5AA + CY5AG,
         total_own_white = CY5AA,
         share_own_white = total_own_white / total_hh_white, # Share of white households that are owners
         
         total_hh_black = CY5AB + CY5AH,
         total_own_black = CY5AB,
         share_own_black = total_own_black / total_hh_black, # Share of Black households that are owners
         
         total_hh_aian = CY5AC + CY5AI, # American Indian/Alaska Native
         total_own_aian = CY5AC,
         share_own_aian = total_own_aian / total_hh_aian,
         
         total_hh_api = CY5AD + CY5AJ, # Asian/Pacific Islander
         total_own_api = CY5AD,
         share_own_api = total_own_api / total_hh_api,
         
         total_hh_other = CY5AE + CY5AK,
         total_own_other = CY5AE,
         share_own_other = total_own_other / total_hh_other,
         
         total_hh_multi = CY5AF + CY5AL,
         total_own_multi = CY5AF,
         share_own_multi = total_own_multi / total_hh_multi,
         
         total_hh_hisp = CZ6AB + CZ6AD,
         total_own_hisp = CZ6AB,
         share_own_hisp = total_own_hisp / total_hh_hisp,
         
         share_total_own_white = total_own_white / total_own, # Share of total homeowners that were white
         share_total_own_black = total_own_black / total_own, # Share of total homeowners that were Black, etc.
         share_total_own_aian = total_own_aian / total_own, # American Indian/Alaska Native
         share_total_own_api = total_own_api / total_own, # Asian/Pacific Islander
         share_total_own_other = total_own_other / total_own,
         share_total_own_multi = total_own_multi / total_own,
         share_total_own_hisp = total_own_hisp / total_own) %>%
  select(DATAYEAR, tract_fips:share_total_own_hisp)

##### Posting to PostGRES database #####
## https://www.r-bloggers.com/getting-started-with-postgresql-in-r/

# install.packages("RPostgreSQL")
require("RPostgreSQL")

# create a connection
# source the postgresql password
source("../server_password.R") # pw <- {'PASSWORD'}

# loads the PostgreSQL driver
drv <- dbDriver("PostgreSQL")
# creates a connection to the postgres database
# note that "con" will be used later in each connection to the database
con <- dbConnect(drv, dbname = "housing-2019-staging",
                 host = "housing-2019-staging.caicgny9d8nv.us-west-2.rds.amazonaws.com", port = 5432,
                 user = "housing2019", password = pw)
rm(pw) # removes the password

if (!(dbExistsTable(con, "race_by_tenure_1990t2010"))) {
  dbWriteTable(con, "race_by_tenure_1990t2010", race_tenure.pdx, row.names = FALSE)
} else {
  print("Already in db.")
}

