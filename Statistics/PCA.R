	library(fpc)
	library(ade4)
	dat1 <- read.table("qiime/group-sample/PCA/genus.prof", head=T, sep="	")
	dat <- dat1[, 2:ncol(dat1)]
	rownames(dat) <- dat1[, 1]
	dat <- as.matrix(dat)
	#ds <- dim(dat)
	dat <- dat[rowSums(dat)!=0,]
	phenotypes <- read.table("qiime/group-sample/PCA/genus.phenotypes")
	data.a <- dat
	data1 <- sweep(data.a, 2, apply(data.a,2,sum), "/")
	data <- t(sqrt(data1))
	data.dudi <- dudi.pca(data, center=TRUE, scale=F, scan=F, nf=2)
	eig <- (data.dudi$eig/ sum(data.dudi$eig))
	write.table(eig, "qiime/group-sample/PCA/genus.eig_contribution", sep="	", quote=F, row.names=paste("PC",1:length(eig),sep=""), col.names=F)
	phenotype <- phenotypes[,0+1]
	IBD <- factor(phenotype)
	pdf("qiime/group-sample/PCA/v34.genus.Group.PCA.pdf")
	x1 <- min(data.dudi$li[,1]) - 0.3
	y1 <- min(data.dudi$li[,2]) - 0.3
	x2 <- max(data.dudi$li[,1]) + 0.3
	y2 <- max(data.dudi$li[,2]) + 0.3
	bb <- head(data.dudi$c1[order(sqrt((data.dudi$c1[,1])^2+(data.dudi$c1[,2])^2),decreasing=T),],n=4L)[1:4,]
	rownames(bb) <- gsub("^X", "", rownames(bb))
	rownames(bb) <- gsub("\\S+f__", "f__", rownames(bb))
	cutoff <- (x2-0.3) / abs(bb[1,1]) * 0.5
	d2 <- data.frame(X=bb[1:dim(bb)[1],1]*cutoff, Y=bb[1:dim(bb)[1],2]*cutoff, LAB=rownames(bb)[1:dim(bb)[1]])
	d <- data.dudi$li
	library("ggplot2")
	library("grid")
	ggdata <- data.frame(d)
	p<-ggplot(ggdata) +xlab(paste("PC1"," (",round(eig[1]*100,2),"%)",sep=""))+ylab(paste("PC2"," (",round(eig[2]*100,2),"%)",sep=""))+ geom_vline(xintercept = 0) + geom_hline(yintercept = 0)
	p+geom_point(aes(x=d[,1], y=d[,2], color=IBD), size=5, shape=20) +
	stat_ellipse(aes(x=d[,1], y=d[,2],fill=IBD),geom="polygon", level=0.8, alpha=0.3) +
	geom_text(data=d2, aes(x=X, y=Y, label=LAB), size=4) +
	geom_segment(data=d2, aes(x=0, y=0, xend=X, yend=Y), arrow = arrow(length = unit(0.2, "cm")), size=0.2, alpha=0.5) +
	guides(color=guide_legend("Cluster"),fill=guide_legend("Cluster"))  +
	theme_bw()+theme(panel.grid =element_blank()) + theme(axis.text = element_blank()) + theme(axis.ticks = element_blank())
	dev.off()

