def Ex_Euclid(a,b):
  if 0==b:
    x=1;y=0;q=a
    return x,y,q
  xyq=Ex_Euclid(b,a%b)
  x=xyq[0];y=xyq[1];q=xyq[2]
  temp=x;x=y;y=temp-a//b*y
  return x,y,q
 
#获取a的逆元(mod b)的函数，目的是为了封装获取逆元的功能
def Get_Inverse(a,b):
  return Ex_Euclid(a,b)[0]
 
#获取a和b的最大公约数函数，目的是为了封装获取最大公约数的功能
def gcd(a,b):
  return Ex_Euclid(a,b)[2]
 
#判断所有的mi是否两两互质
def Is_Coprime(m_list):
  for i in range(len(m_list)):
    for j in range(i+1,len(m_list)):
      if 1!=gcd(m_list[i],m_list[j]):
        return 0  #返回0表示不是两两互质的
  return 1  #返回1表示是两两互质的
 
#获取所有的Mi
def Get_Mi(m_list,M):
  Mi_list=[]
  for mi in m_list:
    Mi_list.append(M//mi)
  return Mi_list
 
#获取所有的Mi的逆元
def Get_Mi_inverse(Mi_list,m_list):
  Mi_inverse=[]
  for i in range(len(Mi_list)):
    Mi_inverse.append(Get_Inverse(Mi_list[i],m_list[i]))
  return Mi_inverse
 
#中国剩余定理,返回值为最终的x
def C_R_T():
  while True:
    #两个空列表，分别用来保存mi和bi
    m_list=[]
    b_list=[]
    
    while True: #输入mi
      m_i=input("请输入mi,以'.'结束输入:")
      if m_i=='.':
        break
      elif False==m_i.isnumeric():
        print("输入有误，请输入数字:")
        m_i=input()
        continue
      else:
        m_list.append(int(m_i))
    
    while True: #输入bi
      b_i=input("请输入bi,以'.'结束输入:")
      if b_i=='.':
        break
      elif False==b_i.isnumeric():
        print("输入有误，请输入数字！\n")
        b_i=input()
        continue
      else:
        b_list.append(int(b_i))
    
    if len(m_list)!=len(b_list):
      print("错误！mi的个数和bi的个数不相同，请重新输入\n")
    elif 0==Is_Coprime(m_list):
      print("错误！输入的mi并不是两两互质的，请重新输入mi\n")
    else:
      break
  
  M=1 #M是所有mi的乘积
  for mi in m_list:
    M*=mi
  
  Mi_list=Get_Mi(m_list,M)
  Mi_inverse=Get_Mi_inverse(Mi_list,m_list)
  x=0
  for i in range(len(b_list)):  #开始计算x
    x+=Mi_list[i]*Mi_inverse[i]*b_list[i]
    x%=M
  return x
 
if __name__=='__main__':
  print("同余式组的解为：x=%d" % C_R_T())