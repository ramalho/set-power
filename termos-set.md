# Glosario: Conjuntos en Python

Inglés / Portugués / Español — definiciones en español.

---

## dictionary view

**Inglés:** dictionary view | **Portugués:** view de dicionário | **Español:** vista de diccionario

Objeto devuelto por `.keys()`, `.values()` o `.items()` de un `dict`.
Las vistas `dict_keys` y `dict_items` implementan los operadores y métodos más útiles de `frozenset`,
permitiendo operaciones de conjuntos directamente sobre las claves e ítems del diccionario.

---

## difference / relative complement

**Inglés:** difference / relative complement | **Portugués:** diferença / complemento relativo | **Español:** diferencia / complemento relativo

Operación que devuelve los elementos del primer conjunto que no están en el segundo.
Operador infijo `-`; método `s.difference(it, …)`.
Notación matemática: `S \ Z`.

---

## disjoint sets

**Inglés:** disjoint sets | **Portugués:** conjuntos disjuntos | **Español:** conjuntos disjuntos

Dos conjuntos son disjuntos cuando no tienen ningún elemento en común,
es decir, su intersección es vacía (`S ∩ Z = ∅`).
Se verifica con `s.isdisjoint(z)`.

---

## element / member

**Inglés:** element / member | **Portugués:** elemento / membro | **Español:** elemento / miembro

Objeto perteneciente a un conjunto. Debe ser *hashable*.
La pertenencia se verifica con el operador `in`: `e in s`.
Símbolo matemático: `e ∈ S`.

---

## `frozenset`

**Inglés:** frozenset | **Portugués:** frozenset | **Español:** frozenset

Variante inmutable del tipo `set`.
Al ser inmutable, es *hashable* y puede usarse como elemento de un `set` o como clave de un `dict`.
No tiene sintaxis literal propia; se crea siempre con el constructor:
`frozenset(range(10))`.

---

## hash code

**Inglés:** hash code | **Portugués:** código de hash | **Español:** código de hash

Valor numérico derivado del contenido de un objeto,
usado internamente en la tabla de hash para localizar elementos de forma eficiente.
Objetos iguales deben tener el mismo código de hash.

---

## hash table

**Inglés:** hash table | **Portugués:** tabela de hash | **Español:** tabla de hash

Estructura de datos que permite localizar elementos en tiempo prácticamente constante.
Es la base interna de los tipos `set`, `frozenset` y `dict` en Python,
y explica su alto rendimiento en pruebas de pertenencia.

---

## hashable

**Inglés:** hashable | **Portugués:** hashable | **Español:** hashable

Propiedad de un objeto que posee un código de hash
invariable durante su ciclo de vida y
implementa `__hash__()` y `__eq__()`.
Solo objetos *hashable* pueden ser elementos de un `set` o `frozenset`, o claves de un `dict`.

---

## immutable

**Inglés:** immutable | **Portugués:** imutável | **Español:** inmutable

Propiedad de un objeto cuyo estado y contenido no puede cambiar tras su creación.
El tipo `frozenset` es inmutable y *hashable*,
lo que permite usarlo como elemento de un `set`.

---

## infix operator

**Inglés:** infix operator | **Portugués:** operador infixo | **Español:** operador infijo

Operador escrito entre sus dos operandos.
Los operadores de conjuntos `|`, `&`, `-` y `^` son infijos y
exigen que ambos operandos sean conjuntos,
a diferencia de los métodos correspondientes,
que aceptan uno o más argumentos iterables, como en `s.union(it1, it2, …)`

---

## intersection

**Inglés:** intersection | **Portugués:** interseção | **Español:** intersección

Operación que devuelve solo los elementos comunes a ambos conjuntos.
Operador infijo `&`; también disponible como `s.intersection(it, …)`.
Símbolo matemático: `S ∩ Z`.

---

## mutable

**Inglés:** mutable | **Portugués:** mutável | **Español:** mutable

Propiedad de un objeto cuyo estado puede modificarse después de su creación.
El tipo `set` es mutable: admite `add()`, `discard()`, `pop()`, `remove()`, etc.

---

## proper subset

**Inglés:** proper subset | **Portugués:** subconjunto próprio | **Español:** subconjunto propio

Subconjunto estrictamente contenido en otro, es decir,
que es subconjunto pero no igual al conjunto contenedor.
Operador `<` en Python. Símbolo matemático: `S ⊂ Z`.

---

## proper superset

**Inglés:** proper superset | **Portugués:** superconjunto próprio | **Español:** superconjunto propio

Superconjunto estrictamente mayor que el conjunto contenido,
es decir, que lo incluye pero no es igual a él.
Operador `>` en Python. Símbolo matemático: `S ⊃ Z`.

---

## salt

**Inglés:** salt | **Portugués:** sal | **Español:** sal

Valor aleatorio incorporado al cálculo del hash de cadenas por razones de seguridad.
Hace que el orden de iteración de los elementos de un
`set` varíe entre distintos procesos Python.

---

## `set`

**Inglés:** set | **Portugués:** conjunto | **Español:** conjunto

Colección de objetos únicos en Python.
Implementado como tipo incorporado,
garantiza que no haya elementos repetidos y soporta
las principales operaciones de la teoría de conjuntos
mediante operadores infijos y métodos.

---

## set comprehension

**Inglés:** set comprehension | **Portugués:** compreensão de conjunto | **Español:** comprensión de conjunto

Sintaxis concisa para construir un conjunto a partir de un iterable,
con filtros opcionales.
Ejemplo: `{chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}`.

---

## set literal

**Inglés:** set literal | **Portugués:** literal de set | **Español:** literal de conjunto

Sintaxis con llaves para construir un conjunto directamente en el código: `{1, 2, 3}`.
El conjunto vacío no tiene literal; debe usarse `set()`.
El tipo `frozenset` tampoco tiene literal propio.

---

## set theory

**Inglés:** set theory | **Portugués:** teoria dos conjuntos | **Español:** teoría de conjuntos

Rama de las matemáticas que estudia colecciones de objetos.
Python implementa sus operaciones fundamentales (unión, intersección, diferencia, etc.)
directamente en los tipos `set` y `frozenset`.

---

## setcomp

**Inglés:** setcomp | **Portugués:** setcomp | **Español:** (ND)

Abreviatura informal de *set comprehension*, usada en la comunidad Python.
No tiene abreviatura equivalente en español.

---

## subset

**Inglés:** subset | **Portugués:** subconjunto | **Español:** subconjunto

Conjunto cuyos elementos están todos contenidos en otro conjunto.
Operador `<=` en Python; método `s.issubset(it)`.
Símbolo matemático: `S ⊆ Z`.

---

## superset

**Inglés:** superset | **Portugués:** superconjunto | **Español:** superconjunto

Conjunto que contiene todos los elementos de otro conjunto.
Operador `>=` en Python; método `s.issuperset(it)`.
Símbolo matemático: `S ⊇ Z`.

---

## symmetric difference

**Inglés:** symmetric difference | **Portugués:** diferença simétrica | **Español:** diferencia simétrica

Operación que devuelve los elementos presentes en uno u otro conjunto, pero no en ambos.
Es el complemento de la intersección.
Operador infijo `^`; método `s.symmetric_difference(it)`.
Símbolo matemático: `S ∆ Z`.

---

## union

**Inglés:** union | **Portugués:** união | **Español:** unión

Operación que devuelve todos los elementos presentes en al menos uno de los conjuntos.
Operador infijo `|` en Python; también disponible como método `s.union(it, …)`.
Símbolo matemático: `S ∪ Z`.
