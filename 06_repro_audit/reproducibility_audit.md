# Auditoría preliminar de reproducibilidad

## Alcance

Esta auditoría preliminar evalúa si el repositorio ofrece condiciones mínimas para reproducir el estudio sobre la influencia de la gestión de riesgos de seguridad de la información en el control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software en empresas peruanas.

## Revisión inicial

| Componente | Estado actual | Observación |
| --- | --- | --- |
| Estructura del repositorio | Cumplido | La organización por carpetas numeradas facilita el seguimiento del curso y la trazabilidad del avance. |
| Formulación del problema | Cumplido | El problema y su redacción ya están unificados en los documentos principales. |
| Protocolo metodológico | Parcial | Existe una versión desarrollada del protocolo, pero todavía falta migrar sus decisiones a un flujo técnico ejecutable. |
| Revisión de literatura | Cumplido | Se cuenta con revisión sistemática preliminar, vacíos y flujo PRISMA inicial. |
| Pipeline técnico | Parcial | La carpeta técnica ya tiene lineamientos, pero aún no incluye scripts, datos versionados ni corridas registradas. |
| Gestión de datos | Parcial | El plan existe a nivel documental, pendiente de aterrizar a archivos y convenciones operativas. |

## Riesgos para la reproducibilidad

- Dependencia excesiva de futuras decisiones manuales si no se documentan pronto los instrumentos y transformaciones.
- Posible heterogeneidad entre fuentes cuantitativas y cualitativas si no se define una convención única de nombres, versiones y metadatos.
- Riesgo de pérdida de trazabilidad si los insumos anonimizados no se separan desde el inicio entre datos brutos, procesados y derivados.

## Acciones recomendadas

1. Incorporar un diccionario de variables y una plantilla de metadatos para la base cuantitativa.
2. Definir nomenclatura estándar para versiones de instrumentos, matrices y salidas analíticas.
3. Añadir, en la siguiente iteración, archivos de control para DVC y una bitácora básica en MLflow.
