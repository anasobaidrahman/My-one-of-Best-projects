import random
class Enemy():
    def __init__(self, lives, hit_points, name='Enemy'):
        self.name = name
        self.lives = lives
        self.hit_points = hit_points
        self.max_hit_points = hit_points

    def take_dmg(self, damage):
        self.hit_points -= damage

        if self.hit_points > 0:
            print(f"{self.name} took {damage} damage. Remaining HP: {self.hit_points}")

        else:
            self.lives -= 1
            if self.lives > 0:
                print(f"{self.name} lost a life! Lives left: {self.lives}")
                overflow = abs(self.hit_points)
                self.hit_points = self.max_hit_points - overflow
                print(f"{self.name}'s HP is reset to {self.hit_points} for the new life.")
            else:
                self.hit_points = 0
                print(f"{self.name}: Arrrgggggh! I died 💀")

    def __str__(self):
        return f'Enemy name:{self.name},Hit points:{self.hit_points},lives:{self.lives}'

class Brain_eater(Enemy):
    def __init__(self,name):
        super().__init__(lives=3,hit_points=45,name=name)
    def duck(self):
        if random.randint(1,5)==5:
            print(f'*******{self.name} is ducked and saaved!')
            return True
        else:
            return False
    def take_dmg(self, damage):
        if not self.duck():
            super().take_dmg(damage=damage)

class king_Brain_eater(Brain_eater):

    def __init__(self,name):
        super().__init__(name)
        self.hit_points=150

    def take_dmg(self, damage):
        super().take_dmg(damage=damage/4)
