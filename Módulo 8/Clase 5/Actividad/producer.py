from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

# Configurar productor Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Función para simular eventos de usuario
def simulate_user_activity():
    actions = [
        {"user_id": 1, "action": "viewed_product", "product_id": 101, "product_name": "Laptop Gaming"},
        {"user_id": 2, "action": "added_to_cart", "product_id": 102, "product_name": "Mouse Inalámbrico"},
        {"user_id": 3, "action": "purchased_product", "product_id": 103, "product_name": "Teclado Mecánico"},
        {"user_id": 1, "action": "viewed_product", "product_id": 104, "product_name": "Monitor 4K"},
        {"user_id": 4, "action": "added_to_cart", "product_id": 105, "product_name": "Auriculares Gaming"},
        {"user_id": 2, "action": "purchased_product", "product_id": 102, "product_name": "Mouse Inalámbrico"},
        {"user_id": 5, "action": "viewed_product", "product_id": 106, "product_name": "Silla Gaming"},
        {"user_id": 3, "action": "added_to_cart", "product_id": 107, "product_name": "Webcam HD"},
        {"user_id": 4, "action": "viewed_product", "product_id": 108, "product_name": "Micrófono USB"},
        {"user_id": 5, "action": "purchased_product", "product_id": 109, "product_name": "Mousepad XXL"}
    ]
    
    try:
        while True:
            # Seleccionar un evento aleatorio
            event = random.choice(actions)
            
            # Agregar timestamp
            event["timestamp"] = datetime.now().isoformat()
            
            # Enviar evento al tema 'user-activity'
            producer.send('user-activity', value=event)
            
            print(f"Evento enviado: {event}")
            
            # Esperar entre 1-3 segundos antes del siguiente evento
            time.sleep(random.uniform(1, 3))
            
    except KeyboardInterrupt:
        print("\nDeteniendo el productor...")
    finally:
        # Asegurar que todos los mensajes se envíen antes de cerrar
        producer.flush()
        producer.close()
        print("Productor cerrado correctamente.")

if __name__ == "__main__":
    print("Iniciando simulación de eventos de usuario...")
    print("Presiona Ctrl+C para detener")
    simulate_user_activity()