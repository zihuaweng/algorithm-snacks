setwd("C:/Users/xxx/Desktop")
library(VennDiagram)
library(grid)
dt1<-read.table("countz_file_1",header = T,sep="\t")
dt2<-read.table("countz_file_2",header = T,sep="\t")
dt3<-read.table("countz_file_3",header = T,sep="\t")
a <- dt1[,1]
b <- dt2[,1]
c <- dt3[,1]
p1 <-venn.diagram(
  list("name_1"=a, "name_2"=b, "name_3"=c), 
  #fill=c("red","green","blue", "orange", "yellow"), fill=1:6,
  fill=rainbow(3),
  filename=NULL,
  alpha=0.3,
  main="pic_name",
  main.cex = 2,
  cex = 1.5,
  ext.text = FALSE
#  ext.line.lwd = 1,
 # ext.dist = -0.05,
  #ext.length = 1,
  #ext.pos = -4,
#  cat.pos = 180,
#  cat.dist = c(0., 0.2, 0.02)
) 

pdf("pdf_name",width = 4, height = 4)
grid.draw(p1)
dev.off()