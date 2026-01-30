**CesarPy** es una herramienta de criptografía clásica que implementa el algoritmo de sustitución de Julio César. Este proyecto se enfoca en la **programación modular** y la **aritmética modular** para transformar texto manteniendo la integridad de los caracteres no alfabéticos.

---

## 🛡️ Características Principales

* **Arquitectura Modular:** Lógica de procesamiento centralizada en una única función para encriptación y desencriptación (DRY Principle).
* **Aritmética Modular:** Uso del operador `% 26` para garantizar que el desplazamiento de caracteres se mantenga dentro del rango del alfabeto (A-Z) de forma circular.
* **Preservación de Formato:** Mantiene mayúsculas, minúsculas, números, espacios y símbolos especiales sin alterarlos.
* **Módulo de Criptoanálisis:** Incluye una función de **Fuerza Bruta** que itera sobre todo el espacio de claves (25 rotaciones) para recuperar mensajes sin conocer el salto original.

---

## 📊 Fundamento Matemático

El cifrado funciona desplazando cada letra $x$ un número $n$ de posiciones:

$$E_n(x) = (x + n) \pmod{26}$$

Para descifrar, aplicamos la operación inversa:

$$D_n(x) = (x - n) \pmod{26}$$



---

## 🛠️ Instalación y Uso

1.  **Clonar el repositorio:**

2.  **Ejecutar la herramienta:**
    ```
    python caesar.py
    ```
---

## 📖 Menú de Funciones

1.  **Encriptar:** Solicita un texto y un número de saltos (shift).
2.  **Desencriptar:** Recupera el texto plano introduciendo el salto conocido.
3.  **Fuerza Bruta:** Útil cuando se intercepta un mensaje pero se desconoce la clave. Despliega todas las variantes posibles en una tabla alineada.

---

© 2026 Desarrollado por **[PedroPena]** - Uso Educativo.
