import json as j,os,urllib.request as u
V=[0,100,320,330,500,900,0]
J=[14,18,31,33,-14,-18,-31,-33]
D=[15,17,-15,-17]
R=[1,-1,16,-16]
G=R+D
Z=[0,0,(J,0),(D,1),(R,1),(D+R,1),(G,0)]
T="KKKKUUUUMMOQLLMPKKKOLJIKLMMGKKKKACEECGKKEKMNELNOEKNOELMNCGKLACEEGIIIIKKKIKLMILLMIKMMIMMMILKKGIIIKKKKLMMMJKKKJKKKJKKKJKKKJKKKKKKLGIIJIKKKIKLLJKLLKKLLILLLIKLKGIIJECCAECCAECCAECCAGEECIGGGOOKKOQMKACEGEGIKEIOQEIQSEIQSEIOQEEKKAEEE"
def d(s):return tuple(0 if q&136 else(ord(s[(7-(q>>4))*4+min(q&7,7-(q&7))])-75)*5 for q in range(128))
P=[d(T[i*32:i*32+32])for i in range(6)]
W=100000
n=0
def A(b,s,y):
 for q in(s+15*(1 if y else -1),s+17*(1 if y else -1)):
  if not q&136 and b[q]==(1|y):return 1
 for q in J:
  x=s+q
  if not x&136 and b[x]==(2|y):return 1
 for q in G:
  x=s+q
  if not x&136 and b[x]==(6|y):return 1
 for q in D+R:
  x=s+q
  while not x&136:
   v=b[x]
   if v:
    if(v&8)==y and(v&7)in((3,5)if q in D else(4,5)):return 1
    break
   x+=q
 return 0
def F(b,t):
 for s in range(128):
  if b[s]==(6|t):return s
 return -1
def M(b,t,e,o=0):
 l=[]
 f2=t^8
 for f in range(128):
  p=b[f]
  if not p or(p&8)!=t:continue
  p&=7
  if p==1:
   d=16 if t==0 else -16
   h=7 if t==0 else 0
   r=1 if t==0 else 6
   q=f+d
   if not b[q]:
    if(q>>4)==h:
     for v in(5,4,3,2):l.append((9000+v*100,f|q<<7|v<<14))
    else:
     if not o:l.append((0,f|q<<7))
     if(f>>4)==r and not b[f+2*d]:
      if not o:l.append((0,f|(f+2*d)<<7))
   for q in(f+d-1,f+d+1):
    if q&136:continue
    v=b[q]
    if v and(v&8)==f2:
     if(q>>4)==h:
      for w in(5,4,3,2):l.append((10000+10*V[v&7]+w*100,f|q<<7|w<<14))
     else:l.append((10000+10*V[v&7]-1,f|q<<7))
    elif q==e and not v:l.append((10000+10*V[1]-1,f|q<<7))
  else:
   q,sl=Z[p]
   for d in q:
    x=f+d
    while not x&136:
     v=b[x]
     if not v:
      if not o:l.append((0,f|x<<7))
     else:
      if(v&8)==f2:l.append((10000+10*V[v&7]-p,f|x<<7))
      break
     if not sl:break
     x+=d
 return l
def K(b,t,e,m):
 f=m&127
 q=(m>>7)&127
 r=m>>14
 b2=bytearray(b)
 v=b2[f]
 b2[f]=0
 s=b2[q]
 if(v&7)==1 and q==e and not s:
  y=q-(16 if t==0 else -16)
  s=b2[y]
  b2[y]=0
 b2[q]=(r|t)if r else v
 return b2,(f+q)//2 if(v&7)==1 and abs(q-f)==32 else -1
def H(b,t):
 s=0
 for q in range(128):
  p=b[q]
  if not p:continue
  v=p&7
  if p&8:s-=V[v]+P[v-1][q^112]
  else:s+=V[v]+P[v-1][q]
 return s if t==0 else -s
def S(b,t,e,d,a,B):
 global n
 n+=1
 if n>W:raise StopIteration
 c=A(b,F(b,t),t^8)
 if d<=0 and not c:
  s=H(b,t)
  if s>=B:return B
  if s>a:a=s
  v=M(b,t,e,1)
 else:v=M(b,t,e)
 v.sort(key=lambda z:-z[0])
 f=-100000
 for _,m in v:
  b2,e2=K(b,t,e,m)
  if A(b2,F(b2,t),t^8):continue
  q=-S(b2,t^8,e2,d-1,-B,-a)
  if q>f:f=q
  if q>a:a=q
  if a>=B:break
 if d<=0 and not c:return a
 if f==-100000:return -99999 if c else 0
 return f
def p(s):
 q=s.split()
 b=bytearray(128)
 r=7
 for o in q[0].split("/"):
  f=0
  for h in o:
   if h.isdigit():f+=int(h)
   else:
    v="PNBRQK".index(h.upper())+1
    if h.islower():v|=8
    b[r*16+f]=v
    f+=1
  r-=1
 t=0 if q[1]=="w" else 8
 e=-1 if q[3]=="-"else(ord(q[3][1])-49)*16+(ord(q[3][0])-97)
 return b,t,e
def c(s,l):
 global n
 b,t,e=p(s)
 r=[]
 for sc,m in M(b,t,e):
  b2,e2=K(b,t,e,m)
  if A(b2,F(b2,t),t^8):continue
  r.append((sc,m))
 r.sort(reverse=True)
 r=[m for _,m in r]
 n=0
 f=r[0]
 try:
  for d in range(1,20):
   a=-100000
   B=100000
   y=f
   v2=-100000
   for m in r:
    b2,e2=K(b,t,e,m)
    q=-S(b2,t^8,e2,d-1,-B,-a)
    if q>v2:
     v2=q
     y=m
    if q>a:a=q
   f=y
   r.remove(y)
   r.insert(0,y)
 except StopIteration:pass
 return "abcdefgh"[f&7]+str(((f>>4)&7)+1)+"abcdefgh"[(f>>7)&7]+str(((f>>11)&7)+1)+("nbrq"[(f>>14)-2]if f>>14 else "")
U=os.environ["MAKEFUN_ENV_URL"]
def o(q,b):
 r=u.Request(U+q,data=j.dumps(b).encode(),headers={"content-type":"application/json"})
 with u.urlopen(r)as s:return j.load(s)
while 1:
 z=o("/game",{})
 if z["status"]=="done":break
 while z["status"]=="your_move":
  try:mv=c(z["fen"],z["legal_moves"])
  except Exception:mv=z["legal_moves"][0]
  z=o("/move",{"game":z["game"],"move":mv})
