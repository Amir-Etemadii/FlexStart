from django.contrib.auth.hashers import BasePasswordHasher
import argon2

class CustomArgon2PasswordHasher(BasePasswordHasher):
    algorithm = 'argon2'
    memory_cost = 200000
    time_cost = 4
    parallelism = 4
    salt_length = 20

    def encode(self, password, salt=None):
        hasher = argon2.PasswordHasher(
            memory_cost=self.memory_cost,
            time_cost=self.time_cost,
            parallelism=self.parallelism,
            salt_len=self.salt_length,
            type=argon2.Type.ID
        )
        return hasher.hash(password)

    def verify(self, password, encoded):
        hasher = argon2.PasswordHasher()
        return hasher.verify(encoded, password)

    def safe_summary(self, encoded):
        return {
            'algorithm': self.algorithm,
            'memory_cost': self.memory_cost,
            'time_cost': self.time_cost,
            'parallelism': self.parallelism,
        }