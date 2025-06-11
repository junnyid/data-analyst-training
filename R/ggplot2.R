# Cài đặt và gọi thư viện ggplot2 
install.packages("ggplot2") 
library(ggplot2)

# Tạo dữ liệu
years <- c(2018, 2019, 2020, 2021, 2022)
sales <- c(150, 200, 250, 220, 300)
df <- data.frame(years, sales)

# Vẽ biểu đồ đường với ggplot2
ggplot(df, aes(x = years, y = sales)) +
  geom_line(color = "blue", size = 1.2) +     # Vẽ đường
  geom_point(size = 3) +                      # Vẽ điểm
  labs(
    title = "Biểu đồ doanh số theo năm",
    x = "Năm",
    y = "Doanh số (triệu đồng)"
  ) +
  theme_minimal()