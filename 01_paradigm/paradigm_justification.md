# Justificación del paradigma

## Paradigmas de investigación para la seguridad del software: positivismo, interpretativismo y métodos mixtos

### 1.1. Tema de investigación y contexto

La transformación digital ha convertido al software en una infraestructura crítica para las organizaciones. En las empresas peruanas de desarrollo de software ya no se administran únicamente aplicaciones: también se gestionan repositorios de código fuente, credenciales privilegiadas, pipelines de integración y despliegue continuo, entornos en la nube, dependencias de terceros, bitácoras de actividad y otros activos sensibles. En este escenario, la seguridad de la información deja de ser un requisito accesorio y pasa a ser una condición necesaria para la continuidad operativa, la protección de la propiedad intelectual, el cumplimiento normativo y la confianza de clientes y usuarios.

Pese a ello, la literatura reciente sigue mostrando una brecha importante entre ese ideal y la práctica cotidiana. Khan et al. (2022), en su revisión sistemática sobre riesgos y prácticas de secure software development, advierten que muchas organizaciones continúan tratando la seguridad como un asunto tardío y no como una actividad integrada a todo el ciclo de vida del desarrollo de software. Kolisnichenko et al. (2022) sostienen, en la misma línea, que la gestión de riesgos debe aplicarse en todas las etapas de DevOps, ya que acelerar el desarrollo sin incorporar seguridad incrementa de forma directa la exposición a ataques. Del mismo modo, Valdés-Rodríguez et al. (2023) muestran que la integración de prácticas de seguridad en entornos ágiles sigue siendo un reto relevante, sobre todo en organizaciones con restricciones de tiempo, recursos o madurez institucional.

El problema, además, no es exclusivamente técnico. Los materiales del curso y los artículos revisados coinciden en que la adopción efectiva de prácticas de desarrollo seguro depende también de variables organizacionales: cultura de seguridad, liderazgo, gobernanza, entrenamiento, métricas y nivel de madurez. Tsai et al. (2025), por ejemplo, proponen líneas base de desempeño para secure software development apoyadas tanto en la conciencia proactiva de seguridad como en la gestión reactiva del riesgo. Esa doble dimensión resulta especialmente útil para este estudio, porque sugiere que la eficacia del control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software no dependen solo de que existan controles formales, sino de cómo esos controles son comprendidos, aplicados y sostenidos en la práctica.

Con base en ello, el problema de investigación se formula así: **la influencia de la gestión de riesgos de seguridad de la información en la eficacia del control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software en empresas peruanas**, con especial interés en contextos de trabajo ágil, DevOps o integración continua.

### 1.2. Pregunta preliminar de investigación

¿Cómo influye la gestión de riesgos de seguridad de la información en la eficacia del control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software en empresas peruanas?

**Tres formulaciones de la misma pregunta de investigación:**

**Versión A - Enfoque explicativo-cuantitativo:** ¿En qué medida el nivel de madurez de la gestión de riesgos de seguridad de la información predice la eficacia del control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software en empresas peruanas?

**Versión B - Enfoque organizacional-interpretativo:** ¿Cómo experimentan desarrolladores, líderes técnicos y responsables de seguridad de empresas peruanas la relación entre la gestión de riesgos y la implementación real de controles de acceso, resguardo del código y trazabilidad dentro del proceso de desarrollo?

**Versión C - Enfoque integrador de métodos mixtos:** ¿Qué dimensiones medibles de la gestión de riesgos se asocian con mejores resultados en control de acceso, protección del código fuente y trazabilidad del desarrollo de software en empresas peruanas, y cómo explican los factores humanos y organizacionales esas asociaciones?

### 1.3. Paradigma elegido y justificación

La presente investigación adopta un **paradigma de métodos mixtos** con orientación **pragmática**, desarrollado mediante un **diseño secuencial explicativo**. La lógica general es primero identificar y medir relaciones entre variables y, después, interpretar con mayor profundidad por qué esas relaciones se manifiestan de determinada manera en contextos organizacionales concretos.

Esta decisión responde a un criterio metodológico central del curso: la elección del paradigma debe derivarse de la naturaleza del problema y no de una preferencia personal o de una costumbre disciplinar. En ese marco, los métodos mixtos solo se justifican cuando un único enfoque resulta insuficiente para comprender el fenómeno de estudio. En este caso, esa insuficiencia es clara.

No se adopta un paradigma **positivista puro** como paradigma principal, aunque la dimensión cuantitativa del estudio es indispensable. Un enfoque positivista permitiría medir variables, construir indicadores, estimar asociaciones y evaluar si una mayor madurez en la gestión de riesgos se relaciona con mejores resultados en control de acceso, protección del código fuente y trazabilidad. Esa mirada es necesaria porque el problema sí incluye dimensiones objetivables: políticas, mecanismos de control, prácticas formales, frecuencia de incidentes, uso de registros, auditoría de actividades y cumplimiento de procedimientos. Sin embargo, una lectura exclusivamente positivista dejaría sin responder una pregunta clave: por qué organizaciones con controles aparentemente semejantes obtienen resultados distintos. La literatura revisada sugiere que, en esa diferencia, pesan factores como la madurez organizacional, el entrenamiento, la resistencia al cambio, el liderazgo y la cultura de seguridad. Esos elementos no se agotan en una escala numérica.

Tampoco se adopta un paradigma **interpretativista puro**. Una aproximación cualitativa permitiría comprender cómo los actores entienden la seguridad, cómo negocian prioridades entre velocidad y control, por qué ciertos mecanismos son percibidos como útiles o como una carga burocrática, y de qué manera se producen fallas de trazabilidad o relajamiento de controles en la práctica cotidiana. Esa comprensión es valiosa, pero por sí sola no ofrece suficiente base para estimar la magnitud de la influencia entre variables ni para sostener comparaciones entre equipos u organizaciones. Si la pregunta de investigación incluye el verbo “influir”, entonces no basta con describir percepciones; también es necesario examinar relaciones observables.

Asimismo, se descarta la **ciencia del diseño** como paradigma principal. Aunque este estudio podría derivar más adelante en un modelo de evaluación, una guía de mejora o un marco de recomendaciones para desarrollo seguro, su propósito central no es diseñar un artefacto tecnológico nuevo y validarlo bajo criterios de utilidad, novedad y rigor, sino explicar una relación entre prácticas de gestión del riesgo y resultados organizacionales y técnicos de seguridad. Por ello, el núcleo de la investigación es explicativo, no artefactual.

En consecuencia, el paradigma de métodos mixtos resulta el mejor ajuste porque el fenómeno tiene una dimensión medible y otra claramente interpretativa. La fase cuantitativa puede mostrar, por ejemplo, que ciertas dimensiones de la gestión de riesgos se asocian con mejores niveles de trazabilidad o con controles de acceso más robustos. La fase cualitativa, en cambio, puede explicar por qué esa asociación aparece, se debilita o incluso se contradice en determinados contextos: falta de capacitación, baja adopción, presiones de entrega, gobernanza difusa o cultura de seguridad débil. El valor del diseño mixto no está en combinar técnicas por amplitud, sino en producir una interpretación más sólida de un problema que no puede entenderse bien desde un solo tipo de evidencia.

Por ello, la fase cualitativa no se plantea como un simple complemento narrativo de los datos cuantitativos. La integración esperada es sustantiva: los hallazgos cualitativos deberán ayudar a reinterpretar los resultados cuantitativos y a explicar por qué la gestión de riesgos funciona mejor en unas organizaciones que en otras, aun cuando los controles formales parezcan comparables. Esa es, precisamente, la condición que convierte a un estudio de métodos mixtos en una investigación coherente y no en dos estudios paralelos presentados bajo una misma carátula.

### 1.4. Implicaciones de la elección del paradigma

**Tipo de datos:** La investigación requerirá datos cuantitativos y cualitativos. La parte cuantitativa puede incluir escalas de madurez de gestión de riesgos, evidencia sobre políticas y prácticas de acceso, uso de controles sobre repositorios, mecanismos de trazabilidad, auditoría de actividades, formación en seguridad y cumplimiento de procedimientos. La parte cualitativa puede incluir entrevistas semiestructuradas con desarrolladores, líderes de proyecto, responsables de seguridad o perfiles DevOps, además del análisis de documentos, flujos de trabajo y prácticas organizacionales.

**Métodos:** El paradigma orienta hacia un diseño secuencial explicativo. Primero, una fase cuantitativa para identificar patrones de asociación o influencia entre la gestión de riesgos y las tres dimensiones dependientes del estudio. Después, una fase cualitativa para explicar esos patrones, sobre todo allí donde existan brechas entre el control formal y la práctica real. La solidez del estudio no dependerá solo del rigor de cada fase por separado, sino de la calidad de la integración entre ambas.

**Criterios de validez:** La fase cuantitativa exigirá claridad en la operacionalización de variables, consistencia de instrumentos y técnicas de análisis adecuadas. La fase cualitativa exigirá transparencia interpretativa, trazabilidad analítica y coherencia entre evidencia y conclusiones. En el plano integrador, el criterio clave será la calidad de las meta-inferencias: si la explicación final logra articular de manera convincente lo que los datos muestran con lo que los actores hacen, interpretan y experimentan.

**Contribución esperada:** La contribución del estudio sería doble. En el plano académico, aportar evidencia sobre cómo la gestión de riesgos de seguridad de la información influye en procesos críticos del desarrollo seguro de software. En el plano aplicado, generar hallazgos útiles para fortalecer políticas, prácticas y capacidades organizacionales relacionadas con control de acceso, protección del código fuente y trazabilidad dentro de empresas peruanas de desarrollo de software, especialmente en entornos de desarrollo ágil o DevOps.

### 1.5. Una duda o tensión

La principal tensión metodológica del estudio está en el acceso y la calidad de la evidencia. Las organizaciones de software suelen considerar sensible la información relacionada con controles de acceso, incidentes, prácticas reales de repositorio, fallas de trazabilidad y debilidades de seguridad. Esto puede limitar la disponibilidad de datos directos y empujar al investigador a depender demasiado de respuestas autodeclaradas, que con frecuencia sobreestiman el nivel real de madurez. Mi principal duda, por tanto, no es si el paradigma mixto encaja, sino cómo asegurar que la fase cuantitativa capture prácticas efectivas y no solo cumplimiento declarado, y que la fase cualitativa logre suficiente apertura de los participantes para explicar tensiones que muchas organizaciones prefieren no hacer explícitas.

## Referencias citadas

Khan, R. A., Khan, S. U., Khan, H. U., e Ilyas, M. (2022). *Systematic Literature Review on Security Risks and Its Practices in Secure Software Development*. IEEE Access, 10, 5456-5481.

Kolisnichenko, O., Kolomytsev, M., y Nosok, S. (2022). *Software Security Risk Management in DEVOPS Methodology*. Theoretical and Applied Cybersecurity, 3(1).

Tsai, Y.-T., Wang, C.-H., Chang, Y.-C., y Tong, L.-I. (2025). *Establishing Performance Baselines for Secure Software Development*. IET Information Security, 2025, 6139424.

Valdés-Rodríguez, Y., Hochstetter-Diez, J., Díaz-Arancibia, J., y Cadena-Martínez, R. (2023). *Towards the Integration of Security Practices in Agile Software Development: A Systematic Mapping Review*. Applied Sciences, 13, 4578.

Souppaya, M., Scarfone, K., y Dodson, D. (2022). *Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities* (NIST SP 800-218). National Institute of Standards and Technology.

OWASP Foundation. (2020). *OWASP SAMM v2*.

Cleland-Huang, J., Gotel, O. C. Z., Hayes, J. H., Mäder, P., y Zisman, A. (2014). *Software Traceability: Trends and Future Directions*. En *Future of Software Engineering, FOSE 2014 Proceedings* (pp. 55-69).
