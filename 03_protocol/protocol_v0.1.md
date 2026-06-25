# Protocolo de investigación (v0.1)

## 3.1. Título

**Influencia de la gestión de riesgos de seguridad de la información en la eficacia del control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software en empresas peruanas: protocolo de un estudio de métodos mixtos**

## 3.2. Resumen

En las empresas peruanas de desarrollo de software, la seguridad de la información ya no puede tratarse como una revisión tardía ni como un requisito aislado del trabajo técnico. Los repositorios de código, los accesos privilegiados, los pipelines de integración y despliegue, y los registros de actividad forman parte de una superficie de riesgo cada vez más compleja. Aunque muchas organizaciones declaran aplicar prácticas de gestión de riesgos, todavía existe poca evidencia empírica sobre cómo esa gestión influye realmente en tres dimensiones críticas del desarrollo seguro: el control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software.

Esta investigación propone un estudio de métodos mixtos con diseño secuencial explicativo en empresas peruanas de desarrollo de software. En una primera fase cuantitativa se evaluará la relación entre la madurez de la gestión de riesgos de seguridad de la información y la eficacia de los controles vinculados a acceso, resguardo del código y trazabilidad. En una segunda fase cualitativa se buscará explicar, mediante entrevistas semiestructuradas y revisión documental, por qué esas relaciones se fortalecen o se debilitan en contextos organizacionales concretos del entorno peruano. Se espera obtener una caracterización más sólida del problema, identificar factores técnicos y humanos que condicionan la efectividad de los controles y formular recomendaciones aplicables para fortalecer la seguridad del desarrollo de software.

## 3.3. Introducción y planteamiento del problema

### Planteamiento del problema

La transformación digital ha incrementado la dependencia de las organizaciones respecto del software y, con ello, la exposición a riesgos asociados al acceso no autorizado, la fuga de código fuente, la pérdida de trazabilidad y la débil gobernanza de cambios dentro del ciclo de desarrollo. En muchas empresas, sobre todo aquellas que trabajan con enfoques ágiles, DevOps o integración continua, la presión por entregar con rapidez puede llevar a que los controles de seguridad existan de manera formal, pero no siempre se apliquen con la misma solidez en la práctica cotidiana.

La literatura reciente muestra que la seguridad todavía suele integrarse de forma desigual en el desarrollo de software. Persisten brechas entre política y ejecución, entre control documentado y comportamiento real, y entre madurez declarada y capacidad efectiva para prevenir incidentes o detectar desviaciones. En ese contexto, no basta con saber si una empresa tiene políticas o herramientas; también importa comprender si la gestión de riesgos influye de manera concreta en la calidad de sus controles sobre accesos, repositorios y trazabilidad operativa.

El problema de investigación surge, entonces, de una insuficiencia de evidencia aplicada: todavía no está suficientemente claro cómo y en qué medida la madurez de la gestión de riesgos de seguridad de la información se relaciona con resultados verificables dentro del desarrollo de software en empresas peruanas, ni qué factores organizacionales explican las diferencias entre empresas con niveles de control aparentemente similares.

### Relevancia del estudio

Este problema es relevante por razones académicas y prácticas. En el plano académico, permite aportar evidencia sobre una relación que suele mencionarse en la literatura de seguridad y desarrollo seguro, pero que con frecuencia se aborda de forma fragmentada. En el plano aplicado, los hallazgos pueden orientar decisiones sobre gobierno de accesos, resguardo del código fuente, auditoría, cumplimiento y fortalecimiento de capacidades internas en empresas peruanas de desarrollo de software.

## 3.4. Revisión breve de literatura

La revisión preliminar sugiere cuatro ideas consistentes. Primero, el desarrollo seguro de software sigue enfrentando dificultades para integrar la seguridad a lo largo de todo el ciclo de vida, en lugar de tratarla como una actividad tardía o reactiva. Segundo, la gestión de riesgos adquiere un papel central en entornos ágiles y DevOps, donde la velocidad operativa puede ampliar la exposición si no existe una gobernanza clara. Tercero, la eficacia de los controles no depende únicamente de herramientas o políticas, sino también de factores como cultura organizacional, formación, liderazgo y disciplina operativa. Cuarto, aún existe una necesidad de estudios que articulen medición e interpretación para explicar por qué algunas organizaciones convierten la gestión de riesgos en prácticas efectivas, mientras otras mantienen una adopción más superficial.

En esta línea, Khan et al. (2022) advierten que muchas organizaciones todavía no integran la seguridad de forma transversal en el desarrollo de software. Kolisnichenko et al. (2022) sostienen que la gestión de riesgos debe atravesar todas las etapas de DevOps para evitar que la aceleración operativa incremente la exposición. Valdés-Rodríguez et al. (2023) muestran que la incorporación de prácticas de seguridad en entornos ágiles sigue siendo un reto importante. Finalmente, Tsai et al. (2025) proponen líneas base de desempeño para secure software development que vinculan la gestión proactiva y reactiva de la seguridad con resultados más sólidos.

## 3.5. Preguntas de investigación y objetivos

### Pregunta general de investigación

**¿Cómo y en qué medida la madurez de la gestión de riesgos de seguridad de la información influye en la eficacia del control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software en empresas peruanas?**

### Preguntas específicas

- ¿Qué dimensiones de la gestión de riesgos de seguridad de la información muestran mayor relación con la eficacia del control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software?
- ¿Qué diferencias se observan entre empresas participantes con distintos niveles de madurez en la gestión de riesgos?
- ¿Cómo explican desarrolladores, líderes técnicos y responsables de seguridad las brechas entre controles formales y prácticas reales dentro del proceso de desarrollo?
- ¿Qué factores organizacionales y operativos ayudan a explicar los resultados cuantitativos observados?

### Objetivo general

Analizar cómo y en qué medida la madurez de la gestión de riesgos de seguridad de la información influye en la eficacia del control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software en empresas peruanas.

### Objetivos específicos

- Caracterizar el nivel de madurez de la gestión de riesgos de seguridad de la información en empresas peruanas de desarrollo de software.
- Evaluar la relación entre dicha madurez y la eficacia de los controles asociados a acceso, protección del código fuente y trazabilidad del desarrollo de software.
- Identificar factores organizacionales, humanos y operativos que expliquen diferencias entre los resultados observados en la fase cuantitativa.
- Integrar la evidencia cuantitativa y cualitativa para formular recomendaciones orientadas al fortalecimiento del desarrollo seguro de software.

## 3.6. Metodología

### Paradigma y diseño

La investigación se desarrollará bajo un **paradigma de métodos mixtos** con orientación **pragmática**, mediante un **diseño secuencial explicativo**. La primera fase será cuantitativa y buscará identificar patrones de relación entre variables. La segunda fase será cualitativa y tendrá como propósito explicar en mayor profundidad esos patrones, especialmente en los casos donde exista distancia entre el control formal y la práctica real.

### Alcance del estudio

El estudio tendrá un alcance **explicativo** y un enfoque aplicado. No busca diseñar un artefacto tecnológico nuevo, sino producir conocimiento útil sobre la relación entre la gestión de riesgos y la efectividad de ciertos controles críticos dentro del desarrollo de software.

### Contexto, población y muestra

La población de interés estará conformada por empresas peruanas de desarrollo de software que gestionen repositorios, accesos y procesos de trazabilidad como parte de su operación habitual. Para esta etapa preliminar se considera priorizar empresas ubicadas en Lima Metropolitana o con operación formal en el país y trabajo bajo enfoques ágiles, DevOps o integración continua.

En la fase cuantitativa se empleará un muestreo no probabilístico intencional. Se proyecta recopilar información de aproximadamente **50 a 80 participantes** entre desarrolladores, líderes técnicos, perfiles DevOps, responsables de calidad y responsables de seguridad, distribuidos en **6 a 10 organizaciones**. En la fase cualitativa se seleccionará un subconjunto de **10 a 15 informantes clave** a partir de los resultados cuantitativos, buscando contrastar perfiles, niveles de madurez y situaciones donde aparezcan patrones especialmente consistentes o contradictorios.

### Técnicas e instrumentos de recolección

- **Encuesta estructurada:** permitirá medir percepciones y prácticas relacionadas con identificación, evaluación, tratamiento y monitoreo de riesgos, así como con control de acceso, protección del código fuente y trazabilidad.
- **Entrevistas semiestructuradas:** se aplicarán a informantes clave para profundizar en decisiones, tensiones, barreras de adopción y diferencias entre procedimientos formales y práctica cotidiana.
- **Revisión documental focalizada:** cuando exista autorización, se revisarán políticas, lineamientos, procedimientos, bitácoras o evidencias institucionales que ayuden a contextualizar los hallazgos.

### Variables y dimensiones preliminares

La **variable explicativa** será la madurez de la gestión de riesgos de seguridad de la información, observada a través de dimensiones como gobernanza, identificación de riesgos, evaluación, tratamiento, monitoreo, capacitación y seguimiento. Las **variables de resultado** serán: **eficacia del control de acceso**, **protección del código fuente** y **trazabilidad del desarrollo de software**.

### Estrategia de análisis

En la fase cuantitativa se realizará análisis descriptivo de los datos, revisión de consistencia del instrumento y análisis de asociación entre variables. De manera preliminar, se considera utilizar correlaciones, comparaciones entre grupos y modelos de regresión, según la calidad y el comportamiento de los datos recopilados.

En la fase cualitativa se empleará análisis temático para identificar patrones de sentido en los testimonios de los participantes. Finalmente, ambas fases se integrarán mediante una estrategia de meta-inferencia, de modo que los resultados cualitativos ayuden a explicar, matizar o reinterpretar los hallazgos cuantitativos.

## 3.7. Consideraciones éticas

El estudio abordará información potencialmente sensible relacionada con prácticas internas de seguridad, por lo que la confidencialidad será una condición central del diseño. No se solicitará acceso a código fuente propietario ni a secretos industriales; la investigación se concentrará en prácticas, percepciones, políticas y evidencias organizacionales que puedan analizarse sin comprometer activos críticos. La participación será voluntaria y se trabajará con consentimiento informado.

Los datos serán anonimizados desde la recolección y se evitará identificar personas, equipos u organizaciones en los productos públicos del estudio, salvo autorización expresa. El protocolo se alineará con la **Ley N.° 29733, Ley de Protección de Datos Personales**, y con el **Código Nacional de Integridad Científica** aprobado por CONCYTEC mediante la **Resolución de Presidencia N.° 028-2024-CONCYTEC-P**. Antes del trabajo de campo se considerará la revisión correspondiente por el comité o instancia ética aplicable.

## 3.8. Resultados esperados

- Un diagnóstico preliminar sobre el nivel de madurez de la gestión de riesgos de seguridad de la información en empresas peruanas de desarrollo de software.
- Evidencia sobre la relación entre dicha madurez y la eficacia del control de acceso, la protección del código fuente y la trazabilidad del desarrollo de software.
- Identificación de factores organizacionales y operativos que expliquen diferencias entre controles declarados y controles efectivamente sostenidos.
- Recomendaciones aplicables para fortalecer prácticas de desarrollo seguro en contextos ágiles, DevOps o de integración continua.
- Un repositorio reproducible con la documentación del proceso, los instrumentos utilizados y los productos académicos permitidos por las condiciones de confidencialidad.

## 3.9. Cronograma y factibilidad

### Cronograma preliminar

- **Meses 1-4:** afinamiento del protocolo, revisión de literatura, diseño de instrumentos y preparación para evaluación ética.
- **Meses 5-8:** validación preliminar de instrumentos, contacto con organizaciones y gestión de accesos para el trabajo de campo.
- **Meses 9-14:** recolección y análisis inicial de la fase cuantitativa.
- **Meses 15-20:** selección de casos o perfiles de interés, entrevistas semiestructuradas y análisis cualitativo.
- **Meses 21-24:** integración de resultados, discusión y formulación de recomendaciones.
- **Meses 25-30:** redacción de artículos o capítulos preliminares y consolidación del repositorio reproducible.
- **Meses 31-36:** escritura final de tesis, revisión interna y preparación para la sustentación.

### Factibilidad y previsiones

El estudio es metodológicamente factible, pero depende de dos condiciones críticas: acceso suficiente a organizaciones dispuestas a colaborar y disponibilidad de participantes para hablar sobre prácticas de seguridad sin comprometer información sensible. Por ello, el cronograma incorpora márgenes para gestión de permisos, evaluación ética, validación de instrumentos y contingencias propias del trabajo de campo. Se considera necesario reservar un buffer razonable para retrasos asociados a coordinación institucional, cambios de agenda o necesidad de recolección complementaria.

### Estimación preliminar de recursos

- Transcripción y apoyo de sistematización de entrevistas: **S/. 1,500**
- Desplazamientos, reuniones y coordinación de campo: **S/. 1,200**
- Herramientas digitales, almacenamiento seguro y respaldo: **S/. 800**
- Contingencias operativas: **S/. 1,000**

## 3.10. Bibliografía preliminar

Khan, R. A., Khan, S. U., Khan, H. U., e Ilyas, M. (2022). *Systematic Literature Review on Security Risks and Its Practices in Secure Software Development*. IEEE Access, 10, 5456-5481.

Kolisnichenko, O., Kolomytsev, M., y Nosok, S. (2022). *Software Security Risk Management in DEVOPS Methodology*. Theoretical and Applied Cybersecurity, 3(1).

Tsai, Y.-T., Wang, C.-H., Chang, Y.-C., y Tong, L.-I. (2025). *Establishing Performance Baselines for Secure Software Development*. IET Information Security, 2025, 6139424.

Valdés-Rodríguez, Y., Hochstetter-Diez, J., Díaz-Arancibia, J., y Cadena-Martínez, R. (2023). *Towards the Integration of Security Practices in Agile Software Development: A Systematic Mapping Review*. Applied Sciences, 13, 4578.

Souppaya, M., Scarfone, K., y Dodson, D. (2022). *Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities* (NIST SP 800-218). National Institute of Standards and Technology.

Joint Task Force. (2020). *Security and Privacy Controls for Information Systems and Organizations* (NIST SP 800-53 Rev. 5). National Institute of Standards and Technology.

Pillitteri, V. (2022). *Assessing Security and Privacy Controls in Information Systems and Organizations* (NIST SP 800-53A Rev. 5). National Institute of Standards and Technology.

OWASP Foundation. (2020). *OWASP SAMM v2*.

Cleland-Huang, J., Gotel, O. C. Z., Hayes, J. H., Mäder, P., y Zisman, A. (2014). *Software Traceability: Trends and Future Directions*. En *Future of Software Engineering, FOSE 2014 Proceedings* (pp. 55-69).

Sánchez-Gordón, M.-L., y Colomo-Palacios, R. (2020). *Security as Culture: A Systematic Literature Review of DevSecOps*. En *Proceedings of the IEEE/ACM 42nd International Conference on Software Engineering Workshops* (pp. 266-269).

CONCYTEC. (2024). *Código Nacional de Integridad Científica*. Resolución de Presidencia N.° 028-2024-CONCYTEC-P.

Ley N.° 29733. Ley de Protección de Datos Personales.

---

**Declaración de apoyo con IA:** Se utilizó asistencia de IA para apoyar la organización del borrador, mejorar la redacción y revisar la claridad formal del texto. La definición del problema, las decisiones metodológicas, la formulación de objetivos y la estructura intelectual del protocolo corresponden a la autora.
