store=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c=input()
for i in c:
    print(store[store.index(i)+c.count(i)],end=" ")
