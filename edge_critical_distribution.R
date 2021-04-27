library(tidyverse)
library(rio) # for importing excel sheets


edge_critical = read.csv("bi5 results/results_all.csv") # read date
edge_critical_average = edge_critical/1000

edge_critical_average$index = 1:99 # set x value

edge_critical_average_gather = edge_critical_average %>% # gather
  gather(N,value,c(1:10))

edge_critical_average_gather$N = sub(".", "", edge_critical_average_gather$N)
edge_critical_average_gather$N <- factor(edge_critical_average_gather$N,
                                         levels=c("10","20","30","40","50",
                                                  "60","70","80","90","100"))

edge_critical_average_gather %>%  # graph
  ggplot(aes(x=index,y=value,color=N))+
  geom_point()+
  theme_light()+
  labs(x = "Number of Critical Bi-grades",y = "Average Distribution of Edges")

data_list = import_list("bi5 results/results_all.xls", setclass = "tbl")
data10 = data_list$"10"
data10 <- mutate_all(data10, function(x) as.numeric(as.character(x)))
data10_gather = data10 %>% # gather
  gather(N,value,c(1:9))

data10_gather %>%
  ggplot()+
  geom_histogram(aes(x=value, color=N),fill="white")+
  xlim(0,10)

data10_gather %>%
  ggplot()+
  geom_density(aes(x=value, fill=N))+
  xlim(0,10)

data50 = data_list$"50"
data50 <- mutate_all(data50, function(x) as.numeric(as.character(x)))
data50_gather = data50 %>% # gather
  gather(N,value,c(1:9))

data50_gather %>%
  ggplot()+
  geom_histogram(aes(x=value, color=N),fill="white")+
  xlim(0,30)

data50_gather %>%
  ggplot()+
  geom_density(aes(x=value, fill=N))+
  xlim(0,30)



