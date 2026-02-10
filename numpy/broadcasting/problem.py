price=[100,200,300]
dis=10
final_price=[]
for p in price:
    
        final_prices=(p - p*dis/100)
        final_price.append(final_prices)
print(final_price)