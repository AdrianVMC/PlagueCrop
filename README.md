PlagueCrop

PlagueCrop es un simulador visual e interactivo de propagación de plagas en cultivos basado en autómatas celulares, desarrollado en Python con Tkinter.

Descripción General

El sistema modela el comportamiento de distintas plagas en un campo de cultivo segmentado en celdas. Cada celda representa una unidad agrícola con propiedades como tipo de cultivo, humedad, etapa de crecimiento, entre otras. Las plagas se propagan entre las celdas de acuerdo con reglas predefinidas y parámetros seleccionados por el usuario.

Flujo del Sistema

1. Inicio y Configuración

El usuario accede a una vista principal (MainView) y de ahí pasa a SettingsView, donde define:

Tipo de cultivo

Tipo de plaga

Etapa fenológica del cultivo

Humedad

Intensidad solar

Nivel de pesticidas

Densidad de ocupación

Densidad de infestación inicial

Capacidad de propagación

Tamaño de la cuadrícula (filas y columnas)

Número de pasos de simulación ("steps")

2. Simulación

Se genera el autómata CellAutomaton con base en los parámetros.

Se infesta una porción inicial de celdas (actualmente de forma aleatoria).

Cada paso de simulación ejecuta una actualización del estado de cada celda, aplicando reglas sobre la propagación de la plaga y el daño causado.

La evolución se visualiza en GridView, usando colores para reflejar el estado de cada celda.

3. Finalización

Al terminar los pasos, el usuario puede:

Ver el estado final.

Reiniciar la simulación.

Volver a la configuración inicial.

Pendientes por Implementar

Distribución Gaussiana de infestación inicial

Mejorar la dispersión de focos de infección para simular brotes más realistas.

Propagación probabilística

Aplicar probabilidades a la propagación, influenciadas por el tipo de cultivo, plaga y condiciones.

Cooldown entre infestaciones

Agregar periodos de espera para evitar infección continua desde la misma celda.

Separación de grid de plaga y daño

Dividir la visualización entre la plaga activa y el daño agronómico acumulado.

Niveles de daño progresivo

Incluir transiciones como: saludable → dañado leve → dañado grave → destruido.

Modelo SIR (Susceptible - Infectado - Resistente)

Implementar un modelo epidemiológico:

S: Celda susceptible

I: Celda infectada

R: Celda recuperada o inmune

Definir tasas de transmisión y recuperación.

Tipado fino de plagas

Asignar comportamientos específicos a cada tipo de plaga (velocidad, agresividad, respuesta a pesticidas).

Resultados estadísticos y exportación

Generar resumen numérico de la simulación.

Exportar resultados en formato PDF (opcional).

Tecnologías Utilizadas

Python 3.13+

Tkinter

Arquitectura modular basada en vistas (main_view, settings_view, simulation_view)

Modelo de simulación basado en autómatas celulares