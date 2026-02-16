# README - chat.py

## 💬 Aplicación de Chat en Tiempo Real con Flet

### Descripción General
Una aplicación de chat interactiva multi-usuario que utiliza el sistema de **pub/sub** (publicación/suscripción) de Flet para comunicación en tiempo real. Los usuarios pueden unirse con un nombre personalizado y enviar mensajes visibles para todos.

---

## 🎯 Características Principales
- ✅ Chat en tiempo real entre múltiples usuarios
- ✅ Sistema de pub/sub para sincronización
- ✅ Mensajes de sistema (notificaciones de entrada)
- ✅ Interfaz limpia con TextField y botones
- ✅ Validación de nombre de usuario
- ✅ Diálogo modal de bienvenida

---

## 📋 Explicación del Código Parte por Parte

### 1. **Importaciones**
```python
from dataclasses import dataclass
import flet as ft
```
- `dataclasses`: Simplifica la creación de clases para estructuras de datos
- `flet`: Framework para la interfaz gráfica

---

### 2. **Clase Message (Dataclass)**
```python
@dataclass
class Message:
    user: str
    text: str
    message_type: str
```

**¿Qué es una dataclass?**
- Genera automáticamente métodos como `__init__`, `__repr__`, `__eq__`
- Evita código repetitivo

**Atributos:**
- `user`: Nombre del usuario que envía el mensaje
- `text`: Contenido del mensaje
- `message_type`: Tipo de mensaje
  - `"chat_message"`: Mensaje normal de usuario
  - `"login_message"`: Notificación de entrada al chat

**Ejemplo de uso:**
```python
msg = Message(user="Juan", text="Hola!", message_type="chat_message")
# Equivalente a:
# msg.user = "Juan"
# msg.text = "Hola!"
# msg.message_type = "chat_message"
```

---

### 3. **Función Principal `main(page: ft.Page)`**

#### **Variables Globales de UI**
```python
chat = ft.Column()
new_message = ft.TextField()
```
- `chat`: Columna que contendrá todos los mensajes
- `new_message`: Campo de texto donde el usuario escribe mensajes

---

### 4. **Función `on_message(message: Message)`**
```python
def on_message(message: Message):
    if message.message_type == "chat_message":
        chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
    elif message.message_type == "login_message":
        chat.controls.append(
            ft.Text(message.text, italic=True, color=ft.Colors.BLACK_45, size=12)
        )
    page.update()
```

**Propósito:** Manejador que recibe mensajes del sistema pub/sub.

**Flujo de ejecución:**

1. **Si es `chat_message` (mensaje normal):**
   ```python
   chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
   ```
   - Agrega un texto en formato: `"Usuario: Mensaje"`
   - **Ejemplo:** `"María: ¿Cómo están?"`

2. **Si es `login_message` (notificación de entrada):**
   ```python
   ft.Text(message.text, italic=True, color=ft.Colors.BLACK_45, size=12)
   ```
   - Texto en cursiva, gris, tamaño 12
   - **Ejemplo:** `"Carlos has joined the chat."`

3. **`page.update()`**: Refresca la UI para mostrar el nuevo mensaje

---

### 5. **Suscripción al Sistema Pub/Sub**
```python
page.pubsub.subscribe(on_message)
```

**¿Qué hace?**
- Registra la función `on_message` como "escuchador"
- Cualquier mensaje publicado con `send_all()` será recibido aquí
- Permite comunicación entre múltiples instancias de la aplicación

**Analogía:** 
- Es como suscribirse a un canal de YouTube
- Cada vez que se publica contenido, todos los suscriptores lo reciben

---

### 6. **Función `send_click(e)`**
```python
def send_click(e):
    page.pubsub.send_all(
        Message(
            user=page.session.store.get("user_name"),
            text=new_message.value,
            message_type="chat_message",
        )
    )
    new_message.value = ""
```

**Flujo paso a paso:**

1. **Obtener nombre de usuario:**
   ```python
   user=page.session.store.get("user_name")
   ```
   - Recupera el nombre almacenado en la sesión
   - `session.store` es un diccionario persistente por sesión

2. **Crear mensaje:**
   ```python
   Message(
       user="Juan",
       text="Hola a todos",
       message_type="chat_message"
   )
   ```

3. **Publicar mensaje:**
   ```python
   page.pubsub.send_all(...)
   ```
   - Envía el mensaje a **todos los suscriptores**
   - Incluye la instancia actual (se ve a sí mismo)

4. **Limpiar campo de texto:**
   ```python
   new_message.value = ""
   ```
   - Borra el contenido del TextField para un nuevo mensaje

---

### 7. **Campo de Nombre de Usuario**
```python
user_name = ft.TextField(label="Enter your name")
```
- TextField con etiqueta "Enter your name"
- Se usa en el diálogo de bienvenida

---

### 8. **Función `join_click(e)`**
```python
def join_click(e):
    if not user_name.value:
        user_name.error_text = "Name cannot be blank!"
    else:
        page.session.store.set("user_name", user_name.value)
        page.pop_dialog()
        page.pubsub.send_all(
            Message(
                user=user_name.value,
                text=f"{user_name.value} has joined the chat.",
                message_type="login_message",
            )
        )
```

**Flujo detallado:**

#### **1. Validación del nombre:**
```python
if not user_name.value:
    user_name.error_text = "Name cannot be blank!"
```
- Si el campo está vacío, muestra mensaje de error en rojo
- **No cierra el diálogo** hasta que ingrese un nombre válido

#### **2. Guardar nombre en sesión:**
```python
page.session.store.set("user_name", user_name.value)
```
- Almacena el nombre para uso posterior
- Accesible con `page.session.store.get("user_name")`

#### **3. Cerrar diálogo:**
```python
page.pop_dialog()
```
- Cierra el diálogo de bienvenida
- Muestra la interfaz principal del chat

#### **4. Notificar entrada al chat:**
```python
page.pubsub.send_all(
    Message(
        user=user_name.value,
        text=f"{user_name.value} has joined the chat.",
        message_type="login_message",
    )
)
```
- Envía mensaje de sistema a todos
- **Ejemplo:** `"Ana has joined the chat."`
- Se mostrará en cursiva y gris

---

### 9. **Diálogo de Bienvenida**
```python
page.show_dialog(
    ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column([user_name], tight=True),
        actions=[ft.Button(content="Join chat", on_click=join_click)],
        actions_alignment=ft.MainAxisAlignment.END,
    )
)
```

**Propiedades del AlertDialog:**

- `open=True`: Se muestra inmediatamente al iniciar la app
- `modal=True`: No se puede interactuar con el fondo hasta cerrarlo
- `title`: Título "Welcome!"
- `content`: Contiene el TextField del nombre
- `actions`: Lista de botones (solo "Join chat")
- `actions_alignment=END`: Alinea el botón a la derecha

**Visualización:**
```
┌─────────────────────────────┐
│         Welcome!           │
├─────────────────────────────┤
│                             │
│  ┌──────────────────────┐  │
│  │ Enter your name      │  │
│  └──────────────────────┘  │
│                             │
├─────────────────────────────┤
│               [Join chat]   │
└─────────────────────────────┘
```

---

### 10. **Construcción de la Interfaz Principal**
```python
page.add(chat, ft.Row([new_message, ft.Button("Send", on_click=send_click)]))
```

**Estructura:**
1. `chat`: Columna con todos los mensajes (se va llenando dinámicamente)
2. `Row`: Fila horizontal con:
   - `new_message`: TextField para escribir
   - `Button`: Botón "Send" con evento `send_click`

**Layout visual:**
```
┌─────────────────────────────┐
│ Juan: Hola!                 │
│ María: ¿Cómo están?         │
│ Carlos has joined the chat. │  ← Mensajes en chat (Column)
│ Carlos: ¡Hola a todos!      │
│                             │
├─────────────────────────────┤
│ ┌──────────────┐  [Send]   │  ← Input + Botón (Row)
│ │ Type here... │            │
│ └──────────────┘            │
└─────────────────────────────┘
```

---

### 11. **Ejecución de la Aplicación**
```python
#ft.run(main)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```

**Dos formas de ejecutar:**
- `ft.run(main)`: Abre como aplicación de escritorio
- `ft.app(target=main, view=ft.AppView.WEB_BROWSER)`: **Abre en navegador web** ← Activo

**Ventajas del modo WEB_BROWSER:**
- Más fácil para probar multi-usuario (múltiples pestañas)
- No requiere instalación de aplicación
- Accesible desde cualquier dispositivo en red local

---

## 🔄 Flujo Completo de Uso

### **Escenario: Dos usuarios se conectan**

#### **Usuario 1 (Ana):**
```
1. Aplicación inicia → Diálogo "Welcome!"
2. Ingresa "Ana" → Clic en "Join chat"
3. Sistema envía: "Ana has joined the chat." [gris, cursiva]
4. Escribe "Hola!" → Clic en "Send"
5. Sistema envía: Message(user="Ana", text="Hola!", type="chat_message")
6. Se muestra: "Ana: Hola!"
```

#### **Usuario 2 (Carlos):**
```
1. Aplicación inicia → Diálogo "Welcome!"
2. Ve en chat: "Ana has joined the chat."
3. Ingresa "Carlos" → Clic en "Join chat"
4. Sistema envía: "Carlos has joined the chat."
5. Ana ve: "Carlos has joined the chat."
6. Carlos escribe "Hola Ana!" → Send
7. Ambos ven: "Carlos: Hola Ana!"
```

---

## 🧠 Conceptos Clave

### 1. **Sistema Pub/Sub (Publicación/Suscripción)**
```python
page.pubsub.subscribe(on_message)    # Suscribirse a mensajes
page.pubsub.send_all(message)        # Publicar mensaje a todos
```
- **Patrón de diseño** para comunicación asíncrona
- Un emisor → Múltiples receptores
- Desacopla emisor de receptores

### 2. **Session Store**
```python
page.session.store.set("user_name", "Juan")
page.session.store.get("user_name")  # → "Juan"
```
- Almacenamiento persistente por sesión
- Similar a diccionario: clave → valor
- Sobrevive a actualizaciones de página

### 3. **Dataclasses**
```python
@dataclass
class Message:
    user: str
    text: str
```
- Sintaxis simplificada para clases de datos
- Genera automáticamente métodos especiales
- Código más limpio y legible

### 4. **Diálogos Modales**
```python
page.show_dialog(ft.AlertDialog(...))
page.pop_dialog()  # Cerrar
```
- Bloquea interacción con fondo
- Perfecto para formularios obligatorios
- `modal=True` → No se puede cerrar clickeando fuera

---

## 🎨 Estilos de Mensajes

| Tipo | Formato | Color | Tamaño | Cursiva |
|------|---------|-------|--------|---------|
| **Chat** | `Usuario: Mensaje` | Negro (default) | Normal | ❌ No |
| **Sistema** | `"Usuario has joined"` | Gris (`BLACK_45`) | 12 | ✅ Sí |

---

## 🚀 Cómo Ejecutar

### **Opción 1: Modo Escritorio**
```python
ft.run(main)
```
```bash
python chat.py
```

### **Opción 2: Modo Navegador (actual)**
```python
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```
```bash
python chat.py
```
- Se abre en el navegador predeterminado
- Para probar multi-usuario: abrir múltiples pestañas

---

## 📦 Dependencias
```bash
pip install flet
```

---

## 🔧 Mejoras Sugeridas

### **1. Agregar timestamps:**
```python
from datetime import datetime

@dataclass
class Message:
    user: str
    text: str
    message_type: str
    timestamp: str = datetime.now().strftime("%H:%M")

# Mostrar:
ft.Text(f"[{message.timestamp}] {message.user}: {message.text}")
```

### **2. Colores por usuario:**
```python
COLORS = ["blue", "green", "purple", "orange"]
user_color = COLORS[hash(message.user) % len(COLORS)]
ft.Text(message.user, color=user_color)
```

### **3. Scroll automático:**
```python
chat = ft.Column(scroll=ft.ScrollMode.AUTO)
# En on_message():
page.update()
chat.scroll_to(offset=-1, duration=300)  # Ir al final
```

### **4. Salir del chat:**
```python
def leave_click(e):
    user = page.session.store.get("user_name")
    page.pubsub.send_all(
        Message(user=user, text=f"{user} left the chat.", 
                message_type="login_message")
    )
    page.window_close()
```

### **5. Lista de usuarios conectados:**
```python
active_users = set()

# En join_click:
active_users.add(user_name.value)
page.pubsub.send_all({"type": "user_list", "users": list(active_users)})
```

---

## 💡 Casos de Uso
- Chat de equipo en tiempo real
- Sistema de notificaciones
- Juegos multijugador (lobby de chat)
- Soporte técnico en vivo
- Colaboración en aplicaciones

---

## 🎓 Diferencias con Otras Apps

| Característica | chat.py | calc_app.py | counter.py |
|----------------|---------|-------------|------------|
| **Comunicación** | Multi-usuario | Solo local | Solo local |
| **Pub/Sub** | ✅ Sí | ❌ No | ❌ No |
| **Diálogos** | ✅ Modal | ❌ No | ❌ No |
| **Persistencia** | Session Store | Variables | Variables |
| **Complejidad** | Alta | Media | Baja |

---

## 🌐 Arquitectura del Sistema

```
┌─────────────┐          ┌──────────────┐          ┌─────────────┐
│  Usuario 1  │          │   Servidor   │          │  Usuario 2  │
│             │          │   Flet       │          │             │
│  ┌───────┐  │          │  ┌────────┐  │          │  ┌───────┐  │
│  │ send  │──┼─────────→│  │pub/sub │──┼─────────→│  │receive│  │
│  └───────┘  │          │  └────────┘  │          │  └───────┘  │
│  ┌───────┐  │          │               │          │  ┌───────┐  │
│  │receive│←─┼──────────┤               │←─────────┼──│ send  │  │
│  └───────┘  │          │               │          │  └───────┘  │
└─────────────┘          └───────────────┘          └─────────────┘
```

**Flujo:**
1. Usuario 1 envía mensaje → `send_all()`
2. Servidor pub/sub distribuye a todos los suscriptores
3. Usuario 2 recibe en `on_message()` → actualiza UI

---

## ✅ Buenas Prácticas Aplicadas

1. ✅ **Dataclasses** para estructuras de datos limpias
2. ✅ **Validación de entrada** (nombre no vacío)
3. ✅ **Separación de tipos de mensajes** (chat vs sistema)
4. ✅ **Manejo de sesiones** con `session.store`
5. ✅ **UI responsive** con actualizaciones en tiempo real
6. ✅ **Feedback visual** (mensajes de error, estilos diferenciados)

---

Este chat es un excelente ejemplo de aplicaciones en tiempo real con Flet. ¡Ideal para aprender patrones de comunicación multi-usuario! 🚀
