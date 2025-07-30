
bangla = float(input("Enter marks for Bangla: "))
english = float(input("Enter marks for English: "))
math = float(input("Enter marks for Math: "))


average = (bangla + english + math) / 3


if bangla >= 40 and english >= 40 and math >= 40:
    print("✅ PASSED all subjects.")
    print(f"🎯 Average Marks: {average:.2f}")


    if average >= 90:
        print("🎓 Grade: A+")
    elif average >= 80:
        print("🎓 Grade: A")
    elif average >= 70:
        print("🎓 Grade: B")
    elif average >= 60:
        print("🎓 Grade: C")
    elif average >= 50:
        print("🎓 Grade: D")
    else:
        print("🎓 Grade: E")
else:
    print("❌ FAILED in one or more subjects.")
    print(f"🎯 Average Marks: {average:.2f}")
    print("🎓 Grade: F")
