from random import randint

class Product:
    stock_amount = 0
    
    def __init__(self, monthly_production):
        self.monthly_production = monthly_production
    
    """
    a class method which changes the class variable "stock_amount" to the
    stock amount of the current month
    """
    @classmethod
    def change_stock_amount(cls,stock_amount):
        cls.stock_amount = stock_amount

    """
    the units_sold method creates a range using the monthly_production
    a random integer taken from that range determines the units sold
    """
    def units_sold(self, monthly_production):
        self.minus_range = monthly_production - 10
        self.plus_range = monthly_production + 10
        self.units_sold = randint(self.minus_range, self.plus_range)
        return self.units_sold
    
    """
    a method which determines how much stock is remaining it uses the class variable
    stock amount as the number of stock from the previous month then
    """
    @classmethod
    def stock_quantity(cls, monthly_production, units_sold):
        cls.stock_level = cls.stock_amount + monthly_production
        cls.stock_level = cls.stock_level - units_sold
        return cls.stock_level

print("Welcome to Programming Principles Sample Product Iventory")

product_code = int(input("Please enter the Product Code: "))
while product_code < 100 or product_code > 1000:
    product_code = int(input("Please enter the Product Code: "))
    if product_code >= 100 and product_code <= 1000:
        break
    else:
        continue
product_name = input("Please enter the Product Name: ")
current_stock = int(input("Pleae enter the Current Stock: "))
while current_stock <= 0:
    current_stock = int(input("Pleae enter the Current Stock: "))
    if current_stock > 0:
        break
    else:
        continue
sale_price = float(input("Please enter the Product Sale Price: "))
while sale_price <= 0:
    sale_price = float(input("Please enter the Product Sale Price: "))
    if sale_price > 0:
        break
    else:
        continue
manufacture_cost = float(input("Please enter the Product Manufacture Cost: "))
while manufacture_cost <= 0:
    manufacture_cost = float(input("Please enter the Product Manufacture Cost: "))
    if manufacture_cost > 0:
        break
    else:
        continue
monthly_production = int(input("Please enter estimated monthly production: "))
while monthly_production < 0:
    monthly_production = int(input("Please enter estimated monthly production: "))
    if monthly_production >= 0:
        break
    else:
        continue




#first month
month1 = Product(monthly_production)
print("Month 1:")
print("\tMonthly Production: ", month1.monthly_production)
print("\tUnits Sold: ", month1.units_sold(monthly_production))

Product.change_stock_amount(current_stock)

Product.stock_quantity(monthly_production, month1.units_sold)
print("\tStock: ", month1.stock_level)


#second month
month2 = Product(monthly_production)
print("Month 2:")
print("\tManufactured: ", month2.monthly_production)
print("\tUnits Sold: ", month2.units_sold(monthly_production))

Product.change_stock_amount(month1.stock_level)
Product.stock_quantity(monthly_production, month2.units_sold)
print("\tStock: ", month2.stock_level)

#third month
month3 = Product(monthly_production)
print("Month 3:")
print("\tMonthly Production: ", month3.monthly_production)
print("\tUnits Sold: ", month3.units_sold(monthly_production))

Product.change_stock_amount(month2.stock_level)
Product.stock_quantity(monthly_production, month3.units_sold)
print("\tStock: ", month3.stock_level)

#4th month
month4 = Product(monthly_production)
print("Month 4:")
print("\tMonthly Production: ", month4.monthly_production)
print("\tUnits Sold: ", month4.units_sold(monthly_production))

Product.change_stock_amount(month3.stock_level)
Product.stock_quantity(monthly_production, month4.units_sold)
print("\tStock: ", month4.stock_level)

#5th month
month5 = Product(monthly_production)
print("Month 5:")
print("\tMonthly Production: ", month5.monthly_production)
print("\tUnits Sold: ", month5.units_sold(monthly_production))

Product.change_stock_amount(month4.stock_level)
Product.stock_quantity(monthly_production, month5.units_sold)
print("\tStock: ", month5.stock_level)

#6th month
month6 = Product(monthly_production)
print("Month 6:")
print("\tMonthly Production: ", month6.monthly_production)
print("\tUnits Sold: ", month6.units_sold(monthly_production))

Product.change_stock_amount(month5.stock_level)
Product.stock_quantity(monthly_production, month6.units_sold)
print("\tStock: ", month6.stock_level)

#7th month
month7 = Product(monthly_production)
print("Month 7:")
print("\tMonthly Production: ", month7.monthly_production)
print("\tUnits Sold: ", month7.units_sold(monthly_production))

Product.change_stock_amount(month6.stock_level)
Product.stock_quantity(monthly_production, month7.units_sold)
print("\tStock: ", month7.stock_level)

#8th month
month8 = Product(monthly_production)
print("Month 8:")
print("\tMonthly Production: ", month8.monthly_production)
print("\tUnits Sold: ", month8.units_sold(monthly_production))

Product.change_stock_amount(month7.stock_level)
Product.stock_quantity(monthly_production, month8.units_sold)
print("\tStock: ", month8.stock_level)

#9th month
month9 = Product(monthly_production)
print("Month 9:")
print("\tMonthly Production: ", month9.monthly_production)
print("\tUnits Sold: ", month9.units_sold(monthly_production))

Product.change_stock_amount(month8.stock_level)
Product.stock_quantity(monthly_production, month9.units_sold)
print("\tStock: ", month9.stock_level)

#10th month
month10 = Product(monthly_production)
print("Month 10:")
print("\tMonthly Production: ", month10.monthly_production)
print("\tUnits Sold: ", month10.units_sold(monthly_production))

Product.change_stock_amount(month9.stock_level)
Product.stock_quantity(monthly_production, month10.units_sold)
print("\tStock: ", month10.stock_level)

#11th month
month11 = Product(monthly_production)
print("Month 11:")
print("\tMonthly Production: ", month11.monthly_production)
print("\tUnits Sold: ", month11.units_sold(monthly_production))

Product.change_stock_amount(month10.stock_level)
Product.stock_quantity(monthly_production, month11.units_sold)
print("\tStock: ", month11.stock_level)

#12th month
month12 = Product(monthly_production)
print("Month 12:")
print("\tMonthly Production: ", month12.monthly_production)
print("\tUnits Sold: ", month12.units_sold(monthly_production))

Product.change_stock_amount(month11.stock_level)
Product.stock_quantity(monthly_production, month12.units_sold)
print("\tStock: ", month12.stock_level)

total_units_sold = month1.units_sold + month2.units_sold + month3.units_sold+  month4.units_sold + month5.units_sold + month6.units_sold + month7.units_sold + month8.units_sold + month9.units_sold + month10.units_sold + month11.units_sold + month12.units_sold
total_units_manufactured = monthly_production * 12

net_profit = (total_units_sold * sale_price) - (total_units_manufactured * manufacture_cost)
net_profit = round(net_profit,2)
print("Net Profit: ", "$" + str(net_profit), "CAD")