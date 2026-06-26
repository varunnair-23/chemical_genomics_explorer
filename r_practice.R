students <- data.frame(
    name = c("Alice", "Ben", "Charlie"),
    quiz1 = c(90, 85, 88),
    quiz2 = c(88, 82, 86),
    quiz3 = c(92, 88, 91)
)

print(students)
print(students$quiz1)
quiz1_average <- mean(students$quiz1)
print(quiz1_average)

print(students[1, ])

print(students["quiz2"])

print(students[2, "quiz3"])

students$average <- rowMeans(students[, c("quiz1", "quiz2", "quiz3")])

print(students)