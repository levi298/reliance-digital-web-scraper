from bs4 import BeautifulSoup 
import requests 

# site =requests.get("https://www.reliancedigital.in/collection/mobiles?internal_source=navigation&page_no=1&page_size=12&page_type=number&q=phones")

# print(site.status_code)
# print("bypassig")

# # for each page number:
#     build URL using that page number
#     requests.get(URL)
#     BeautifulSoup(...)
#     find product container
#     for each product:
#         get name
#         get price
lists1 = []
lists2 = []
count = 0 
x = int(input("how many page of data tho ? :")) 
# soup = BeautifulSoup(site.text, "html.parser")
# product =soup.find(class_="main-grid")
i=1
for i in range (1,x+1) :
    site = requests.get(f"https://www.reliancedigital.in/collection/mobiles?internal_source=navigation&page_no={i}&page_size=12&page_type=number&q=phones")
    soup = BeautifulSoup(site.text, "html.parser")
    product =soup.find(class_="main-grid")
    



    for product in product :

        na=(product.find("div",class_="product-card-title"))
        
        lists1.append(na.text)

        na=(product.find("div",class_="price"))
        
        lists2.append(na.text)




        count += 1


dictionaryy1 = {"names  are : ": lists1  ,  "prices are : ": lists2 }

print("counted number : ",count)
# print(dictionaryy1)
# p=1
for name, price in zip(lists1,lists2):
    print("products === ",name)
    print("prices ₹ === ",price[2::])
    print("")

    pass