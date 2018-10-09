fert<-c(100,200,300,400,500,600,700)
rainfall<-c(10,20,10,30,20,20,30)
yield<-c(40,50,50,70,65,65,80)

regression <- lm(yield~fert+rainfall)
regression

summary(regression)
anova(regression)
plot(yield ~ fert,
	xlab = "fert",
	ylab = "yield",
	main = "Relationship Between yield and fertilizer")
		
lm(yield ~ fert)
	abline(lm(yield ~ fert))	
plot(yield ~ rainfall,
	xlab = "rainfall",
	ylab = "yield",
	main = "Relationship Between yield and rainfall")
		
lm(yield ~ rainfall)
	abline(lm(yield ~ rainfall))
	
	