setwd("C:/Users/xxx/Desktop")
library('ggplot2')
library('grid')
library('gridExtra')
library('reshape2')
library('plyr')
library('kml')
pdf('pdf_name')
dt <- data.frame(read.table('count_file',header = T))
ggplot(dt,aes(x=depth,y=coverage,group=sample))+ 
geom_line(size=0.3,aes(colour = sample))+
labs(x="x", y='y')+
coord_cartesian(xlim = c(0,120))+
theme(  
  panel.background = element_blank(),
	plot.background = element_blank(),
	axis.text.y= element_text(hjust = 0, color = 'black', size = 7),
	axis.title=element_text(size = 8),
	axis.line.x=element_line(color='black', size = 0.4),
	axis.line.y=element_line(color='black', size = 0.4),
	axis.ticks.length = unit(0.1, 'cm'),
	axis.ticks = element_line(color='black', size = 0.4),
	panel.margin = unit(0, 'lines'),
	legend.position = "none"
)
dev.off()
##########################
#find the max coverage & max depth for each sample
dt1 <- ddply(dt, "sample", summarize, max.cvg = max(coverage))
dt2 <- ddply(dt, "sample", summarize, max.dep = max(depth))
dt1 <- dt1[order(-dt1$max.cvg),]
dt2 <- dt2[order(dt2$max.dep),]
#########################
#cluster all the data
dt3 <- subset(dt, depth<128)
dt3 <- dcast(dt3, 
             sample ~ depth,
             value.var="coverage")
cldSDQ <- cld(dt3)
kml(cldSDQ,nbClusters = 2:6, nbRedrawing = 20,toPlot="both")
plotAllCriterion(cldSDQ)
choice(cldSDQ)
#plot(cldSDQ,6,parMean=parMEAN(type="l")) no character
plot(cldSDQ,6,parMean=parMEAN(pchPeriod=Inf))
#find cluster data
dt3$cluster <- getClusters(cldSDQ,6)
dt4 <- data.frame(sample = dt3$sample,cluster = dt3$cluster)
dt4 <- dt4[order(dt4$cluster),]
#dt3AE <- dt3[dt3$cluster %in% c("A", "E"), ]

#count <- table(dt4[2])


	