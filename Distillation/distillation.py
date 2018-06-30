import matplotlib.pyplot as plt
import numpy as np


class PressureCompositionDiagram:
    """Requires two pure vapour pressures as initialiser arguments, and the
    names of the components, in the sequence vapour pressure, name,
    vapour pressure, name. The more volatile should come first
    """
    def __init__(self, pure_vapour_pressureA, name_of_A, pure_vapour_pressureB, name_of_B):
        self.pvp1 = pure_vapour_pressureA
        self.name1 = name_of_A
        self.pvp2 = pure_vapour_pressureB
        self.name2 = name_of_B
        self.total_pressure = [
            [0, 1],
            [pure_vapour_pressureA, pure_vapour_pressureB]
        ]

    def configure_base_plot(self):
        scale_max = max([self.pvp1, self.pvp2])
        fig, ax = plt.subplots(1, 1)
        ax.set_xticks(np.arange(0, 1, 0.1))
        # ax.set_yticks(np.arange(0, scale_max + 1, scale_max/10))
        ax.plot(*self.total_pressure, label='Total Pressure')
        ax.plot(
            [0, 1],
            [0, self.pvp2],
            label='Partial Pressure of {}'.format(self.name2),
        )
        ax.plot(
            [0, 1],
            [self.pvp1, 0],
            label='Partial Pressure of {}'.format(self.name1),
        )
        plt.xlabel('Mole Fraction of {}'.format(self.name2))
        plt.ylabel('Pressure (kPa)')
        plt.grid(True)

        return fig, ax

    def show_plot(self):
        self.configure_base_plot()
        plt.show()

    def find_pressures_at_mole_fractions(self, mf):
        pA = ( (0 - self.pvp1) / (1 - 0) ) * mf + self.pvp1
        pB = self.pvp2 * mf
        pTot = pA + pB
        return pA, pB, pTot

    def mole_fraction_plot(self, mole_fraction_of_B):
        pA, pB, pTot = self.find_pressures_at_mole_fractions(mole_fraction_of_B)
        fig, ax = self.configure_base_plot()
        ax.plot(
            [mole_fraction_of_B for i in range(0, 4)],
            [0, pA, pB, pTot],
            'k--'
        )
        ax.plot(
            [0, mole_fraction_of_B],
            [pA, pA],
            'k--'
        )
        ax.plot(
            [0, mole_fraction_of_B],
            [pB, pB],
            'k--'
        )
        ax.plot(
            [0, mole_fraction_of_B],
            [pTot, pTot],
            'k--'
        )
        plt.legend()
        plt.show()


if __name__ == "__main__":
    a = PressureCompositionDiagram(67, 'A', 20, 'B')
    a.mole_fraction_plot(0.6)
