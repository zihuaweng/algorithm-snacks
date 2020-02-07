#!/usr/bin/perl -w                                                                                                                                                      
use strict;
#################################################################################
unless(1==@ARGV) {
	&usage;
	exit;
}
################################################################################
my($cvglist)=@ARGV;
my(@info,%list,$max,%cvg,$i,$j,$k,%count,%length,%w_length,$temp,$sum,$count_zero);
my$reflength="file/of/Bacteria/genome/ref/length";
my$R="/dir/of/R";
################################################################################
open LIST, $cvglist or die "failed to open file $cvglist $!\n";
while(<LIST>){
	chomp;
	@info = split /\t/, $_;
	$list{$info[0]} = $info[1];
}
close LIST;
################################################################################
open LEN, $reflength or die "failed to open file $reflength $!\n";
while(<LEN>){
	chomp;
	@info = split /\t/, $_;
	$length{$info[1]}{$info[0]} = $info[2];
}
foreach $i(keys %length){
	foreach $j(keys %{$length{$i}}){
		$w_length{$i} += $length{$i}{$j};
	}
}
close LEN;
################################################################################
foreach $i(sort keys %list){
	&subdata($i);
	&coverageplot($i);
}
################################################################################
sub subdata{
	my($species) = @_;
	open WIN, $list{$species} or die 
	"failed to open file $list{$species} $!\n";
	open OUT, ">$list{$species}.count" or die 
	"failed to write file $list{$species}.count $!\n";
	$max = 0;
	$count_zero = 0;
	$sum=0;
	while(<WIN>){
		chomp;
		@info = split /\t/, $_;
		$max = $info[3] if ($info[3] > $max);
		$cvg{$info[0]}{$info[2]}=$info[3];
	}
	my@num = 1..$max;
	foreach $i(keys %cvg){
		foreach $j(keys %{$cvg{$i}}){
			if($cvg{$i}{$j}<=1){
				$temp = 0;
				$count_zero++;
#				print "len\t\t$species\t$w_length{$species}\n";
				$sum += $cvg{$i}{$j}*1000/$w_length{$species};
			}elsif($cvg{$i}{$j}>1 && $cvg{$i}{$j}<=2){
				$temp = 2;
				$count{$species}{$temp}++;
			}elsif($cvg{$i}{$j}>2){
				foreach $k(@num){
					if(2*$k < $cvg{$i}{$j} && $cvg{$i}{$j} <= 2*$k+2){
						$temp = 2*$k+2;
						$count{$species}{$temp}++;
					}
				}
			}
		}
	}
	print OUT "depth\ttimes\tcoverage\n0\t$count_zero\t$sum\n";
	foreach $i(sort keys %count){
		next unless ($i eq $species);
		foreach $j(sort {$a <=> $b} keys %{$count{$i}}){
			print OUT "$j\t$count{$i}{$j}\t";
			$sum += $count{$i}{$j}*1000/$w_length{$i};
			print OUT "$sum\n";
		}
	}
	close WIN;
	close OUT;
}
################################################################################
sub coverageplot {
	my($species)=@_;
	open OUTR,">$list{$species}.coverage.R" or die
	"failed to write $list{$species}.coverage.R $!\n";
	print OUTR "
	library('ggplot2');
	library('grid');
	library('gridExtra');
	library('reshape2');
	pdf('$list{$species}.coverage.pdf',width=8, height=2);
	dt <- read.table('$list{$species}.count',header = T);
	dt1 = dt[-2]
	upper <- ggplot(dt1,aes(x=depth,y=coverage,group=1))+ 
	geom_line(size=0.3)+
	labs(x=NULL, y='Coverage')+
	theme(  
	panel.background = element_blank(),
	plot.background = element_blank(),
	axis.text.y= element_text(hjust = 0, color = 'black', size = 7),
	axis.text.x=element_blank(),
	axis.title=element_text(size = 8),
	axis.line.y=element_line(color='black', size = 0.4),
	axis.ticks.length = unit(0.1, 'cm'),
	axis.ticks = element_line(color='black', size = 0.4),
	axis.ticks.x = element_blank(),
	panel.margin = unit(0, 'lines')
	)

	dt2 = dt[-3]
	dt2\$times = log2(dt2\$times)+1
	below <- ggplot(dt2, aes(x=depth,y=times))+ 
	geom_bar(stat='identity' ,width = 0.3,alpha=0.8)+
	labs(x='Depth', y='Times(log2)')+
	theme(  
	panel.background = element_blank(),
	plot.background = element_blank(),
	axis.text = element_text(vjust = 0, color = 'black',size = 5),
	axis.line.x=element_line(color='black', size = 0.4),
	axis.line.y=element_line(color='black', size = 0.4),
	legend.key.size = unit(0.5, 'lines'),
	legend.text = element_text(size = 7),
	legend.justification=c(0,1), 
	legend.position=c(0,1.5),
	legend.box = 'horizontal',
	legend.title=element_blank(),
	legend.background = element_blank(),
	axis.ticks.length = unit(0.1, 'cm'),
	axis.title = element_text(size = 8),
	axis.ticks = element_line(color='black', size = 0.4),
	panel.margin = unit(0, 'lines')
	)

	gU = ggplotGrob(upper)
	gB = ggplotGrob(below)
	maxWidth = unit.pmax(gU\$widths,gB\$widths)
	gU\$widths <- maxWidth
	gB\$widths <- maxWidth
	grid.arrange(gU,gB, ncol=1, heights=c(2,3))
	dev.off()
	";
	system("$R -f $list{$species}.coverage.R 1>/dev/null");
	close OUTR;
}
################################################################################
sub usage {
	print STDERR
	"\n
	author:\n
	ZihuaWeng/2016
	Description:\n
	This script is to return statistics info and plot for cvg_window (1000)\n
	Usage:  \$perl $0 [cvg_win.list]\n
	\n"
}

