	library(scatterplot3d)
    library(WGCNA)
    library(extrafont)
	setwd("/dir/with/PCoA/weighted_unifrac")
	data = read.table("weighted_unifrac_sorted_otu_table.txt")
    d=as.dist(data)
	groups = read.table("/group_file", head=T)
	rownames(groups) <- groups$sample
	groups1 <- factor(groups$group)
	group <- levels(groups$group)
#lab <- levels(groups$sample)
	lab <- colnames(data)
	lab = gsub("X","",lab)
	cols=c("pink", "orange", "green", "cyan", "blue", "purple", "seagreen", "steelblue", "red", "DarkTurquoise", "Sienna", "Chocolate", "BlueViolet", "Magenta", "brown", "gray", "darkred", "darkmagenta", "mediumvioletred")
	pchs <- c(21,22,23,24,25,8,1,2,3,4,5)
	pch <- rep(19, dim(data)[1])
	col <- rep("black", dim(data)[1])
	for (i in 1:length(group)){
		pch[groups[rownames(data),2] == group[i]] <- pchs[i]
		col[groups[rownames(data),2] == group[i]] <- cols[i]
	}


# Dendorgram
    h = hclust(d, "average");
    pdf("weighted_unifrac/Dendrogram.pdf",height=5,width=8)
    plot(as.dendrogram(h),main = "Sample Cluster", sub="",xlab="",ylab="",horiz=T,col=col)
    dev.off()

# PCoA
	pca = cmdscale(d,k=3,eig=T) 
    PC1=pca$points[,1]
    PC2=pca$points[,2]
    PC3=pca$points[,3]
    write.csv(pca$points,file="PCoA.csv")

	pc1 =floor(pca$eig[1]/sum(pca$eig)*10000)/100
	pc2 = floor(pca$eig[2]/sum(pca$eig)*10000)/100
    pc3 = floor(pca$eig[3]/sum(pca$eig)*10000)/100
# PCoA 2D pdf
	pdf("weighted_unifrac/PCoA-2D.pdf",height=5,width=15)
	par(mfrow = c(1,3))
# PC1 vs PC2	
	xlab <- paste("PC1 ", pc1,"%",sep="")
	ylab <- paste("PC2 ", pc2,"%",sep="")
	main <- "PCoA-PC1 vs PC2"
	plot(PC1,PC2, xlab = xlab, ylab = ylab,cex = 0.8, main=main, type="n")
	abline(v = 0, h = 0, lty = 3)
	points(PC1, PC2, col=col,cex = 0.8, pch = pch,bg=col)
#*	text(PC1, PC2, adj =-0.2 ,labels=lab,pos = NULL, offset = 0.4, vfont = NULL,cex =1.2, col = NULL, font = NULL)
	legend("bottomright", legend=group, col=cols, pch = pchs, cex=0.8,bty="n",pt.bg=cols)
# PC1 vs PC3
	xlab <- paste("PC1 ", pc1,"%",sep="")
	ylab <- paste("PC3 ", pc3,"%",sep="")
	main <- "PCoA-PC1 vs PC3"
	plot(PC1,PC3, xlab = xlab, ylab = ylab,cex = 0.8, main=main, type="n")
	abline(v = 0, h = 0, lty = 3)
	points(PC1, PC3, col=col,cex = 0.8, pch = pch,bg=col)
#*	text(PC1, PC3, adj =-0.2 ,labels=lab,pos = NULL, offset = 0.4, vfont = NULL,cex =1.2, col = NULL, font = NULL)
	legend("bottomright", legend=group, col=cols, pch = pchs, cex=0.8,bty="n",pt.bg=cols)
# PC2 vs PC3
	xlab <- paste("PC2 ", pc2,"%",sep="")
	ylab <- paste("PC3 ", pc3,"%",sep="")
	main <- "PCoA-PC2 vs PC3"
	plot(PC2,PC3, xlab = xlab, ylab = ylab,cex = 0.8, main=main, type="n")
	abline(v = 0, h = 0, lty = 3)
	points(PC2, PC3, col=col,cex = 0.8, pch = pch,bg=col)
#*	text(PC2, PC3, adj =-0.2 ,labels=lab,pos = NULL, offset = 0.4, vfont = NULL,cex =1.2, col = NULL, font = NULL)
	legend("bottomright", legend=group, col=cols, pch = pchs, cex=0.8,bty="n",pt.bg=cols)
	dev.off()
# PCoA 3D pdf
	pdf("weighted_unifrac/PCoA-3D.pdf")
	xlab <- paste("PC1 ", pc1,"%",sep="")
	ylab <- paste("PC2 ", pc2,"%",sep="")
	zlab <- paste("PC3 ", pc3,"%",sep="")
	main <- "PCoA 3D plot"
    s3d <- scatterplot3d(PC1, PC2, PC3, xlab = xlab, ylab = ylab, zlab = zlab, angle=60, main=main, type="n",grid=F,highlight.3d=T)
	s3d$points3d(PC1, PC2, PC3, col=col,cex = 0.8, pch = pch,bg=col)
	legend("bottomright", legend=group, col=cols, pch = pchs, cex=0.8,bty="n",pt.bg=cols)
	dev.off()
# PCoA 3D png
	png("weighted_unifrac/PCoA-3D.png")
	xlab <- paste("PC1 ", pc1,"%",sep="")
	ylab <- paste("PC2 ", pc2,"%",sep="")
	zlab <- paste("PC3 ", pc3,"%",sep="")
	main <- "PCoA 3D plot"
    s3d <- scatterplot3d(PC1, PC2, PC3, xlab = xlab, ylab = ylab, zlab = zlab, angle=60, main=main, type="n",grid=F,highlight.3d=T)
	s3d$points3d(PC1, PC2, PC3, col=col,cex = 0.8, pch = pch,bg=col)
	legend("bottomright", legend=group, col=cols, pch = pchs, cex=0.8,bty="n",pt.bg=cols)
	dev.off()
