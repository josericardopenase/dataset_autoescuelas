# Exámenes de conducir por autoescuela en la provincia de Canarias

## Descripción

Este dataset recopila información sobre el número de alumnos **aptos y no aptos** en los exámenes de tráfico, desglosado por **año, mes, tipo de examen y autoescuela**. Incluye también datos de los centros de examen, ubicación y detalles de contacto de las autoescuelas.

## Contexto

En España existen numerosas autoescuelas, y tanto los futuros alumnos como las propias autoescuelas necesitan información confiable sobre tasas de aprobación y rendimiento en los exámenes.  

El dataset proporcionará información valiosa para:  

- Identificar autoescuelas con mayores tasas de éxito.  
- Determinar los mejores centros de examen según resultados.  
- Apoyar la toma de decisiones estratégicas para negocios como **Autoescuelas ECO**, propiedad de la familia del alumno, que podrá utilizar estos datos para análisis y planificación.  

Los datos se han recopilado a partir de dos fuentes oficiales de la **Dirección General de Tráfico (DGT)**:  

- [Listado de autoescuelas](https://www.dgt.es/conoce-la-dgt/con-quien-trabajamos/autoescuelas/)  
- [Resultados de exámenes de tráfico por provincia](https://www.dgt.es/menusecundario/dgt-en-cifras/matraba-listados/conductores-autoescuelas.html)  

## Representación gráfica

![Gráfico](img_1.png){ width=50% style="display:inline-block;" }


## Contenido del dataset

El conjunto de datos contiene las siguientes variables:

- **nombre**: Nombre de la autoescuela o centro examinador.  
- **lat, lon**: Coordenadas geográficas del centro de examen.  
- **codigo_centro**: Identificador único del centro de examen.  
- **codigo_autoescuela**: Identificador único de la autoescuela.  
- **codigo_seccion**: Código de sección administrativa o territorial del centro.  
- **direccion**: Dirección física de la autoescuela o del centro de examen.  
- **telefono**: Número de contacto de la autoescuela.  
- **email**: Correo electrónico de la autoescuela.  
- **provincia**: Provincia donde se encuentra la autoescuela o centro de examen.  
- **centro_examen**: Nombre del centro donde se realiza el examen.  
- **NOMBRE_AUTOESCUELA**: Nombre oficial de la autoescuela.  
- **month, year**: Mes y año en que se realizó el examen.  
- **tipo_examen**: Tipo de examen (teórico, práctico, etc.).  
- **permiso**: Tipo de permiso de conducción (B, A, C, etc.).  
- **aptos**: Total de alumnos aprobados.  
- **aptos_primera_conv**: Aprobados en primera convocatoria.  
- **aptos_segunda_conv**: Aprobados en segunda convocatoria.  
- **aptos_tercera_o_cuarta_conv**: Aprobados en tercera o cuarta convocatoria.  
- **aptos_quinta_conv**: Aprobados en quinta convocatoria.  
- **no_aptos**: Alumnos que no aprobaron.  
- **presentados**: Total de alumnos presentados al examen.

## Inspiración

El objetivo principal es proporcionar un dataset que permita a **Autoescuelas ECO** analizar la evolución de los resultados de exámenes, comparando por:  

- Tipo de examen y permiso de conducción.  
- Centro de examen.  
- Sección administrativa de la autoescuela.  

La idea es establecer un **proceso continuo de recolección de datos** mediante scrapping periódico, facilitando un dataset actualizado para minería de datos y análisis predictivo.

## Código utilizado

Durante la práctica se emplearon las siguientes herramientas:  

- **Scrapy y Selenium**: Para realizar web scraping de las fuentes oficiales.  
- **Pandas**: Para la limpieza y transformación de los datos.  
- **Docker**: Para la contenedorización del proyecto y reproducibilidad del entorno.

## Licencia

Este contenido se distribuye bajo la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).  

- Se requiere **atribución** al autor.  
- No se permite uso comercial.  
- Las obras derivadas deben compartirse bajo la **misma licencia**.
