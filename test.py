from Callable import LibraryGate

studentGate = LibraryGate("Student")
studentGate("Junaid", "Student")
studentGate("Bari", "Student")

studentGate("Riyaz", "Student")
studentGate("Ayaan", "Staff")

print(studentGate._count)

#myAccess = LibraryGate()
#myAccess("Junaid", "Staff")

