from django.shortcuts import render
import cv2
import numpy as np
import base64
from django.core.files.base import ContentFile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ScannedDocument
from .serialiers import ScanSerializer

from django.http import StreamingHttpResponse

def generate_frames():
    cap = cv2.VideoCapture(0)  # Use 0 for the default webcam
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # _, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # contours, hierarchy = cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame, contours, -1, (0,255,0), thickness = 2)
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

def video_feed(request):
    response = StreamingHttpResponse(generate_frames(), content_type="multipart/x-mixed-replace; boundary=frame")
    response["Access-Control-Allow-Origin"] = "*"  # Allow all (or restrict it)
    return response


def decode_base64_image(image_data):
    format, imgstr = image_data.split(';base64,')
    ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name="uploaded." + ext)

def process_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)
    return edged

@api_view(['POST'])
def scan_image(request):
    image_data = request.data['image']
    uploaded_file = decode_base64_image(image_data)
    
    # Save Original Image
    doc = ScannedDocument(image=uploaded_file)
    doc.save()
    
    # Process Image
    processed_img = process_image(doc.image.path)
    _, buffer = cv2.imencode('.png', processed_img)
    processed_img_base64 = base64.b64encode(buffer).decode()
    
    # Save Processed Image
    processed_file = ContentFile(base64.b64decode(processed_img_base64), name="processed.png")
    doc.processed_image.save("processed.png", processed_file)
    
    return Response({
        "processed_image": doc.processed_image.url
    })


