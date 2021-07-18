Promises
======
.then()
async 
generators -  function_name* - yield.
yield helps to temporarily stop the execution.


Event loop
======
V8 engine - Event Loop and the Stack.
SetTimeout callback gets scheduled when the stack is empty. 
Excellent video on Event Loops - https://www.youtube.com/watch?v=8aGhZQkoFbQ

JIT compilation - Learned from: Franziska Hinkelmann
=============
JIT helps in faster JS execution.
Dynamic types makes it hard for the JS comipler to create optimized execution code.
The baseline compiler creates the initial executable code
There is an optimizing compiler which optimize based on the objects that it has seen.
If unseen objects are encountered as funcion arguments, the optimizer fallsback to the initial executable code.
-----------------
