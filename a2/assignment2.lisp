;;; CSC344 Assignment 2
;;; LISP Assignment
;;; Joe Fitzsimmons

(setq p1 '(+ x (* x (- y (/ z 2)))))
(setq p2 '(+ (- z 2) (* x 5)))
(setq p3 '(+ 1 a))
(setq p4 '(+ x (+ x (* x 0))))

(defun addexp (e1 e2) (list '+ e1 e2))
(defun subexp (e1 e2) (list '- e1 e2))
(defun mulexp (e1 e2) (list '* e1 e2))
(defun divexp (e1 e2) (list '/ e1 e2))

(defun deep-subst (old new expr)
  (cond
   ((null expr) 
     nil
   )
   ((listp (car expr))
    (cons (deep-subst old new (car expr)) (deep-subst old new (cdr expr)))
   )
   ((eq old (car expr)) 
    (cons new (deep-subst old new (cdr expr)))
   )
   (T   
    (cons (car expr) (deep-subst old new (cdr expr)))
    )
  )
)

(defun subst-bindings (expr bindinglist)
  (cond   
    ((null bindinglist) 
       expr )
    (T 
       (deep-subst (car (car bindinglist)) (car (cdr (car bindinglist))) 
		(subst-bindings expr (cdr bindinglist))
    ))))
	
(defun simplify-triple(op left-arg right-arg)
  (cond
    ((and (numberp left-arg) (numberp right-arg))
      (eval (list op left-arg right-arg))
    )
    ((and (eq op '+) (eql right-arg 0))
      left-arg
    )
    ((and (eq op '+) (eql left-arg 0))
      right-arg
    )
    ((and (eq op '-) (eql right-arg 0))
      left-arg
    )
    ((and (eq op '-) (eql right-arg left-arg))
      0
    )
    ((and (eq op '*) (eql right-arg 0))
      0
    )
    ((and (eq op '*) (eql left-arg 0))
      0
    )
    ((and (eq op '*) (eql right-arg 1))
      left-arg
    )
    ((and (eq op '*) (eql left-arg 1))
      right-arg
    )
    ((and (eq op '/) (eql left-arg 0))
      0
    )
    ((and (eq op '/) (eql right-arg 1))
      left-arg
    )
    ((and (eq op '/) (eql right-arg left-arg))
      1
    )
;;	((and (listp right-arg) (listp left-arg))
;;		(list op (simplify left-arg) (simplify right-arg))
;;	)
;;	((listp right-arg)
;;
;;		(list op left-arg (simplify right-arg))
;;	)
	(T
		(list op left-arg (simplify right-arg))
	)
  )
)

(defun simplify (exp)
  (cond
    ( (listp exp)
        (simplify-triple (car exp) (simplify (car (cdr exp))) (simplify (car (cdr (cdr exp)))))
	)	
	(T 
        exp)))


(defun evalexp (exp binding-list)
  (simplify (subst-bindings exp binding-list))
)

(defun recursive-list-length (L)
  "A recursive implementation of list-length."
  (if (null L)
      0
    (1+ (recursive-list-length (rest L)))))
