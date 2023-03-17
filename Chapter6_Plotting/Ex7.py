import numpy as np
import matplotlib.pyplot as plt
factor_tan = [1., 3., 5.]
factor_cot = [1., 2.]
x = np.linspace(-2.6*np.pi, 2.6*np.pi, 200)
y = np.sqrt((8./x)**2-1.)
tan = np.tan(x)
ytanM = np.ma.masked_where(np.abs(tan) > 20., tan)
cot = 1.0/tan
ycotM = np.ma.masked_where(np.abs(cot) > 20., cot)
plt.rc('mathtext', fontset='stix')
fig, ax = plt.subplots(2,1, figsize=(8,6), sharex=True, sharey=True)
ax[0].plot(x, ytanM)
ax[0].plot(x,y, linestyle=':')
ax[1].plot(x, ycotM)
ax[1].plot(x,-y, linestyle=':')
ax[0].set_xlim(0, 8)
ax[0].set_ylim(-7.5, 7.5)
ax[0].set_ylabel(r'$\tan\theta$')
ax[1].set_xlabel(r'$\theta$')
ax[1].set_ylabel(r'$\cot\theta$')
for i_tan in factor_tan:
    ax[0].axvline(x= i_tan* np.pi / 2, color="gray", linestyle='--')
for i_cot in factor_cot:
    ax[1].axvline(x= i_cot* np.pi, color="gray", linestyle='--')
for j in range(2):
    ax[j].axhline(color='gray', zorder=-1)

fig.show()