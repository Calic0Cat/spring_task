import copy
import time
import re

class Node():
  #  それぞれのノードはデータと次のノードへのリンクを持つ。
  def __init__(self, data, next = None):
    self.data = data
    self.next = next
  # データを設定する。
  def set_data(self, data):
    self.data = data
  # データを取得する。
  def get_data(self):
    return self.data
  # 次のノードを設定する。
  def set_next(self, next):
    self.next = next
  # 次のノードを取得する。
  def get_next(self):
    return self.next

class LinkedList():
    # リストの先頭
    def __init__(self):
        self.head = None
        self.length = 0
    def list_length(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.get_next()
        return count

    # データの出力
    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    # 先頭にノードを挿入する。
    def insert_at_start(self, data):
        length = self.list_length()
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length = length + 1
    
    # 最後にノードを挿入する。
    def insert_at_end(self, data):
        length = self.list_length()
        new_node = Node(data)
        temp = self.head
        # 最後のノードまで移動する。
        while temp.get_next() is not None:  
            temp = temp.get_next()
        temp.next = new_node
        self.length = length  + 1

    # ある場所にノードを挿入する。
    def insert_position(self, position, data):
        if position < 0 or position > self.length:
            raise ValueError
        else:
            if position == 0:
                self.insert_at_start(data)
            else:
                if position == self.length:
                    self.insert_at_end(data)
                else:
                    length = self.list_length()
                    new_node = Node(data)
                    count = 0
                    temp = self.head
                    while count < position -1:
                        count += 1
                        temp = temp.get_next()
                    new_node.set_next(temp.get_next())
                    temp.set_next(new_node)
                    self.length = length + 1

    # データに基づきノードを削除する。
    def delete(self, data):
        length = self.list_length()
        temp = self.head
        # 削除するノードが先頭の場合
        if (temp.next is not None):
            if(temp.data == data):
                self.head = temp.get_next()
                temp = None
                self.length = length - 1
                return
            else:
                #  ノードを検索する。
                while temp.next is not None:
                    if temp.data == data:
                        break
                    # 現在のノードを一つ前のノードとして保存し、次に進む。
                    prev = temp          
                    temp = temp.get_next()
                # ノードが見つからなかった場合。
                if temp is None:
                    return
                
                self.length = length - 1
                prev.next = temp.get_next()
                return

    # データの検索
    def search(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        return self.search(node.get_next(), data)


def delete_min_five():
  over_five = {}
  with open("timeline_tag_rt.anony.dat","r") as f:
    for line in f:
      retweet = line.strip().split(",")
      for user in retweet:
        if not user in over_five:
          over_five[user] = 0
        over_five[user] += 1
  with open("timeline_tag_rt.anony.dat","r") as f,open("timeline_tag_rt.anony_cascade.txt","w") as wf:
    for line in f:
      retweet = line.strip().split(",")
      temp = copy.deepcopy(retweet)
      # time.sleep(1)
      for user in retweet:
        if over_five[user] < 5:
          if retweet.index(user) % 2 == 1:
            del temp[retweet.index(user)-1:retweet.index(user)+1]
          else:
            del temp[retweet.index(user):retweet.index(user)+2]
      if temp:
        wf.write(','.join(temp)+"\n")

def delete_duplicate():
  with open("timeline_tag_rt.anony_cascade.txt","r") as f,open("timeline_tag_rt.anony_cascade_1.txt","w") as wf:
      for line in f:
        templine = copy.deepcopy(line)
        retweet = list(reversed(line.strip().split(",")))
        temp = copy.deepcopy(retweet)
        t = []
        if len(temp) > 2:
          for i in range(len(temp)//2):
            if temp[i*2]+","+temp[i*2+1] not in t:
              t.append(temp[i*2]+","+temp[i*2+1])
          wf.write(",".join(t)+"\n")
          
        else:
          wf.write(','.join(temp)+"\n")
        

# if __name__ == '__main__':
#     List = LinkedList()
#     # ノード1
#     List.insert_at_start(1)           
#     # ノード1 -> ノード2
#     List.insert_at_end(2)     
#     # ノード1 -> ノード2 -> ノード3
#     List.insert_at_end(3)
#     # ノード4 -> ノード1 -> ノード2 -> ノード3 
#     List.insert_at_start(4)    
#     # ノード4 -> ノード1 -> ノード2 -> ノード5 -> ノード3
#     List.insert_position(3, 5)     
#     # ノード4 -> ノード1 -> ノード2 -> ノード5 -> ノード3 -> ノード6  
#     List.insert_at_end(6)
#     List.print_linked_list()
#     print()
#     # ノード4 -> ノード1 -> ノード2 -> ノード5 -> ノード6  
#     List.delete(3)
#     List.print_linked_list()
#     print()
#     print(List.search(List.head, 1))

# def separate_duplicate():
#   with open("timeline_tag_rt.anony_cascade_1.txt","r") as f,open("timeline_tag_rt.anony_cascade_2.txt","w") as wf:
#     for line in f:
#       retweet = line.strip().split(",")
#       temp = copy.deepcopy(retweet)
#       t = []
#       if len(temp) > 2:
#         for i in range(len(temp)//2):
#           List = LinkedList()
#           List.insert_at_start(temp[i*2])
#           List.insert_at_end(temp[i*2+1])
#           t.append(List)
#         for i in t:


def separate_duplicate():
  with open("timeline_tag_rt.anony_cascade_1.txt","r") as f,open("timeline_tag_rt.anony_cascade_2.txt","w") as wf:
    for line in f:
      retweet = line.strip().split(",")
      temp = copy.deepcopy(retweet)
      t = []
      if len(temp) > 2:
        for i in range(len(temp)//2):
          t.append([temp[i*2],temp[i*2+1]])
        t_copy = copy.deepcopy(t)
        for i in t_copy:
          for j in range(len(t_copy)):
            if t_copy[j] != []:
              if i[-1] == t_copy[j][0]:
                if i in t_copy:
                  t_copy[t_copy.index(i)] = []
                t_copy[j] = i[:-1]+t_copy[j]
        for i in t_copy:
          if i:
            temp = list(dict.fromkeys(i))
            wf.write(",;".join(temp)+"\n")
                        
      else:
        wf.write(',;'.join(temp)+"\n")
        
separate_duplicate()