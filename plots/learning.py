import pandas as pd
import matplotlib.pyplot as plt 


things = '2000'
code = '1_' + things + '_1000_1'
#code = '1_200_1000_1'
#code = '1_500_1000_1'
#code = '1_1000_1000_1'
#code = '1_2000_1000_1'
#code = '1_5000_1000_1'


df = pd.read_csv('../saidas/TS/' + code + '_solution.csv', sep=';')



y = df['Solution']
x = list(range(1, len(y)+1))

fig,ax = plt.subplots()

fig.set_size_inches(6, 4)
ax.plot(x, y, "-", label="Complete model", linewidth=2.0, markersize=12, color='#006bb3')

ax.set_xlabel("Iteração", fontsize=24, labelpad=8)
ax.set_ylabel("Valor total",fontsize=24)

xticks = [0, 200,  400, 600]

ax.set_xticks(xticks)
ax.set_xticklabels(xticks, fontsize=22)


yticks = [0, 25000, 50000, 75000, 100000]
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=22)
#tkw = dict(size=4, width=1.5)
#ax.tick_params(axis='y', **tkw, labelsize=22)

ax.set_title('KSP '+ things + ' itens', fontsize=22)
#ax.tick_params(axis='x', **tkw, labelsize=16)

ax.grid(b=True, which='major', linestyle='--')

plt.savefig(code + ".pdf", bbox_inches='tight')
plt.savefig(code + ".png", bbox_inches='tight')

#plt.show()