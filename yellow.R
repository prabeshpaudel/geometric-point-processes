library(tidyverse)

mat = scan("yellow1.txt")
mat = matrix(mat, ncol = 500, byrow = TRUE)
mat = t(mat)
df = as.data.frame(mat) %>%
  mutate(V1 = NULL)
colnames(df) = c("point1","point2","point3","point4","point5")

# yellow_degree = [2, 3, 3, 4, 4]
# yellow_distance = [727, 732, 739, 719, 729]

df %>%
  ggplot()+
  geom_histogram(aes(x = `point1`))

df %>%
  ggplot()+
  geom_histogram(aes(x = `point2`))

df %>%
  ggplot()+
  geom_histogram(aes(x = `point3`))

df %>%
  ggplot()+
  geom_histogram(aes(x = `point4`))

df %>%
  ggplot()+
  geom_histogram(aes(x = `point5`))

df_gather = df %>% # gather
  gather(N,value,c(1:5))

colMeans(df)
