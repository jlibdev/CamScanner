from django.shortcuts import render
import cv2
from django.http import StreamingHttpResponse, JsonResponse

cap = None  # Global variable for the camera

def generate_frames():
    """Generate frames from the webcam."""
    global cap
    while True:
        if cap is None or not cap.isOpened():
            break  # Stop the loop if the camera is closed
        
        success, frame = cap.read()
        if not success:
            break
        
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


def video_feed(request):
    global cap
    if cap is None or not cap.isOpened():
        return JsonResponse({"error": "Camera is not started"}, status=503)
    try:
        return StreamingHttpResponse(generate_frames(), content_type="multipart/x-mixed-replace; boundary=frame")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def start_camera(request):
    """Start the camera."""
    global cap
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if cap.isOpened():
            return JsonResponse({"status": "Success"})
        else:
            cap = None 
            return JsonResponse({"status": "Error"})

    return JsonResponse({"status": "Already running"})

def stop_camera(request):
    global cap
    if cap is not None and cap.isOpened():
        cap.release()
        cap = None  # Reset variable
        cv2.destroyAllWindows()  # Ensure resources are released
    return JsonResponse({"status": "Success"})
