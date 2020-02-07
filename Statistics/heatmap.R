setwd("C:/Users/xxx/Desktop")
library('RColorBrewer')
library('gplots')
library('heatmap.plus')
#data=na.omit(data) #delete lines with missing values\
t <- as.matrix(read.table('sig.abun', row.names=1, head =T, sep = '\t'))
t <- log(t + 1)
#t <-  cor(t)
#diag(t) <- NA
t[lower.tri (t)] <- NA
svg("abc")
png('png_name', width=1000, height=1000, res=72)
pdf('pdf_name', width=9, height=6)
mycolors <- colorpanel(299,"blue","yellow","red")
col_breaks = c(seq(0,0.1,length=100), 
              seq(0.10001,0.4,length=100), 
             seq(0.40001,0.8,length=100))

#t <- t[,order(nchar(t))]
#df<-df[,order(colnames(df),decreasing=TRUE)]

heatmap.2(
  t,
  #cellnote = t,
  #notecol = "none",
  #keep.dendro = F,
  #Rowv = NULL,
  #Colv = NULL,
  main = "NIPT&CNV (species_level)",
  density.info = "none",
  trace = "none",
  margins = c(12,12),
  col = mycolors,
  #breaks = col_breaks,
  dendrogram = "row",
  #Colv = "NA",
  key.title=NA,
  densadj = 0.25,
  keysize=0.8,
  cexRow=0.6,
  cexCol=0.6,
  srtCol=45
)
dev.off()