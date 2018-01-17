(define (find s predicate)
  (if (null? s)
    #f
    (if (predicate (car s))
      (car s)
      (find (force (cdr s)) predicate)
    )
  )
)

(define (scale-stream s k)
  (if (null? s)
    nil
    (cons-stream
      (* (car s) k)
      (scale-stream (force (cdr s)) k) 
    )
  )
)

(define (has-cycle s)
  (define (helperMethod originalS newS) 
    (cond
      ((null? originalS) #f)
      ((find newS (lambda (x) (eq? x originalS) )) #t)
      (else (helperMethod (cdr-stream originalS) (cons-stream originalS newS)))
    ) 
  )
  (helperMethod s nil)
)

