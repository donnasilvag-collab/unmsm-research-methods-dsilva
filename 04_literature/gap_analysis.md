# Análisis de vacíos de investigación

## 4.1. Propósito

Este análisis de vacíos sintetiza qué aspectos siguen insuficientemente resueltos en la literatura revisada sobre desarrollo seguro de software, gestión de riesgos, control de acceso y trazabilidad. Su objetivo es mostrar con claridad por qué el problema de investigación propuesto no repite simplemente lo ya sabido, sino que responde a una zona todavía poco articulada entre marcos técnicos, prácticas organizacionales y evidencia aplicada.

## 4.2. Matriz de vacíos

| Tipo de vacío | Vacío identificado | Evidencia principal | Relevancia para el estudio |
| --- | --- | --- | --- |
| **Vacío de conocimiento** | La literatura describe riesgos, prácticas y marcos de secure SDLC, pero todavía ofrece poca evidencia integrada sobre cómo la **madurez de la gestión de riesgos** influye de manera concreta en el **control de acceso**, la **protección del código fuente** y la **trazabilidad** dentro de empresas de desarrollo de software. | Khan et al. (2022); Tsai et al. (2025); Valdés-Rodríguez et al. (2023) | Justifica la necesidad de estudiar la relación entre una variable organizacional amplia, como la gestión de riesgos, y resultados operativos específicos del proceso de desarrollo. |
| **Vacío metodológico** | Predominan revisiones, marcos comparativos y propuestas de buenas prácticas, pero son menos frecuentes los estudios que combinen **medición cuantitativa** y **explicación cualitativa** para entender por qué controles similares producen resultados distintos entre organizaciones. | Khan et al. (2022); Sánchez-Gordón y Colomo-Palacios (2020); De Win et al. (2009) | Respaldan la elección de un diseño de métodos mixtos, porque un enfoque solo descriptivo o exclusivamente técnico dejaría fuera la dimensión organizacional del problema. |
| **Vacío contextual** | La mayor parte de los estudios revisados se desarrolla en contextos internacionales generales, marcos industriales amplios o entornos académicos. Sigue habiendo poca evidencia centrada en **empresas peruanas** o, de forma más amplia, en organizaciones latinoamericanas de desarrollo de software. | Valdés-Rodríguez et al. (2023); Basin et al. (2023); Humayun et al. (2022) | Refuerza la pertinencia aplicada del estudio, porque permite producir evidencia situada en un contexto donde las restricciones institucionales, de recursos y de madurez pueden ser distintas. |
| **Vacío teórico-práctico** | Existen estándares y marcos sólidos, como NIST SSDF, NIST SP 800-53 y OWASP SAMM, pero estos lineamientos no explican por sí solos cómo se traducen en prácticas sostenidas ni cómo interactúan con factores como cultura, liderazgo, disciplina operativa o presión por entrega. | Souppaya et al. (2022); OWASP Foundation (2020); Tsai et al. (2025); Sánchez-Gordón y Colomo-Palacios (2020) | Abre espacio para una investigación que no se limite a verificar cumplimiento formal, sino que examine la brecha entre control prescrito y control realmente ejecutado. |
| **Vacío en control de acceso** | Sí existen estudios sobre modelado y vulnerabilidades de acceso, pero con frecuencia se concentran en arquitectura, web applications o enfoques altamente especializados. Hay menor desarrollo de trabajos que integren el control de acceso dentro de una mirada más amplia de gestión de riesgos en el SDLC. | Basin et al. (2023); Basin, Doser y Lodderstedt (2006) | Da sustento a una de las tres dimensiones dependientes del estudio y evita tratar el acceso como un problema aislado de diseño o configuración. |
| **Vacío en trazabilidad** | La trazabilidad está bien reconocida como capacidad clave de aseguramiento, gobernanza y mantenimiento de vínculos entre artefactos, pero no siempre aparece conectada a evaluaciones de seguridad organizacional o a la gestión de riesgos del desarrollo cotidiano. | Cleland-Huang et al. (2014) | Justifica abordar la trazabilidad no solo como una práctica documental, sino como un componente de control y auditabilidad dentro del desarrollo seguro. |
| **Vacío en protección del código y artefactos** | La literatura revisada ofrece más densidad en secure SDLC, amenazas y control de acceso que en la relación entre gestión de riesgos y **protección de repositorios, código fuente y artefactos de desarrollo** como objeto central de análisis. | Khan et al. (2022); Kolisnichenko et al. (2022); Tsai et al. (2025) | Refuerza la originalidad del estudio al incorporar una dimensión que suele quedar dispersa entre supply chain, prácticas de repositorio y control de cambios. |

## 4.3. Lectura integrada de los vacíos

La revisión no muestra una ausencia total de literatura. Lo que revela, más bien, es una **fragmentación** del conocimiento disponible. Algunos estudios se concentran en riesgos y prácticas a lo largo del SDLC; otros, en marcos de proceso; otros, en control de acceso; otros, en trazabilidad; y otros, en cultura DevSecOps. El problema es que esos aportes no siempre convergen en una pregunta integrada sobre cómo la gestión de riesgos repercute en controles concretos del desarrollo de software.

Ese punto es importante porque el estudio no pretende demostrar que la seguridad es importante, algo que la literatura ya ha establecido con claridad. Lo que busca es una contribución más específica: comprender si una mayor madurez en gestión de riesgos se relaciona efectivamente con mejores resultados en acceso, protección del código y trazabilidad, y explicar por qué esa relación puede fortalecerse o debilitarse según el contexto organizacional.

## 4.4. Cómo responde esta investigación a esos vacíos

La propuesta de investigación responde a los vacíos identificados de cuatro maneras:

- **Integra dimensiones que suelen estudiarse por separado:** gestión de riesgos, control de acceso, protección del código fuente y trazabilidad.
- **Combina medición e interpretación:** no se limita a describir marcos o prácticas, sino que busca relacionar indicadores cuantitativos con explicaciones cualitativas.
- **Aporta contexto aplicado:** orienta el análisis hacia empresas peruanas de desarrollo de software, un espacio poco visible en la literatura revisada.
- **Examina la brecha entre lo formal y lo real:** no asume que la existencia de políticas o herramientas equivale automáticamente a controles eficaces.

## 4.5. Implicación para la formulación del problema

A partir de este análisis, el problema de investigación se fortalece en un punto central: no basta con preguntar si las organizaciones tienen prácticas de seguridad, ni con listar marcos disponibles. La pregunta más relevante es si la gestión de riesgos realmente se traduce en mejores capacidades de control dentro del desarrollo de software y qué condiciones explican esa traducción. Ese es, precisamente, el espacio donde este estudio puede hacer una contribución académica y aplicada más defendible.

## 4.6. Referencias base utilizadas para el análisis

- Basin, D., Guarnizo, J., Krstić, S., Nguyen, H., y Ochoa, M. (2023). *Is Modeling Access Control Worth It?*
- Basin, D. A., Doser, J., y Lodderstedt, T. (2006). *Model Driven Security: From UML Models to Access Control Infrastructures*.
- Cleland-Huang, J., Gotel, O. C. Z., Hayes, J. H., Mäder, P., y Zisman, A. (2014). *Software Traceability: Trends and Future Directions*.
- De Win, B., Scandariato, R., Buyens, K., Grégoire, J., y Joosen, W. (2009). *On the Secure Software Development Process: CLASP, SDL and Touchpoints Compared*.
- Humayun, M., Jhanjhi, N., Almufareh, M. F., y Khalil, M. I. (2022). *Security Threat and Vulnerability Assessment and Measurement in Secure Software Development*.
- Khan, R. A., Khan, S. U., Khan, H. U., e Ilyas, M. (2022). *Systematic Literature Review on Security Risks and Its Practices in Secure Software Development*.
- Kolisnichenko, O., Kolomytsev, M., y Nosok, S. (2022). *Software security risk management in DEVOPS methodology*.
- OWASP Foundation. (2020). *OWASP SAMM v2*.
- Sánchez-Gordón, M.-L., y Colomo-Palacios, R. (2020). *Security as Culture: A Systematic Literature Review of DevSecOps*.
- Souppaya, M., Scarfone, K., y Dodson, D. (2022). *Secure Software Development Framework (SSDF) Version 1.1*.
- Tsai, Y.-T., Wang, C.-H., Chang, Y.-C., y Tong, L.-I. (2025). *Establishing Performance Baselines for Secure Software Development*.
- Valdés-Rodríguez, Y., Hochstetter-Diez, J., Díaz-Arancibia, J., y Cadena-Martínez, R. (2023). *Towards the Integration of Security Practices in Agile Software Development: A Systematic Mapping Review*.

---

**Declaración de apoyo con IA:** Se utilizó asistencia de IA para apoyar la organización del borrador, revisar redacción y mejorar la claridad expositiva. La identificación de vacíos, la articulación del problema y la interpretación académica corresponden a la autora.
