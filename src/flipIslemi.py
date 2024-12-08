import os
import glob
from PIL import Image

def flip_images_in_folder(folder_path):
    # Verilerin olduğu klasörle aynı dizinde Flip klasörünü oluştur (eğer yoksa)
    parent_folder_path = os.path.dirname(folder_path)
    flip_folder_path = os.path.join(parent_folder_path, "flip")
    os.makedirs(flip_folder_path, exist_ok=True)
    
    # Klasördeki tüm .jpg dosyalarını bul
    image_paths = glob.glob(os.path.join(folder_path, "*.jpg"))
    
    for image_path in image_paths:
        # Resmi oku
        image = Image.open(image_path)
        
        # Resme flip uygula (horizontal flip)
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        
        # Yeni dosya adı oluştur
        base_name = os.path.basename(image_path)
        new_name = f"{os.path.splitext(base_name)[0]}_flip.jpg"
        new_path = os.path.join(flip_folder_path, new_name)
        
        # Flip uygulanmış resmi kaydet
        flipped_image.save(new_path)

# Örnek kullanım
folder_path = "/path/to/your/images"  # Kendi klasör yolunuzu buraya ekleyin
flip_images_in_folder(folder_path)

# Kullanım örneği:
# flip_images_in_folder('/path/to/your/folder')

#flip_images_in_folder("C:\\Users\\TUF Dash F15\\Desktop\\DataCogalt\\veri\\Original")