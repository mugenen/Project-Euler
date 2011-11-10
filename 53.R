
c <- 0
for(i in 1:100) {
	for(j in 1:i) {
		if(choose(i, j) > 1000000) {
			c <- c + 1
		}
	}
}

c
