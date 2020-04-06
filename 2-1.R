
library(igraph)  # ライブラリを読み込み
ER<-erdos.renyi.game(n=200,p=0.05)  # ER モデルでノード数 200 密度 0.05 のグラフを生成
# write.graph(g1,"er.dot",format="dot") # グラフを er.dot というファイルに書き出し
WS<-watts.strogatz.game(dim=1,size=200,nei=5,p=0.05) # WS モデルでグラフを生成
# write.graph(g2,"ws.dot",format="dot") 
BA<-ba.game(n=200,m=2,directed=F) # BA モデルでグラフを生成
# write.graph(g3,"ba.dot",format="dot")

# #plot
# library(igraph)
# g1<-erdos.renyi.game(n=200,p=0.05)
# plot(g1)

library(igraph)
g<-erdos.renyi.game(n=200,p=0.05)
dd<-degree.distribution(g) # 次数分布を求める
plot(dd[-1],xlab="degree",ylab="proportion") # 次数分布をプロットする
plot(dd[-1],log="xy",xlab="degree",ylab="proportion") # 両対数軸でプロットする