import matplotlib.pyplot as plt
categories = ["Food","Travel","Shopping"]
expenses = [500,300,200]
explode = [0.1,0,0]
plt.pie(
    expenses,
    labels = categories,
    autopct ='%1.1f%%',
    explode = explode,
    shadow = True,
    startangle = 90
)
plt.title("category breakdown of expenses")
plt.show()