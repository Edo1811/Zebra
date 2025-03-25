import cv2
import time

# Inizializza la cattura video da una webcam (0 indica la webcam predefinita)
cap = cv2.VideoCapture(0)

# Imposta le dimensioni del frame e il codec video per l'output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter(r'C:\Users\Edoardo\Desktop\Zebra OPSYS python\output.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (frame_width, frame_height))

# Inizializza un oggetto per calcolare il tempo trascorso
start_time = time.time()
frame_count = 0

while True:
    # Legge il frame dalla cattura video
    ret, frame = cap.read()
    if not ret:
        break

    # Incrementa il contatore di frame
    frame_count += 1

    # Calcola il tempo trascorso
    elapsed_time = time.time() - start_time

    # Calcola il frame rate
    fps = frame_count / elapsed_time

    # Mostra il frame rate sul frame
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Scrivi il frame nel video di output
    out.write(frame)

    # Mostra il frame
    cv2.imshow('FPS Counter', frame)

    # Esci se viene premuto il tasto 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilascia la cattura video, il video di output e chiudi le finestre
cap.release()
out.release()
cv2.destroyAllWindows()
