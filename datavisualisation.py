import matplotlib.pyplot as plt





years=[1950,1992,1940,1930,3900,1912,1913,1914,1915,1916,1917,1918,1920,1921,1922]
pops =[2456,3789,2898,2001,2030]
deaths=[1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.1,2.3,3.4,3.5  ]

plt.plot(years,pops, colour=(255/255,100/255,100/255))
plt.plot(years,deaths, colour=(0/255,100/255,100/255))
plt.ylabel('population in billions')
plt.xlabel('population growth by year')
plt.title('population growth')
plt.show()
