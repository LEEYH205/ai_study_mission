# XML 파일에서 Bounding Box와 클래스 정보 추출 (수정된 버전)
for obj in root.findall("object"):
    class_name = obj.find("name").text  # 클래스 이름
    bndbox = obj.find("bndbox")
    x_min = int(bndbox.find("xmin").text) if bndbox.find("xmin").text else 0
    y_min = int(bndbox.find("ymin").text) if bndbox.find("ymin").text else 0
    x_max = int(bndbox.find("xmax").text) if bndbox.find("xmax").text else 0
    y_max = int(bndbox.find("ymax").text) if bndbox.find("ymax").text else 0

    print(f"Class: {class_name}, Bounding Box: ({x_min}, {y_min}, {x_max}, {y_max})") 