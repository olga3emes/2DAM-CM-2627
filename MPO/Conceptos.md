# Conceptos

Tipos de escalado: Vertical y Horizontal

Tipos de servicios: IaaS, PaaS, SaaS

Servicios de AWS importantes: 
EC2, S3, RDS, Lambda, CloudFront, VPC, IAM, CloudWatch, CloudTrail.

EC2: "Los servidores - como si me creo una MV". Elastic Compute Cloud, es un servicio de computación en la nube que permite a los usuarios ejecutar instancias de servidores virtuales en la infraestructura de AWS.

S3: "Almacenamiento de objetos - como si me creo un disco duro - Google Drive cateto". Simple Storage Service, es un servicio de almacenamiento de objetos que permite a los usuarios almacenar y recuperar datos en la nube de manera escalable y segura.

RDS: "Base de datos - como si me creo una base de datos en mi ordenador". Relational Database Service, es un servicio administrado de bases de datos relacionales que facilita la configuración, operación y escalado de bases de datos en la nube.

Lambda: "Funciones(procedimientos almacenados) - como si me creo un script que se ejecuta en la nube". AWS Lambda es un servicio de computación sin servidor que permite a los usuarios ejecutar código en respuesta a eventos sin tener que aprovisionar o administrar servidores.

CloudFront: "CDN - como si me creo un servidor de caché". Amazon CloudFront es un servicio de red de entrega de contenido (CDN) que distribuye contenido a los usuarios finales con baja latencia y altas velocidades de transferencia.

VPC: "Redes - como si me creo una red privada en mi ordenador". Amazon Virtual Private Cloud (VPC) permite a los usuarios crear redes virtuales aisladas dentro de la nube de AWS, proporcionando control sobre el entorno de red, incluyendo la selección de rangos de IP, subredes y configuraciones de enrutamiento.
10.0.0.0/16 5 IPS reservadas, en cada red. 256-> 251 IPS disponibles. /16-/28

IAM: "Usuarios y permisos - como si me creo un usuario en mi ordenador". AWS Identity and Access Management (IAM) permite a los usuarios gestionar el acceso a los servicios y recursos de AWS de manera segura, mediante la creación de usuarios, grupos y políticas de permisos.

CloudWatch: "Monitorización - como si me creo un monitor de recursos en mi ordenador". Amazon CloudWatch es un servicio de monitoreo y observabilidad que proporciona datos y conocimientos sobre los recursos de AWS, aplicaciones y servicios, permitiendo a los usuarios recopilar y rastrear métricas, logs y eventos.

CloudTrail: """"LOGS"""" -Auditoría - como si me creo un registro de auditoría en mi ordenador". AWS CloudTrail es un servicio que permite a los usuarios registrar y supervisar la actividad de la cuenta de AWS, proporcionando un historial de eventos y acciones realizadas en los recursos de AWS para fines de auditoría y cumplimiento.

EC2 Autoscaling: "Escalado automático - como si me creo un script que se ejecuta en la nube y me duplica los servidores o me los para". Amazon EC2 Auto Scaling es un servicio que permite a los usuarios ajustar automáticamente la capacidad de sus instancias EC2 en función de la demanda, asegurando un rendimiento óptimo y costos eficientes.

Para crear una Well-Architected Application, se deben tener en cuenta los siguientes pilares:

- EC2 + EC2 Autoscaling: Para garantizar que la aplicación pueda escalar automáticamente según la demanda, utilizando instancias EC2 y el servicio de Auto Scaling.
Aproximación de recursos Hardware. (Hay que medir rendimiento en DOcker o de los procesos en uso. + el SO de AMI (Amazon Machine Image)). CUIDADO con la BBDD, hay que tomar decisiones de escalado y replicación. (RDS, Aurora, DynamoDB, etc.) o entorno local.

Desarrollo Local - Preproducción - Producción: Se recomienda tener un entorno de desarrollo local para pruebas y desarrollo, un entorno de preproducción para pruebas más cercanas a la producción, y un entorno de producción para el despliegue final de la aplicación.

Elastic Load Balancing (ELB): "Balanceador de carga". Elastic Load Balancing (ELB) es un servicio que permite distribuir el tráfico entrante de manera eficiente entre las instancias EC2, asegurando alta disponibilidad y rendimiento.

Route 53: "DNS". Amazon Route 53 es un servicio de sistema de nombres de dominio (DNS) que proporciona una forma confiable y escalable de dirigir el tráfico de los usuarios a aplicaciones y servicios en la nube.

Suponga que todo falla. Luego, diseñe en sentido inverso. --> PLAN DE CONTINGENCIA. Diseñar la arquitectura de la aplicación teniendo en cuenta posibles fallos y cómo se recuperará de ellos, implementando estrategias de respaldo, replicación y recuperación ante desastres.

BBDD relacionales escalado vertical fácil muy difícil escalado horizontal. BBDD no relacionales escalado horizontal fácil muy difícil escalado vertical. (NoSQL, DynamoDB, MongoDB, etc.) NO es Ctrl+C Ctrl+V. 

ACL: "Listas de control de acceso". Access Control Lists (ACLs) son mecanismos de seguridad que permiten a los usuarios definir reglas de acceso a recursos específicos, controlando quién puede acceder y qué acciones pueden realizar.

Grupos de seguridad: "Firewall". Los grupos de seguridad son conjuntos de reglas de firewall que controlan el tráfico entrante y saliente hacia las instancias EC2, proporcionando una capa adicional de seguridad.

