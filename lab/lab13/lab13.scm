;; Scheme ;;
(define (double x) (* x 2))

(define (compose-all funcs)
  (define (helper x remainingFuncs)
    (if (null? remainingFuncs) 
      x
      (helper ((car remainingFuncs) x) (cdr remainingFuncs))
    )
  )
  (lambda (y) (helper y funcs))
)

(define (deep-map fn s)
  (cond
     ; if s is not a list, then just apply f to s
     [(null? s) s]
     [(not (list? s)) (fn s)]
     [else (cons (deep-map fn (car s)) (deep-map fn (cdr s)))]
  )
)
