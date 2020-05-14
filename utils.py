import matplotlib.pyplot as plt

def plot_xv(x,v,t=None, title='', ax1xlim=None, ax1ylim=None, ax2xlim=None, ax2ylim=None):
    if t is None:
        t = range(len(x))
    # First plot plots x and v against t.
    plt.subplot(1,2,1)
    plt.plot(t,x,label='x')
    plt.plot(t,v,label='v')
    plt.xlabel('t')
    plt.xlim(ax1xlim); plt.ylim(ax1ylim);
    plt.legend()
    plt.title(title)
    
    # Second plot plots trajectory in phase-space (x,v)
    plt.subplot(1,2,2)
    plt.plot(x, v,color='black')
    plt.scatter(x[0], v[0], label='start', color='black')
    plt.legend()
    plt.xlabel('x'); plt.ylabel('v')
    plt.xlim(ax2xlim); plt.ylim(ax2ylim);
    plt.title('State Space Plot')
