import numpy as np

class FiberLossCalculator:
    def __init__(self, fiber_length_km=1.0, alpha_db_km=0.2, connector_loss_db=0.5, splice_loss_db=0.1, num_connectors=2, num_splices=1):
        self.fiber_length_km = fiber_length_km
        self.alpha_db_km = alpha_db_km
        self.connector_loss_db = connector_loss_db
        self.splice_loss_db = splice_loss_db
        self.num_connectors = num_connectors
        self.num_splices = num_splices

    def linear_loss(self):
        return self.alpha_db_km * self.fiber_length_km

    def connector_loss(self):
        return self.num_connectors * self.connector_loss_db

    def splice_loss(self):
        return self.num_splices * self.splice_loss_db

    def fresnel_loss(self, n1=1.46, n2=1.0):
        R = ((n1 - n2) / (n1 + n2)) ** 2
        return -10 * np.log10(1 - R)

    def total_loss(self):
        return (
            self.linear_loss() +
            self.connector_loss() +
            self.splice_loss() +
            self.fresnel_loss()
        )