setwd("C:/Users/xzy/Desktop")
library('ggplot2')
library('RColorBrewer')
library('reshape2')
library('scales')
dt<-read.table("all",header = T,  sep="\t")
names(dt) <- c("genus","M1600045_V4","M1600018_V4")

dt <- melt(dt,
           id = "genus",
           variable.name = "sample",
           value.name = "abun"
)

colors <- colorRampPalette(brewer.pal(12,"Paired"))(length(unique(dt$genus)))

dt$v4 <- factor(dt$genus, levels=dt$genus)
dt$v5 <- factor(dt$species, levels=dt$species)

ggplot(dt, aes(x = sample, y = abun, fill = v4))+
  geom_bar(stat = "identity", position="fill", width = 0.5)+
  #facet_grid(area ~ .)+
  ggtitle("genus_distribution")+
  labs(x = "Sample", y = "abun")+
  scale_y_continuous(labels = percent_format())+
  scale_fill_manual("genus",values = colors)+
  theme(
    panel.background = element_blank(),
    plot.background = element_blank(),
    axis.text.x=element_text(angle=45, hjust = 1)
  )