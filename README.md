﻿# Multiagentes
Implementación de Simulación 2D con OpenGL y Pygame
Descripción del Problema
El problema planteado consistía en desarrollar un programa que permitiera la visualización y manipulación de triángulos en un espacio 2D utilizando OpenGL y Pygame. Cada triángulo debía someterse a transformaciones geométricas, como rotación, traslación y escalado, y el sistema debía simular la relación entre tres objetos:
Un triángulo que rota sobre su propio eje (Sol).
Un segundo triángulo que rota y orbita alrededor del primero (Tierra).
Un tercer triángulo que orbita alrededor del segundo (Luna).
Solución Técnica
La solución técnica se basó en la implementación de dos clases principales: OpMat para gestionar las transformaciones geométricas y Triángulo para representar las figuras geométricas.
Matriz de Modelado y Transformaciones: Clase OpMat
La clase OpMat fue diseñada para manejar las transformaciones geométricas mediante una matriz de modelado. Esta matriz es utilizada para realizar las siguientes transformaciones:
Traslación: Desplazar el objeto en el espacio bidimensional.
Rotación: Rotar el objeto alrededor de un eje en el plano.
Escalado: Cambiar el tamaño del objeto en el plano.
Se implementaron las siguientes funciones:
translate(tx, ty): Desplaza los puntos en el eje X (tx) y el eje Y (ty).
rotate(angle): Rota los puntos alrededor del origen en función del ángulo en radianes.
scale(sx, sy): Escala los puntos según los factores sx y sy.
Además, la clase permite almacenar y recuperar el estado de la matriz mediante las operaciones push y pop, lo cual es útil para aplicar transformaciones sin alterar el estado global.
Representación Gráfica: Clase Triángulo
La clase Triángulo fue implementada para representar una figura triangular cuyos vértices están definidos en posiciones fijas en el espacio: (-1, -1), (1, -1) y (0, 2). Esta clase utiliza la matriz de modelado proporcionada por OpMat para transformar los vértices del triángulo y luego dibujarlo en la pantalla. El algoritmo de Bresenham fue empleado para dibujar las líneas que conectan los vértices, garantizando una representación visual precisa de los triángulos.
Composición de Transformaciones
El reto más significativo fue aplicar las transformaciones en el orden correcto para lograr el comportamiento deseado:
Rotación y Traslación del Triángulo Tierra (Triángulo 2):
Primero se rota el triángulo en torno al origen (Sol).
Luego se traslada a una posición adecuada para que orbite alrededor del Triángulo 1 (Sol).
Finalmente, se escala el triángulo para que mantenga una proporción adecuada.
Rotación y Traslación del Triángulo Luna (Triángulo 3):
Similar al Triángulo 2, pero este gira alrededor del Triángulo 2 (Tierra), simulando su órbita.
El código principal hace uso de las funciones push y pop para aislar las transformaciones de cada triángulo, lo que garantiza que las operaciones de un triángulo no afecten a los demás.
Conclusión
La solución implementada satisface todos los requisitos del problema. Los triángulos rotan y se trasladan en un espacio bidimensional conforme a las transformaciones geométricas definidas. La combinación de matrices de transformación y el uso de operaciones matriciales permiten un control preciso sobre la posición y orientación de los triángulos, y el algoritmo de Bresenham asegura que los triángulos sean dibujados correctamente.
Observaciones
Durante el desarrollo, fue necesario ajustar el orden de las transformaciones para asegurar que los triángulos orbitaran correctamente unos alrededor de otros. Además, el uso de las funciones push y pop fue crucial para evitar que las transformaciones de un triángulo interfirieran con las de otro.
En resumen, este proyecto logró implementar de manera eficiente un sistema gráfico 2D utilizando OpenGL y Pygame para simular la rotación y traslación de triángulos en un ambiente bidimensional.
