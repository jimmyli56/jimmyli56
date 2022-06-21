fun main(args: Array<String>) {
    val num = 29
    var flag = false
    for (i in 2..num / 2){
        // condition for nnon prime number
        if (num %i == 0) {
            flag = true
            break
        }
    }

    if (!flag)
        println("$num is a prime number.")
    else
        println("$num is no a prime number.")
}