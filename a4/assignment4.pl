/* Joe Fitzsimmons || Assignment 4 || CSC344 */
   
type(s,string).
type(a,animal).
type(c,creature).
type(n,npc).
type(p,pc).
type(r,room).

/* Class Hierarchy: parent(X,Y) the parent of X is Y */
parent(creature,object).
parent(animal,creature).
parent(npc,creature).
parent(string,object).
parent(pc,creature).

/* Methods: hasMethod(X,Y) X hasMethod Y. */
/* Room's Methods */
hasMethod(room,addCreature).
hasMethod(room,removeCreature).
hasMethod(room,hasPC).
hasMethod(room,hasSpace).

/* Creature's Methods */
hasMethod(creature,getName).
hasMethod(creature,findNewRoom).
hasMethod(creature,moveRoom).
hasMethod(creature,checkState).
hasMethod(creature,setDesc).
hasMethod(creature,setRoom).
hasMethod(creature,getRoom).
hasMethod(creature,getDesc).
hasMethod(creature,performAction).
hasMethod(creature,forceAction).
hasMethod(creature,glad).
hasMethod(creature,angry).
hasMethod(creature,notifySC).

/* Object's Methods */
hasMethod(object,finalize).
hasMethod(object,getClass).
hasMethod(object,hashCode).
hasMethod(object,wait).
hasMethod(object,toString).
hasMethod(object,compareTo).
hasMethod(object,equals).

/* String's Methods */
hasMethod(string,charAt).
hasMethod(string,endsWith).

/* Return Values */
returns(finalize,void).
returns(getClass,class).
returns(hashCode,int).
returns(wait,void).
returns(toString,string).
returns(compareTo,int).
returns(charAt,char).
returns(endsWith,boolean).
returns(findNewRoom,void).
returns(getName,string).
returns(moveRoom,boolean).
returns(checkState,void).
returns(setDesc,void).
returns(setRoom,void).
returns(getRoom,room).
returns(performAction,void).
returns(forceAction,void).
returns(glad,void).
returns(angry,void).
returns(notifySC,void).
returns(addCreature,void).
returns(removeCreature,boolean).
returns(hasPC,boolean).
returns(hasSpace,boolean).
returns(equals,boolean).

extends(X,Y) :- parent(X,Y).
extends(X,Y) :- parent(X,Z), extends(Z,Y).

check(Type,Method,R) :- type(Type,X), hasMethod(X, Method), returns(Method,R);
					    type(Type,X), extends(X,Y), hasMethod(Y, Method), returns(Method,R).
