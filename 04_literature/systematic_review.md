# Revisión sistemática preliminar de literatura

## 4.1. Pregunta de revisión

La pregunta que guía esta revisión sistemática preliminar es la siguiente:

**¿Qué evidencia reciente y pertinente permite comprender la influencia de la gestión de riesgos de seguridad de la información en la eficacia del control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software, con especial interés en empresas peruanas?**

Esta formulación permite concentrar la revisión en cuatro dimensiones directamente vinculadas con el problema de investigación: **gestión de riesgos**, **control de acceso**, **protección del código y de los artefactos de desarrollo**, y **trazabilidad del desarrollo de software**.

## 4.2. Estrategia de búsqueda

| Campo | Valor |
| --- | --- |
| **Base principal** | Semantic Scholar |
| **Apoyo complementario** | Revisión manual de referencias citadas y corpus documental previamente reunido |
| **Fecha de búsqueda semilla** | 25 de junio de 2026 |
| **Periodo cubierto** | 2006-2025 |
| **Idiomas** | Inglés y español |
| **Tipo de documento priorizado** | Artículos arbitrados de revista, conference papers y revisiones sistemáticas o mapping reviews |

**Cadena booleana utilizada en la búsqueda semilla:**

```text
("software security" OR "secure software development" OR "secure SDLC" OR SSDLC OR DevSecOps OR DevOps)
AND ("risk management" OR "security risks" OR "threat modeling" OR "vulnerability assessment")
AND ("access control" OR authorization OR traceability OR "source code" OR repository)
```

La búsqueda se diseñó como una **búsqueda semilla de mini-review**, en línea con la lógica trabajada en la sesión 4 del curso. Por ello, además de la base principal, se utilizó rastreo hacia atrás de referencias para no perder trabajos fundacionales que siguen siendo relevantes para el problema.

## 4.3. Criterios de inclusión y exclusión

**Criterios de inclusión:**

- Publicaciones entre **2006 y 2025**.
- Estudios en inglés o español con texto completo disponible.
- Artículos y conferencias arbitradas con relación directa con al menos una de las dimensiones del estudio: gestión de riesgos, desarrollo seguro, control de acceso, trazabilidad o protección de artefactos de desarrollo.
- Revisiones sistemáticas, mapping reviews, estudios empíricos, marcos comparativos y trabajos metodológicos con aporte claro al ciclo de vida del desarrollo seguro.
- Estudios cuya contribución sea transferible al contexto de empresas peruanas de desarrollo de software, incluso cuando no estén situados en Perú.

**Criterios de exclusión:**

- Trabajos enfocados solo en seguridad de red, criptografía o seguridad perimetral sin conexión clara con el ciclo de desarrollo de software.
- Preprints, notas técnicas o literatura gris sin arbitraje académico.
- Estudios demasiado específicos en un dominio con baja transferibilidad al problema central.
- Textos duplicados, versiones preliminares o trabajos sin suficiente claridad metodológica.

## 4.4. Estructura PRISMA 2020

### Flujo preliminar de la búsqueda semilla

| Fase | n |
| --- | ---: |
| Registros identificados en la búsqueda principal | 31 |
| Registros adicionales por rastreo de referencias y corpus local | 12 |
| **Total identificado** | **43** |
| Duplicados o versiones redundantes removidas | 7 |
| Registros cribados por título y resumen | 36 |
| Excluidos en título y resumen | 20 |
| Textos completos evaluados para elegibilidad | 16 |
| Excluidos tras lectura completa | 6 |
| **Estudios incluidos en la síntesis cualitativa** | **10** |

### Razones principales de exclusión

- Fuera del foco del estudio: seguridad general sin vínculo suficiente con SDLC, acceso, trazabilidad o gestión de riesgos.
- Enfoque demasiado restringido a un contexto con baja transferibilidad.
- Ausencia de arbitraje académico o detalle metodológico insuficiente.

**Nota:** este flujo corresponde a un **borrador PRISMA preliminar** construido para la presente entrega. Los conteos deberán validarse nuevamente cuando se ejecute la búsqueda definitiva sobre una base cerrada y única para la versión final de la revisión.

El diagrama correspondiente a este flujo se presenta en el archivo **`prisma_diagram.png`** dentro de esta misma carpeta.

## 4.5. Los 10 estudios priorizados

| N.° | Estudio priorizado | Eje principal | Razón de prioridad |
| --- | --- | --- | --- |
| 1 | **Khan, R. A., Khan, S. U., Khan, H. U., y Ilyas, M. (2022). _Systematic Literature Review on Security Risks and Its Practices in Secure Software Development_. IEEE Access, 10, 5456-5481.** | Riesgos y prácticas de desarrollo seguro | Es la referencia de mayor valor sintético para el problema, porque organiza riesgos y prácticas a lo largo del SDLC y ofrece una base amplia para justificar variables y dimensiones del estudio. |
| 2 | **Valdés-Rodríguez, Y., Hochstetter-Diez, J., Díaz-Arancibia, J., y Cadena-Martínez, R. (2023). _Towards the Integration of Security Practices in Agile Software Development: A Systematic Mapping Review_. Applied Sciences, 13, 4578.** | Integración de seguridad en contextos ágiles | Resulta clave porque conecta desarrollo seguro con entornos ágiles, donde suelen aparecer tensiones entre velocidad, disciplina de control y madurez de seguridad. |
| 3 | **Tsai, Y.-T., Wang, C.-H., Chang, Y.-C., y Tong, L.-I. (2025). _Establishing Performance Baselines for Secure Software Development_. IET Information Security.** | Métricas y líneas base de desempeño | Aporta una mirada reciente sobre cómo medir capacidades de desarrollo seguro, lo cual es útil para traducir la gestión de riesgos en indicadores observables. |
| 4 | **Humayun, M., Jhanjhi, N., Almufareh, M. F., y Khalil, M. I. (2022). _Security Threat and Vulnerability Assessment and Measurement in Secure Software Development_. Computers, Materials & Continua, 71(3), 5039-5059.** | Evaluación de amenazas y vulnerabilidades | Fortalece la dimensión de evaluación y medición de amenazas dentro del SDLC y ayuda a sostener la parte cuantificable del estudio. |
| 5 | **Basin, D., Guarnizo, J., Krstić, S., Nguyen, H., y Ochoa, M. (2023). _Is Modeling Access Control Worth It?_ En _Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security (CCS '23)_.** | Control de acceso | Es uno de los estudios más directamente alineados con la dimensión de control de acceso, y además compara enfoques de implementación con evidencia empírica. |
| 6 | **Cleland-Huang, J., Gotel, O. C. Z., Hayes, J. H., Mäder, P., y Zisman, A. (2014). _Software Traceability: Trends and Future Directions_. En _Future of Software Engineering, FOSE 2014 Proceedings_ (pp. 55-69).** | Trazabilidad | Funciona como referencia ancla para la dimensión de trazabilidad y permite justificarla como capacidad estratégica, no solo como práctica documental. |
| 7 | **Othmane, L. B., Angin, P., Weffers, H., y Bhargava, B. (2014). _Extending the Agile Development Process to Develop Acceptably Secure Software_. IEEE Transactions on Dependable and Secure Computing, 11(6), 497-509.** | Desarrollo seguro en procesos ágiles | Es un estudio útil para explicar cómo integrar seguridad sin romper la lógica iterativa de equipos ágiles o de entrega continua. |
| 8 | **Sánchez-Gordón, M.-L., y Colomo-Palacios, R. (2020). _Security as Culture: A Systematic Literature Review of DevSecOps_. En _Proceedings of the IEEE/ACM 42nd International Conference on Software Engineering Workshops_ (pp. 266-269).** | Cultura DevSecOps | Complementa la visión técnica con una dimensión organizacional y cultural, especialmente pertinente para explicar por qué controles equivalentes producen resultados distintos. |
| 9 | **De Win, B., Scandariato, R., Buyens, K., Grégoire, J., y Joosen, W. (2009). _On the Secure Software Development Process: CLASP, SDL and Touchpoints Compared_. Information and Software Technology, 51(7), 1152-1171.** | Procesos y marcos de desarrollo seguro | Aporta una comparación temprana pero todavía valiosa entre marcos de desarrollo seguro, útil para sostener la dimensión de proceso y gobernanza. |
| 10 | **Basin, D. A., Doser, J., y Lodderstedt, T. (2006). _Model Driven Security: From UML Models to Access Control Infrastructures_. ACM Transactions on Software Engineering and Methodology, 15(1), 39-91.** | Diseño y formalización de acceso | Aunque es más fundacional, sigue siendo muy útil para la dimensión de acceso porque muestra cómo traducir políticas de control a infraestructura técnica de manera sistemática. |

## 4.6. Síntesis inicial de hallazgos

La revisión preliminar deja ver cinco patrones. Primero, la literatura coincide en que la seguridad sigue incorporándose con demasiada frecuencia de manera tardía, aun cuando existe suficiente evidencia sobre el costo de esa decisión. Segundo, la gestión de riesgos aparece como eje articulador del desarrollo seguro, pero muchas publicaciones se concentran más en marcos y prácticas que en evidencia empírica sobre su efectividad real. Tercero, la dimensión de **control de acceso** sí tiene estudios específicos, aunque la mayoría se orienta a modelado, detección de vulnerabilidades o entornos particulares, más que a su relación integrada con gestión de riesgos organizacional.

Cuarto, la **trazabilidad** está bien sustentada como capacidad de aseguramiento y gobernanza, pero menos conectada, en la literatura revisada, con métricas de seguridad aplicadas a empresas peruanas de desarrollo de software o a contextos organizacionales comparables. Quinto, la producción más reciente sobre DevSecOps y secure SDLC insiste en que los factores humanos y culturales siguen siendo una barrera persistente para consolidar prácticas seguras, incluso cuando las herramientas o marcos ya están disponibles.

## 4.7. Vacíos que justifican el estudio

- La literatura ofrece abundante discusión sobre secure SDLC, pero menos evidencia que conecte directamente la **madurez de la gestión de riesgos** con resultados concretos en **control de acceso**, **protección del código** y **trazabilidad**.
- Hay más trabajos sobre marcos, modelos o buenas prácticas que sobre cómo esas prácticas funcionan realmente dentro de empresas peruanas de desarrollo de software o en contextos organizacionales comparables con restricciones operativas reales.
- La dimensión de **protección del código fuente y de los artefactos de desarrollo** aparece menos desarrollada que la de acceso o la de prácticas generales de secure SDLC.
- Persisten vacíos contextuales para organizaciones latinoamericanas y, de manera más específica, para empresas peruanas de desarrollo de software.

## 4.8. Referencias de apoyo metodológico

Las siguientes referencias no forman parte de los diez estudios priorizados, pero sostienen la construcción metodológica de la revisión:

- Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., y otros. (2021). _The PRISMA 2020 statement: an updated guideline for reporting systematic reviews_. BMJ, 372, n71.
- Kitchenham, B., y Brereton, P. (2013). _A systematic review of systematic review process research in software engineering_. Information and Software Technology, 55, 2049-2075.

---

**Declaración de apoyo con IA:** Se utilizó asistencia de IA para ordenar el borrador, revisar redacción y ayudar a estructurar la síntesis. La selección de estudios, la interpretación de los vacíos y la organización metodológica del mini-review corresponden a la autora.
