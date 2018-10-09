X1<-c(0,0,10,10,20,20)
X2<-c(0,0,100,100,400,400)
Y<-c(5,7,15,17,9,11)

regression <- lm(Y~X1+X2)
regression

summary(regression)
anova(regression)
plot(Y ~ X1,
	xlab = "X1",
	ylab = "Y",
	main = "Relationship Between X1 and Y")
		
lm(Y ~ X1)
	abline(lm(Y ~ X1))	
plot(Y ~ X2,
	xlab = "X2",
	ylab = "Y",
	main = "Relationship Between X2 and Y")
		
lm(Y ~ X2)
	abline(lm(Y ~ X2))
	
	