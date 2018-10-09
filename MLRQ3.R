CPUTime<-c(2,5,7,9,10,13,20)
memory<-c(2,4,8,16,32,64, 128)
DiskIO<-c(14,16,27,42,39,50, 83)

regression <- lm(DiskIO~CPUTime+memory)
regression

summary(regression)
anova(regression)
plot(DiskIO ~ CPUTime,
     xlab = "CPUTime",
     ylab = "DiskIO",
     main = "Relationship Between CPUTime and DiskIO")

lm(DiskIO ~ CPUTime)
abline(lm(DiskIO ~ CPUTime))	
plot(DiskIO ~ memory,
     xlab = "memory",
     ylab = "Y",
     main = "Relationship Between memory and DiskIO")

lm(DiskIO ~ memory)
abline(lm(DiskIO ~ memory))


