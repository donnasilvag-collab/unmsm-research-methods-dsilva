# Pipeline reproducible del estudio

**Problema de investigación:** Influencia de la gestión de riesgos de seguridad de la información en la eficacia del control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software en empresas peruanas: protocolo de un estudio de métodos mixtos.

## Finalidad de esta carpeta

Esta carpeta documenta el diseño reproducible del componente técnico del estudio. Aunque la investigación no plantea, por ahora, un modelo predictivo complejo, sí requiere un flujo ordenado para versionar datos, registrar transformaciones analíticas y dejar evidencia verificable de cada etapa del trabajo.

## Enfoque de reproducibilidad

- **Git** se utilizará para versionar documentos, instrumentos, scripts y decisiones metodológicas.
- **DVC** se reservará para versionar bases anonimizadas, matrices de variables, versiones de cuestionario y derivados tabulares que no conviene almacenar directamente en Git.
- **MLflow** se empleará como bitácora de ejecuciones analíticas, sobre todo para registrar variantes del procesamiento cuantitativo, supuestos de análisis y resultados comparables.

## Flujo previsto

1. Recolección o consolidación de datos anonimizados provenientes de encuesta, entrevistas y documentos institucionales autorizados.
2. Versionado del insumo tabular y sus transformaciones mediante DVC.
3. Limpieza, codificación y generación de variables analíticas.
4. Ejecución del análisis cuantitativo y registro de parámetros, salidas y métricas en MLflow.
5. Integración con hallazgos cualitativos y resguardo de evidencias trazables en el repositorio.

## Salidas esperadas

- Base de datos cuantitativa anonimizada.
- Diccionario de variables y criterios de codificación.
- Registro de corridas analíticas reproducibles.
- Evidencia de trazabilidad entre insumo, transformación, análisis y resultado.

## Estado actual

Esta carpeta se encuentra en fase de diseño documental. En la siguiente iteración del repositorio se incorporarán scripts, archivos `.dvc` y el detalle operativo necesario para ejecutar el pipeline completo.
