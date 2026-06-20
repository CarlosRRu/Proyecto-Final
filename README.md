# Sistema de Biofeedback para el Control del Estrés (ECG + EEG)

## Descripción

Este proyecto implementa un sistema de biofeedback para la detección del estado de relajación o estrés utilizando señales biomédicas de ECG y EEG.

El sistema adquiere ambas señales, aplica procesamiento digital, extrae características fisiológicas y presenta el resultado mediante una interfaz gráfica basada en un semáforo de relajación.

---

## Objetivo

Desarrollar una interfaz capaz de:

* Detectar picos R en ECG.
* Calcular métricas de HRV:

  * RMSSD
  * Relación LF/HF
* Extraer potencia Alfa del EEG (8–13 Hz).
* Clasificar el estado del usuario:

  * Verde → Relajado
  * Amarillo → Intermedio
  * Rojo → Estrés

---

## Integrantes del equipo

* Juan Carlos Argueta Hernández
* Dario Mariano Gomezpeña Cabrera
* Ian Shaiel Anell Rodriguez

---

## Estructura del repositorio

```text
Proyecto-Biofeedback-ECG-EEG/
│
├── Hardware/
│   ├── Fotosmontaje/
│   │   ├── BIOPAC_Funcionando.png
│   │   ├── Paciente_Dario.png
│   │   └── Paciente_Ximena.png
│   │
│   ├── Conexiones_Usuario-BIOPAC.png
│   └── ConfiguracionBIOPAC.pdf
│
├── Reporte/
│   ├── ArticuloIEEE.pdf
│   └── ArticuloIEEE.docx
│
├── Software/
│   ├── capturas/
│   │   ├── Estres.png
│   │   ├── Intermedio.png
│   │   └── Relajado.png
│   │
│   ├── datos/
│   │   ├── LankyCalibracion.acq
│   │   └── LankyRE.acq
│   │
│   ├── LunaSemaforofinal.py
│   └── requirements.txt
│
├── README.md
└── .gitignore
```

### Organización

* **Hardware:** diagramas, configuración del sistema y evidencia experimental.
* **Software:** código fuente, datos biomédicos y capturas del sistema.
* **Reporte:** artículo científico IEEE y versión editable.
* **README:** guía rápida de instalación y ejecución.

```
```


---

## Hardware utilizado

* Sistema BIOPAC (o dispositivo utilizado)
* Electrodos ECG
* Electrodos EEG
* Computadora para procesamiento

---

## Requisitos de software

Python 3.11+

Instalar librerías:

pip install bioread numpy scipy pyqtgraph PyQt5

---

## Archivos necesarios

Colocar en la misma carpeta:

LankyCalibracion.acq
LankyRE.acq
LunaSemaforofinal.py

---

## Ejecución

Entrar a la carpeta Software:

python LunaSemaforofinal.py

---

## Procesamiento implementado

### ECG

1. Filtrado 5–25 Hz
2. Detección de picos R
3. Cálculo RMSSD
4. Cálculo LF/HF

### EEG

1. Filtrado 1–40 Hz
2. Extracción banda Alfa
3. Cálculo PSD con Welch

---

## Interfaz gráfica

La GUI muestra:

* Señal ECG
* Señal EEG
* BPM
* RMSSD
* LF
* HF
* LF/HF
* Potencia Alfa
* Estado del semáforo

<img width="1919" height="1030" alt="Relajado" src="https://github.com/user-attachments/assets/259e325c-71e2-4444-af4b-c098810ba24f" />



<img width="1919" height="1026" alt="Intermedio" src="https://github.com/user-attachments/assets/8adbbe88-493a-4a87-be31-aeddc63a9647" />



<img width="1919" height="1031" alt="Estres" src="https://github.com/user-attachments/assets/063700df-677e-44bf-858f-7dd14e6dfe97" />



---

## Resultados esperados

Estado relajado:

* ↑ Potencia Alfa
* ↓ LF/HF

Estado de estrés:

* ↓ Potencia Alfa
* ↓ RMSSD
* ↑ LF/HF

---

## Problemas comunes

### Error:
ModuleNotFoundError

Solución:
pip install nombre_libreria

### Error:

FileNotFoundError

Ejemplo:

FileNotFoundError: [Errno 2] No such file or directory:
'LankyCalibracion.acq'

### Causa:

El programa no encuentra el archivo porque:

* El archivo `.acq` no está en la carpeta correcta.
* El nombre del archivo es distinto.
* Se está ejecutando el script desde otra ubicación.

### Solución:

Verificar que los archivos estén dentro de la carpeta del proyecto:

Software/
├── LunaSemaforofinal.py
├── LankyCalibracion.acq
└── LankyRE.acq

Después ejecutar:

python LunaSemaforofinal.py

Si los archivos están en otra carpeta, modificar la ruta dentro del código:

data = bioread.read_file("ruta/al/archivo/LankyRE.acq")

---

### Error:

ModuleNotFoundError

Ejemplo:

ModuleNotFoundError: No module named 'bioread'

### Solución:

Instalar la librería faltante:

pip install bioread

---

### Error:

La interfaz abre pero no aparecen gráficas

### Solución:

Verificar que:

* Los archivos `.acq` contengan datos.
* El orden de canales sea:

  * Canal 0 → EEG
  * Canal 1 → ECG
* La frecuencia de muestreo coincida con FS = 1000.


---

## Referencias

## Referencias

[1] Porras-Álvarez, J., y Bernal-Calderón, M. O., “Variabilidad de la frecuencia cardiaca: evaluación del entrenamiento deportivo. Revisión de tema”, Revista Duazary, vol. 16, núm. 2, 2019.

[2] Gallo Villegas, J. A., Farbiarz Farbiarz, J., y Álvarez Montoya, D. L., “Análisis espectral de la variabilidad de la frecuencia cardíaca”, Revista Iatreia, 1999.

[3] Rodas, G., Pedret, C., Ramos, J., y Capdevila, L., “Variabilidad de la frecuencia cardíaca: concepto, medidas y relación con aspectos clínicos (I)”, Archivos de Medicina del Deporte, 2008.

[4] Medina Bañuelos, V., Azpiroz Leehan, J., y Saldívar Salazar, E., “Análisis espectral del electroencefalograma”, Revista Mexicana de Ingeniería Biomédica.

[5] Muravchik, C. H., Fernández Corazza, M., y Collavini, S., “Procesamiento de Señales: Para los problemas directo e inverso en electro- y magneto-encefalografía”, en La bioingeniería en la Argentina, Academia Nacional de Ciencias Exactas, Físicas y Naturales, 2018.

[6] [SciPy Documentation](https://docs.scipy.org/?utm_source=chatgpt.com)

[7] [PyQtGraph Documentation](https://pyqtgraph.readthedocs.io/?utm_source=chatgpt.com)
