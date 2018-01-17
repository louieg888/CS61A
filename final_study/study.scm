(define (add-to-all item lst) 
  (define (helper item curr rest)
    (if (null? rest)
      curr
      (helper item 
        (append (list (cons item (car rest))) curr) 
        (cdr rest)
      )  
    ) 
  )
  (helper item '() lst)
)

(define (reverse lst)
  (define (reverse-helper toReverse reversed)
    (if (null? toReverse)
      reversed
      (reverse-helper 
        (cdr toReverse)
        (cons (car toReverse) reversed)
      )
    )
  )
  (reverse-helper lst '())
)

(define (sixty-ones lst)
  (define (helper lst2 count)
    (if (or (null? lst2) (null? (cdr lst2)))
      count
      (if 
        (and 
          (= (car lst2) 6)
          (= (car (cdr lst2)) 1)
        )
        (helper (cdr lst2) (+ 1 count))
        (helper (cdr lst2) count)
      )
             
    )
  )
  (helper lst 0)
)

;(sixty-ones '(4 6 1 6 0 1))
;(sixty-ones '(1 6 1 4 6 1 6 0 1))
;(sixty-ones '(6 1 6 1 4 6 1 6 0 1))

(define (sum-every-other lst)
  (cond 
    ((null? lst) 0)
    ((null? (cdr lst)) (car lst))
    (else (+ (car lst) (sum-every-other (cdr (cdr lst)) ) ) )
  )
)

(define (sublists lst)
  (if (null? lst) 
    (list nil)
    (append 
      (sublists (cdr lst))
      (add-to-all (car lst) (sublists (cdr lst)))
    )
  )
)

; (sublists '(1 2 3))

; STREAMS
(define (odd-stream n)
  (cons-stream n (odd-stream (+ n 2)))
)
