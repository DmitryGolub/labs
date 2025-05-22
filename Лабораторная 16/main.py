import face_recognition

img1 = face_recognition.load_image_file("img1.jpg")
img2 = face_recognition.load_image_file("img2.jpg")

img1_encoding = face_recognition.face_encodings(img1)[0]
img2_encoding = face_recognition.face_encodings(img2)[0]

results = face_recognition.compare_faces([img1_encoding], img2_encoding)

if results[0]:
    print("✅ Лица совпадают!")

else:
    print("❌ Лица разные!")
