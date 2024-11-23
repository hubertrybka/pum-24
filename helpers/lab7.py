import torch.nn as nn
import torch

class Encoder(nn.Module):
    def __init__(self, latent_size):
        super(Encoder, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.fc2 = nn.Linear(256, 64)
        self.fc_mu = nn.Linear(64, latent_size)
        self.fc_logvar = nn.Linear(64, latent_size)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        mu = self.fc_mu(x)
        logvar = self.fc_logvar(x)
        return mu, logvar


class Decoder(nn.Module):
    def __init__(self, latent_size):
        super(Decoder, self).__init__()
        self.fc1 = nn.Linear(latent_size, 64)
        self.fc2 = nn.Linear(64, 256)
        self.fc3 = nn.Linear(256, 784)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x


class VAE(nn.Module):
    def __init__(self, latent_size):
        super(VAE, self).__init__()
        self.encoder = Encoder(latent_size)
        self.decoder = Decoder(latent_size)

    def forward(self, x):
        mu, logvar = self.encoder(x)
        z = self.reparametrize(mu, logvar)
        x_hat = self.decoder(z)
        return x_hat, mu, logvar

    def reparametrize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std  # reparametrization trick!


class VAELoss(nn.Module):
    def __init__(self):
        super(VAELoss, self).__init__()
        self.binary_cross_entropy = nn.BCELoss(reduction='sum')

    def forward(self, x_hat, x, mu, sigma):
        # calculate the reconstruction loss
        recon_loss = self.binary_cross_entropy(x_hat, x)

        # calculate the KL divergence loss
        kl_loss = -0.5 * torch.sum(1 + sigma - mu ** 2 - sigma.exp())

        return recon_loss + kl_loss

