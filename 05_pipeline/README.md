# Pipeline reproducible del estudio

**Problema de investigación:** Influencia de la gestión de riesgos de seguridad de la información en la eficacia del control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software en empresas peruanas: protocolo de un estudio de métodos mixtos.

## Finalidad de esta carpeta

Esta carpeta presenta el entregable técnico-documental del paso 5 del curso. Su función no es alojar todavía datos reales ni scripts definitivos, sino dejar especificado de manera clara cómo se organizará el flujo reproducible del estudio cuando se incorporen insumos autorizados y anonimizados.

## Alcance de esta entrega

En esta etapa, el componente reproducible queda resuelto a nivel de diseño y trazabilidad. Por ello, la carpeta incluye:

- una descripción explícita del flujo de trabajo reproducible;
- un inventario mínimo de artefactos esperados;
- una lista de verificación para asegurar consistencia entre datos, análisis y resultados;
- criterios de uso de Git, DVC y MLflow coherentes con la naturaleza sensible del estudio.

## Enfoque de reproducibilidad

- **Git** se utilizará para versionar documentos, instrumentos, scripts y decisiones metodológicas.
- **DVC** se reservará para versionar bases anonimizadas, matrices de variables, versiones de cuestionario y derivados tabulares que no conviene almacenar directamente en Git.
- **MLflow** se empleará como bitácora de ejecuciones analíticas, sobre todo para registrar variantes del procesamiento cuantitativo, supuestos de análisis y resultados comparables.

## Flujo de trabajo reproducible

1. Recolección o consolidación de datos anonimizados provenientes de encuesta, entrevistas y documentos institucionales autorizados.
2. Versionado del insumo tabular y sus transformaciones mediante DVC.
3. Limpieza, codificación y generación de variables analíticas.
4. Ejecución del análisis cuantitativo y registro de parámetros, salidas y métricas en MLflow.
5. Integración con hallazgos cualitativos y resguardo de evidencias trazables en el repositorio.

## Artefactos mínimos del pipeline

- `README.md`: explica el propósito de la carpeta y el flujo general.
- `artifact_manifest.md`: define qué archivos o productos deberán existir cuando el pipeline se ejecute con insumos reales.
- `reproducibility_checklist.md`: resume los controles mínimos para mantener trazabilidad y consistencia.

## Salidas esperadas

- Base de datos cuantitativa anonimizada.
- Diccionario de variables y criterios de codificación.
- Registro de corridas analíticas reproducibles.
- Evidencia de trazabilidad entre insumo, transformación, análisis y resultado.

## Estado actual

El pipeline queda documentado como un diseño reproducible preliminar, suficiente para esta fase del curso. No se incorporan todavía datos reales, scripts ejecutables ni archivos `.dvc` porque el estudio aún no ha ingresado a trabajo de campo ni a procesamiento empírico; sin embargo, la estructura, el criterio de versionado y la lógica de trazabilidad ya están definidos.
