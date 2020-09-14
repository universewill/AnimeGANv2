
import os
import cv2
import random


def get_images_list_in_dir(dir):
    files = os.listdir(dir)
    image_files = [f for f in files if f.split('.')[-1] in ('jpg', 'jpeg', 'png', 'tif', 'tiff')]
    return image_files


def random_crop(image, length):
    h, w, c = image.shape
    start_x = random.randint(0, w - length - 1)
    start_y = random.randint(0, h - length - 1)
    return image[start_y:start_y+length, start_x:start_x+length, :]


def random_resize_and_crop(image, length, ratio=[0.4, 1.0]):
    h, w, c = image.shape
    ratio = random.uniform(0.5, 1.0)
    ratio = max(256.0/h, 256.0/w, ratio)

    new_w = int(ratio * w) + 1
    new_h = int(ratio * h) + 1
    image = cv2.resize(image, (new_w, new_h))

    image_crop = random_crop(image, length)
    return image_crop


def crop_style_images():
    data_dir ='../data/veer'
    save_dir = '../dataset/fabric/style'

    # data_dir ='../data/pair/描稿图'
    # save_dir = '../dataset/fabric/style'
    image_names = get_images_list_in_dir(data_dir)
    for epoch in range(0, 15):
        random.shuffle(image_names)
        for i, name in enumerate(image_names):
            image = cv2.imread('%s/%s' % (data_dir, name))
            image_crop = random_crop(image, 256)
            save_path = '%s/%s.jpg' % (save_dir, epoch*len(image_names)+i)
            cv2.imwrite(save_path, image_crop)
    return None


def crop_fabric_images():
    data_dir ='../data/pair/扫描稿'
    save_dir = '../dataset/train_photo'
    image_names = get_images_list_in_dir(data_dir)
    for epoch in range(0, 15):
        random.shuffle(image_names)
        for i, name in enumerate(image_names):
            image = cv2.imread('%s/%s' % (data_dir, name))
            image_crop = random_crop(image, 256)
            save_path = '%s/%s.jpg' % (save_dir, epoch*len(image_names)+i)
            cv2.imwrite(save_path, image_crop)
    return None


if __name__ == "__main__":
    crop_style_images()
    crop_fabric_images()
    pass