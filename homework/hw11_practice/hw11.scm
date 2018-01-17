(define (find s predicate)
  (if (null? s)
    #f
    (if (predicate (car s))
      (car s)
      (find (cdr-stream s) predicate)
    )
  )
)

(define (scale-stream s k)
  (if (null? s)
    nil
    (cons-stream
      (* (car s) k)
      (scale-stream (cdr-stream s) k)
    )
  )
)

(define (has-cycle s)
  (define (helper origS newS)
    (cond
      [(null? newS) #f]
      [(eq? origS (cdr-stream newS)) #t]
      ; [else (helper origS (cdr-stream newS))]
      [else (helper origS (cdr-stream newS))]
    )
  ) 
  (helper s s)
)

