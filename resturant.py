class Resturant:
    def customeruniqueness(self,id):
        if len(id)!=len(set(id)):
            print('customer id must be unique')
    def uniquness(self,cust_id,menu_id):
        matches=dict()
        for i in range(len(menu_id)):
            matches[cust_id[i]]=menu_id.count(menu_id[i])
        for j in matches.values():
            if j>1:
                print("duplicate menu id are present")
                break
            
    def maxOrderedItem(self,orders):
        li=[]
        rating=dict()
        for i in orders.values():
            if len(i)>1:
                for j in range(len(i)):
                    li.append(i[j])
            else:
                li.append(i[0])
        for i in set(li):
            rating[i]=li.count(i)
        return list(zip(rating.values(),rating.keys()))  
path='dishes.txt'
customer_id=[]
menu_id=[]
orders=dict()
with open(path,'r') as fh:
    for line in fh:
        customer_id.append(line.split()[0])
        menu_id.append(line.split()[1])
        orders[line.split()[1]]=list(line.split()[2:])
#print(customer_id)
#print(menu_id)
#print(type(orders))
c1=Resturant()
c1.customeruniqueness(customer_id)
c1.uniquness(customer_id,menu_id)
maxitem=c1.maxOrderedItem(orders)
maxitem.sort(reverse=True)
maxitem=maxitem[0:3]
for i in maxitem:
    print("most ordered item by the customer is %s"%(i[1]))