import random

l1 = [chr(a) for a in range(49,58)]
l2 = [chr(a) for a in range(65,91)]
l3 = [chr(a) for a in range(97,123)]
l4 = ["@","#","$","%"]

full_dict = [*l1,*l2,*l3,*l4]

random.shuffle(full_dict)

raw_pass = []
shuffle_pass = []
final_pass = ""

raw_pass.append(random.choice(l1))
raw_pass.append(random.choice(l2))
raw_pass.append(random.choice(l3))
raw_pass.append(random.choice(l4))

for _ in range(4,16):
    raw_pass.append(random.choice(full_dict))

shuffle_pass = random.sample(raw_pass,len(raw_pass))
final_pass = final_pass.join(shuffle_pass)

print(final_pass)
