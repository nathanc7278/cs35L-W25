(defun gps-line()
  (interactive)
  (let ((start (point-min))
	(n (line-number-at-pos))
	(total (count-matches "\n" (point-min) (point-max))))
    (if (= start 1)
	(message "Line %d/%d" n total)
      (save-excursion
	(save-restriction
	  (widen)
	  (message "line %d (narrowed line %d)"
		   (+ n (line-number-at-pos start) -1) n))))))
