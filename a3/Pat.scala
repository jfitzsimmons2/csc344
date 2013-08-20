class Pat(position: Int, pattern: String) {
	var pos = position;
	val pat:String = pattern;
	val len = pat.length()
	  
	def peek(): Char = {
		if(pos+1==len) {
		  '$'
		} else {
		  pat.charAt(pos)
		}
	}
	
	def getPrev(): Char = {
	  pat.charAt(pos-1)
	}
	
	def advance():Unit = {
	  pos += 1
	}
	
	def reset() {
	  pos = 0
	}
	
	/*
	 * Parsing functions for the nodes of the tree
	 */
	
	def parseS(): S = {
	  S(parseE(): E, '$')
	}
	
	def parseE(): E = {
	  E(parseT,parseE2)
	}
	
	def parseE2(): E2 = {
	  if (peek()=='|') {
	    advance
	    E2('|',parseE3)
	  } else { 
	    null 
	  }
	}
	
	
	def parseE3(): E3 = {
	  E3(parseT, parseE2)
	}
	
	def parseT(): T = {
	  if (peek==')') null else T(parseF(),parseT2())
	}
	
	def parseT2(): T2 = {
	  if(peek!='|' && peek!=')' && peek!='$') T2(parseF(), parseT2()) else null
	}
	
	def parseF(): F = {
	  F(parseA(),parseF2())
	}
	
	def parseF2(): F2 = {	  
	  if (peek()=='?') F2(parseOpt,parseF2) else null
	}
	
	def parseOpt(): Char = {
	  advance
	  '?'
	}
	
	
	def parseA(): A = {
	  A(parseC,parseA2)
	}
	
	def parseA2(): A2 = {
	  if(peek=='(') {
	    A2(parseL,parseA3)
	  } else null
	}
	
	def parseL(): Char = {
	 advance
	 '(' 
	}
	
	def parseA3(): A3 = {
	  A3(parseE,parseR)
	}
	
	def parseR(): Char = {
	  advance
	  ')'
	}
	
	def parseC(): C = {
	  if(peek.isLetter || peek.isDigit || peek=='.' || peek==' ') {
	    advance
	    C(getPrev)
	  } else null
	}
}

abstract class ParseTree(any: Any)
case class S(e: E, eof: Char) extends ParseTree  {
  def eval():Boolean = {
    this.e.eval() 
  }
}
case class E(t: T, e2: E2) extends ParseTree {
  def eval():Boolean={
      if(t.eval==false) { 
         if (e2==null) false else e2.eval
      } else true
  }
}
case class E2(or: Char, e3: E3) extends ParseTree {
   def eval():Boolean={
     e3.eval
  }
}
case class E3(t: T, e2: E2) extends ParseTree {
    def eval():Boolean={
      if (e2==null) {
        (t.eval)
      } else {
        t.eval || e2.eval
      }
  }
}
case class T(f: F, t2: T2) extends ParseTree {
    def eval():Boolean={
      if(t2==null) {
        f.eval
      } else {
    	f.eval && t2.eval
      }
    }
}
case class T2(f: F, t2: T2) extends ParseTree {
    def eval():Boolean={
      if(this.t2==null) this.f.eval else f.eval && t2.eval
    }
}
case class F(a: A, f2: F2) extends ParseTree {
    def eval():Boolean = {
      if(a.eval==true) {
        true
      } else {
        if (f2==null) {
          false
        } else {
        f2.eval
        }
      }
    }
}
case class F2(quest: Char, f2: F2) extends ParseTree {
    def eval():Boolean={
      if (quest=='?') true else false
    }
}
case class A(c: C, a2: A2) extends ParseTree {
	def eval():Boolean={
	  if (c==null) a2.eval else c.eval  
	}
}
case class A2(open: Char,a3: A3) {
    def eval():Boolean={
      a3.eval
    }
}

case class A3(e: E, close: Char) extends ParseTree {
    def eval():Boolean={
      e.eval 
    }
}
case class C(terminal: Char) extends ParseTree {
    def eval():Boolean={
    if((MyHomework3.str.charAt(MyHomework3.pos)==this.terminal||this.terminal=='.') && MyHomework3.str.charAt(MyHomework3.pos)!='$') {
      MyHomework3.advance
      true 
    } else false
  }
}
case class L(open: Char) extends ParseTree 
case class R(close: Char) extends ParseTree 
case class O(or: Char) extends ParseTree 
case class OPTION(opt: Char) extends ParseTree
 