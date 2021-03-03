library(tidyverse)

edge_critical = read.csv("results_all.csv") # read date
edge_critical$index = 1:99 # set x value

edge_critical_gather = edge_critical %>% # gather
  gather(N,value,c(1:10))

edge_critical_gather %>%  # graph
  ggplot(aes(x=index,y=value,color=N))+
  geom_point()+
  labs(x = "Number of Critical Bi-grades",y = "Distribution")

edge_critical_mutate = edge_critical %>%
  mutate(X10 = X10 / sqrt(10),
         X20 = X20 / sqrt(20),
         X30 = X30 / sqrt(30),
         X40 = X40 / sqrt(40),
         X50 = X50 / sqrt(50),
         X60 = X60 / sqrt(60),
         X70 = X70 / sqrt(70),
         X80 = X80 / sqrt(80),
         X90 = X90 / sqrt(90),
         X100 = X100 / sqrt(100))

edge_critical_mutate_gather = edge_critical_mutate %>% # gather
  gather(N,value,c(1:10))

edge_critical_mutate_gather %>%  # graph
  ggplot()+
  geom_point(aes(x=index,y=value,color=N))+
  labs(x = "Number of Critical Bi-grades",y = "Distribution")



