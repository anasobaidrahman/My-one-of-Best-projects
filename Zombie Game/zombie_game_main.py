from player_zombie import player

from enemy_zombie import Enemy,Brain_eater,king_Brain_eater
# Big_mouth=Enemy(3,8,'Big mouth Monster')
# print(Big_mouth)
# Big_mouth.take_dmg(5)
# print(Big_mouth)
# Big_mouth.take_dmg(6)
# print(Big_mouth)
# Big_mouth.take_dmg(7)
# print(Big_mouth)
# Big_mouth.take_dmg(8)
# print(Big_mouth)
# Big_mouth.take_dmg(8)
# print(Big_mouth)
import time
start_time=time.time()
brain_eater=king_Brain_eater('brain eater')
while brain_eater.lives>0:
    brain_eater.take_dmg(1)
end_time=time.time()
req_time=end_time-start_time
print(req_time)
























