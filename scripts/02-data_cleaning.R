#### Preamble ####
# Purpose: Cleans the raw data into a digestable and saves many different tables to be analysed later format
# Author: Rahul Gopeesingh
# Date: 30 March 2024
# Contact: rahul.gopeesingh@mail.utoronto.ca


#### Workspace setup ####

library(tidyverse)
library(arrow)
library(dplyr)
library(ggplot2)

#### Clean data ####


#import raw t1 data
t1_data <-
  read_csv(
    "data/raw_data/t1rawdata.csv",
    col_types =
      cols(
        "Player Name" = col_character(),
        "CS at 10" = col_integer(),
        "Max Level Lead" = col_integer(),
        "Outcome" = col_character()
      )
  )

t1_data
#slice data accordingly

t1_data$`CS at 10` <- cut(t1_data$`CS at 10`, 
                   breaks = c(-Inf, 50, 70, 100, Inf), 
                   labels = c("1", "2", "3", "4"),
                   include.lowest = TRUE)
t1_data <- t1_data %>%
  mutate(Outcome = ifelse(Outcome == "Win", 1, ifelse(Outcome == "Lose", 0, Outcome)))
write_parquet(t1_data, "/Users/rahulgopeesingh/Documents/Match Prediction/data/analysis_data/t1_data.parquet")
t1_data


#filter t1 jungler and support
t1_data_filtered <- t1_data %>%
  filter(`Player Name` != "Oner" & `Player Name` != "Keria")
write_parquet(t1_data_filtered, "/Users/rahulgopeesingh/Documents/Match Prediction/data/analysis_data/t1_data_filtered.parquet")

#filter t1 jungler

t1_data_filtered_max_level <- t1_data %>%
  filter(`Player Name` != "Keria")

write_parquet(t1_data_filtered_max_level, "/Users/rahulgopeesingh/Documents/Match Prediction/data/analysis_data/t1_data_filtered_max_level.parquet")





#import raw gengdata 
geng_data <-
  read_csv(
    "data/raw_data/gengrawdata.csv",
    col_types =
      cols(
        "Player Name" = col_character(),
        "CS at 10" = col_integer(),
        "Max Level Lead" = col_integer(),
        "Outcome" = col_character()
      )
  )

geng_data
#slice the geng data accordingly
geng_data$`CS at 10` <- cut(geng_data$`CS at 10`, 
                          breaks = c(-Inf, 50, 70, 100, Inf), 
                          labels = c(1, 2, 3, 4),
                          include.lowest = TRUE)
geng_data <- geng_data %>%
  mutate(Outcome = ifelse(Outcome == "Win", 1, ifelse(Outcome == "Lose", 0, Outcome)))
write_parquet(geng_data, "/Users/rahulgopeesingh/Documents/Match Prediction/data/analysis_data/geng_data.parquet")
geng_data



###filter support and jungle from geng table
geng_data_filtered <- geng_data %>%
  filter(`Player Name` != "Canyon" & `Player Name` != "Lehends")
write_parquet(geng_data_filtered, "/Users/rahulgopeesingh/Documents/Match Prediction/data/analysis_data/geng_data_filtered.parquet")


###Filter out a table with no support only for geng
geng_data_filtered_max_level <- geng_data %>%
  filter(`Player Name` != "Lehends")

write_parquet(geng_data_filtered_max_level, "/Users/rahulgopeesingh/Documents/Match Prediction/data/analysis_data/geng_data_filtered_max_level.parquet")

