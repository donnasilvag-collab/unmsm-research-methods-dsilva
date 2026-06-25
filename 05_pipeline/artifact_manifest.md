# Inventario mínimo de artefactos del pipeline

## Propósito

Este documento define los artefactos mínimos que deberá contener el pipeline reproducible cuando el estudio avance de la fase documental a la fase de ejecución analítica.

## Artefactos previstos

| Artefacto | Finalidad | Herramienta principal | Estado en esta entrega |
| --- | --- | --- | --- |
| Base cuantitativa anonimizada | Reunir respuestas estructuradas para el análisis cuantitativo | DVC | Definido |
| Diccionario de variables | Precisar nombre, tipo, escala y significado de cada variable | Git | Definido |
| Registro de transformaciones | Dejar rastro de limpieza, codificación y cambios sobre los datos | Git + DVC | Definido |
| Corridas analíticas | Registrar parámetros, supuestos y salidas del análisis cuantitativo | MLflow | Definido |
| Evidencia de integración | Relacionar resultados cuantitativos con hallazgos cualitativos y decisiones interpretativas | Git | Definido |

## Convenciones mínimas

- Los datos identificables no se almacenarán en el repositorio.
- Todo artefacto analítico deberá tener fecha, versión y breve descripción.
- Las transformaciones relevantes deberán poder rastrearse desde el insumo hasta el resultado reportado.
