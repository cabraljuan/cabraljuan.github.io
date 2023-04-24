
#### Cobb douglas
def cobb_douglas(alpha,beta,p1,p2,w):
    marshall_x1=(w/p1)*(alpha/(alpha+beta))
    marshall_x2=(w/p2)*(beta/(alpha+beta))
    utility=(marshall_x1**alpha)*(marshall_x2**beta)
    print("Marshall demand x1:",marshall_x1)
    print("Marshall demand x2:",marshall_x2)
    print("Utility with marshall demands:",utility)