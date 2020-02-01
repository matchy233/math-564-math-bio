import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

matplotlib.rc('text', usetex=True)

def cobwebbing(x0, fun, output_x, output_y, curr_layer=0, max_layer=50):
    if curr_layer == 0:
        output_x.append(0)
        output_y.append(x0)
    else:
        output_x.append(curr_layer)
        output_y.append(fun(x0))
    if curr_layer >= max_layer:
        return
    cobwebbing(fun(x0), fun, output_x, output_y, curr_layer+1, max_layer)

def plot_cobwebbing(x0, fun, x_bar, title):
    """ Use the cobwebbing method to plot a higher-order difference equation
    Args:
        x0: initial value
        f: the function describing the mapping: x_n+1 = f(x_n)
        x_bar: the steady state
        title: the title of the figure to save
    """
    x = []; y = []
    cobwebbing(x0, fun, x, y, max_layer=20)
    plt.figure()
    plt.plot(x, y, '--o')
    plt.xticks(range(0, 21))
    plt.xlabel("$x_n$")
    plt.ylabel("$x_{n+1}$")
    plt.axhline(x_bar, color="red")
    file_name = rf"./fig/{title}.pdf"
    if os.path.isfile(file_name):
        os.remove(file_name)
    plt.savefig(file_name)

def plot_logis_lambda(r, K):
    x = np.arange(2*K)
    y = list(map(lambda x: pow(np.e, r*(1-x/K)), x))
    plt.plot(x, y)
    plt.xlabel("$N$")
    plt.ylabel(r"$\lambda$")
    plt.axvline(K, linestyle='--', color='r')
    ytick, fig = plt.yticks()
    xtick, fig = plt.xticks()
    y_mid = ytick[len(ytick)//2+1]
    x_int = xtick[1] - xtick[0]
    del fig, xtick, ytick
    plt.text(K+0.1*x_int, y_mid, 'N = K', 
            rotation=-90, fontsize=12, color="red")
    plt.axhline(1, xmax=0.5, linestyle='--', color='r', label=r"$\lambda = 1$")
    plt.plot(K, 1, 'ro')
    plt.show()

def main():
    plot_cobwebbing(0.001, lambda x: 2*x*(1-x), 0, "fig2(a)")
    plot_cobwebbing(
        1.6,
        lambda x: -(x**2)*(1-x),
        (1+np.sqrt(5))/2, "fig2(b)")
    plot_cobwebbing(
        0.4,
        lambda x: 1/(2+x),
        np.sqrt(2)-1,
        "fig2(c)"
    )
    plot_cobwebbing(
        1.648,
        lambda x: x*np.log(x**2),
        np.e**0.5,
        "fig2(d)"
    )

if __name__ == "__main__":
    plot_logis_lambda(2, 50)