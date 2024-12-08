import os
import glob
from PIL import Image

def rotate_images_90_and_save(folder_path):
    # Verilerin olduğu klasörle aynı dizinde rotate_90 klasörünü oluştur (eğer yoksa)
    parent_folder_path = os.path.dirname(folder_path)
    rotate_90_folder_path = os.path.join(parent_folder_path, "rotate_90")
    os.makedirs(rotate_90_folder_path, exist_ok=True)
    
    # Klasördeki tüm .jpg dosyalarını bul
    image_paths = glob.glob(os.path.join(folder_path, "*.jpg"))
    
    for image_path in image_paths:
        # Resmi oku
        image = Image.open(image_path)
        
        # Resmi 90 derece döndür
        rotated_image = image.rotate(90, expand=True)
        
        # Yeni dosya adı oluştur
        base_name = os.path.basename(image_path)
        new_name = f"{os.path.splitext(base_name)[0]}_rotate_90.jpg"
        new_path = os.path.join(rotate_90_folder_path, new_name)
        
        # 90 derece döndürülmüş resmi kaydet
        rotated_image.save(new_path)

# Örnek kullanım
folder_path = "/path/to/your/images"  # Kendi klasör yolunuzu buraya ekleyin
rotate_images_90_and_save(folder_path)



#rotate_images_90_and_save("C:\\Users\\TUF Dash F15\\Desktop\\DataCogalt\\veri")