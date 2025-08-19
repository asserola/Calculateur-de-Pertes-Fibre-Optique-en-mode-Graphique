import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_fiber_losses(calculator, master):
    labels = ['Perte linéique', 'Pertes connecteurs', 'Pertes épissures', 'Perte Fresnel', 'Perte totale']
    values = [
        calculator.linear_loss(),
        calculator.connector_loss(),
        calculator.splice_loss(),
        calculator.fresnel_loss(),
        calculator.total_loss()
    ]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Bar plot
    ax1.bar(labels, values, color=colors)
    ax1.set_title("Détail des pertes (dB)")
    ax1.set_ylabel("Perte (dB)")
    ax1.grid(axis='y', linestyle='--', alpha=0.7)

    # Pie chart
    ax2.pie(values[:-1], labels=labels[:-1], autopct='%1.1f%%', colors=colors[:-1])
    ax2.set_title("Répartition des pertes")

    plt.tight_layout()

    # Embed in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.draw()
    canvas.get_tk_widget().pack(side="top", fill="both", expand=True)