import os
import shutil

base_dir = 'images'
test_dir = 'test'
train_dir = 'train'

if(os.path.exists(train_dir)):
    shutil.rmtree(train_dir)
if(os.path.exists(test_dir)):
    shutil.rmtree(test_dir)

os.mkdir(test_dir)
os.mkdir(train_dir)

for d in os.listdir(base_dir):
    dogs = os.listdir(f"{base_dir}/{d}")
    print(len(dogs))
    test_len = int(len(dogs) * 0.3)
    print("test", test_len)

    train_len = len(dogs) - test_len
    print("train", train_len)

    os.mkdir(f"{test_dir}/{d}")
    os.mkdir(f"{train_dir}/{d}")

    for dog in dogs[:test_len]:
        shutil.copy(f'{base_dir}/{d}/{dog}', f'{test_dir}/{d}/{dog}')

    for dog in dogs[test_len:(train_len + test_len)]:  # [pointdepart: nombrediteration]
        shutil.copy(f'{base_dir}/{d}/{dog}', f'{train_dir}/{d}/{dog}')

