# mini project - text emoticons ko emoji me badlo
message = input("Enter message: ")
words = message.split()  # string ko list of words me toddo

# dictionary me emoticon:emoji pairs
emojis = {
    ":)": "😊",
    ":(": "😢",
    ":D": "😁",
    "<3": "❤️"
}

output = ""
for word in words:
    # get() - agar word dict me hai to emoji, warna word waise hi
    output += emojis.get(word, word) + " "

print(output)
