Clase 11: Animaciones + Transiciones + V0 chat vercel
#####################################################
Transicion:hover
"cuando pasas el cursor por encima"

ejemplo
button { transition: box-shadow 500ms ease; }

button:hover{ box-shadow: 0 8px 20px black; }

transiciones
alt text

transform:
translate(x,y) -> mueve el elemento en el eje X o Y
scale(x,y) -> agranda o achica un elemento
rotate(deg) -> rota el elemento segun los grados indicados
skew(x,y) -> inclina el elemento
transiciones + transform
button { transition: transform 500ms ease; }

button:hover{ transform: scale(1.2) rotate(10deg); }

animaciones
"como una transicion pero no hace falta posicionar el cursor encima"

se definen a traves de fotogramas claves (@keyframes)
@keyframe blink{ 0% { opacity: 1 } 50% { opacity: 0 } 100% { opacity: 1 } }

.blink { font-size: 24px; font-weigth: bold; animation: blink 1s infinite; }

ejemplo spiner
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

.spinner { width: 50px; height: 50px; border: 6px solid #ddd; border-top: 6px solid #3498db; border-radius: 50%; animation: spin 1s linear infinite; }