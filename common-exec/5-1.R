library(igraph)
g<-erdos.renyi.game(n=200,p=0.05)
dd<-degree.distribution(g) # 次数分布を求める
plot(dd[-1],xlab="degree",ylab="proportion") # 次数分布をプロットする
