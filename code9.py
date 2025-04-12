# Подсчет гласных в строке
# Подсчет гласных в строке
vowels = "aeiou"
text = "Hello, World!"
count = sum(1 for char in text.lower() if char in vowels)
print(f"Количество гласных: {count}")
