# Bounding Box 그리기
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
ax.imshow(image)

# 각 어노테이션에 대해 바운딩 박스 그리기
for anno in annotations:
    bbox = anno["bbox"]
    class_name = anno["class"]
    
    # 클래스에 따른 색상 설정
    color = "red" if class_name == "cat" else "blue"
    
    # 바운딩 박스 그리기
    draw_bbox(ax, bbox, class_name, color)

ax.set_title(f"Bounding Box Visualization: {train_example_image_name}")
ax.axis("off")
plt.tight_layout()
plt.show()

# 어노테이션 정보 출력
print(f"이미지: {train_example_image_name}")
print(f"감지된 객체 수: {len(annotations)}")
for i, anno in enumerate(annotations):
    print(f"  객체 {i+1}: {anno['class']} - BBox: {anno['bbox']}") 