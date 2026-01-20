# Fuzzy Mamdani - Sistema de Inferencia Difusa

Sistema de control difuso implementado en Python basado en el **Método de Mamdani**. Este motor está diseñado para ajustar automáticamente la velocidad de un ventilador considerando múltiples factores ambientales y de contexto.

## Variables del Sistema
El sistema toma decisiones basadas en cuatro entradas dinámicas:
* **Temperatura** (`temperature`)
* **Humedad** (`humidity`)
* **Ocupación** (`occupancy` - número de personas)
* **Hora del día** (`time_of_day`)

---

## Estructura del Proyecto

El proyecto sigue una arquitectura modular y desacoplada para facilitar su mantenimiento:

```text
fuzzy_mamdani/
├── main.py              # Punto de entrada y ejemplo de uso
├── data/
│   ├── variables.json   # Definición de conjuntos y funciones de pertenencia
│   └── rules.json       # Base de reglas (IF-THEN)
└── fuzzy/
    ├── membership.py    # Funciones matemáticas (Triangular, Trapezoidal, etc.)
    ├── variable.py      # Estructuras para variables lingüísticas
    ├── rule.py          # Lógica de las reglas difusas
    ├── data_loader.py   # Parser de archivos JSON
    ├── fuzzifier.py     # Paso 1: Fuzzificación
    ├── inference.py     # Paso 2: Motor de Inferencia (Mamdani)
    ├── defuzzifier.py   # Paso 3: Desfuzzificación (Método del Centroide)
    └── engine.py        # Orquestador central del sistema
```

## Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/CristianDC-Junkier/Fuzzy-Mamdami.git
   cd fuzzy_mamdani
   ```

2. Requisitos:
  * Python 3.x instalado.
  * Este motor está desarrollado exclusivamente con la librería estándar, por lo que no requiere instalar dependencias adicionales vía pip.

3. Ejecución del ejemplo:
  ```bash
  python main.py
  ```

## Base de Conocimiento

El sistema es altamente flexible gracias a que la lógica de negocio reside en la carpeta data/:
  * variables.json: Define los rangos (universo de discurso) y los términos lingüísticos (ej. cold, warm, hot) mediante parámetros geométricos.
  * rules.json: Contiene la lógica condicional. Al estar en JSON, puedes ajustar el comportamiento del ventilador sin necesidad de modificar el código Python.

## Componentes del Sistema

El flujo de trabajo sigue las etapas clásicas de la computación blanda:
  * fuzzifier.py: Transforma las entradas reales (ej. 25.5°C) en valores difusos usando las funciones en membership.py.
  * inference.py: Evalúa las reglas y aplica el operador MIN (o producto) para la implicación de Mamdani.
  * defuzzifier.py: Ejecuta el método del Centroide para obtener un valor nítido de salida (ej. 65% de potencia).
  * engine.py: Actúa como el cerebro que coordina la comunicación entre todos los módulos.

## Ejemplo de Comportamiento

El sistema está configurado para responder de forma inteligente a contextos complejos:
  * Eficiencia Térmica: A mayor temperatura y ocupación, mayor velocidad.
  * Confort por Humedad: Si la humedad es extrema (muy baja o muy alta), el sistema prioriza una ventilación más activa.
  * Sensibilidad Temporal: Durante la Noche, el sistema suaviza las potencias para reducir el ruido, mientras que por la Mañana/Tarde permite el máximo rendimiento.

## Licencia
Este proyecto se distribuye bajo la licencia MIT, permitiendo su uso libre para fines académicos, personales o comerciales.
    
