# Shivani
# **Assignment - 3**

def input_chats():
    n = int(input("Enter the number of messages: "))
    chats = {}
    for i in range(n):
        name, chat = input().split(":", 1)
        name = name.strip()
        chat = chat.strip()
        if name in chats:
            chats[name].append(chat)
        else:
            chats[name] = [chat]
    return chats

def show_options():
    options = [
        "Exit",
        "Count total number of messages",
        "Identify unique users in the chat",
        "Count total words in the chat",
        "Calculate average words per message",
        "Find the longest message sent",
        "Find the most active user",
        "Get message count for a specific user",
        "Find the most frequently used word by a specific user",
        "Retrieve the first and last message sent by a user",
        "Check if a user is present in the chat",
        "Find commonly repeated words",
        "Identify the user with the longest average message length",
        "Count how many messages mention a specific user",
        "Remove duplicate messages",
        "Sort messages alphabetically",
        "Extract all questions asked in the chat",
        "Calculate the reply ratio between two users",
        "Check for deleted messages"
    ]
    print("===" * 15)
    print("Options:")
    for i in range(len(options)):
        print(f"{i}. {options[i]}")
    print("===" * 15)

def count_total_messages(chats):
    total = 0
    for user in chats:
        for _ in chats[user]:
            total += 1
    return total

def unique_users(chats):
    count = 0
    users = []
    for user in chats:
        count += 1
        users.append(user)
    return f"{count} users:\n{users}"

def total_words(chats):
    total = 0
    for user in chats:
        for message in chats[user]:
            words = message.split()
            for _ in words:
                total += 1
    return total

def average_words_per_message(chats):
    word_count = 0
    msg_count = 0
    for user in chats:
        for msg in chats[user]:
            word_count += len(msg.split())
            msg_count += 1
    if msg_count == 0:
        return 0
    return word_count / msg_count

def longest_message(chats):
    max_msg = ""
    for user in chats:
        for msg in chats[user]:
            if len(msg) > len(max_msg):
                max_msg = msg
    return max_msg

def most_active_user(chats):
    max_msgs = 0
    active_user = ""
    for user in chats:
        if len(chats[user]) > max_msgs:
            max_msgs = len(chats[user])
            active_user = user
    return active_user

def msg_count_for_user(chats):
    user = input("Enter user name: ")
    if user in chats:
        return len(chats[user])
    return "User not found."

def most_used_word_by_user(chats):
    user = input("Enter user name: ")
    if user in chats:
        word_freq = {}
        for msg in chats[user]:
            words = msg.split()
            for word in words:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
        max_word = ""
        max_count = 0
        for word in word_freq:
            if word_freq[word] > max_count:
                max_count = word_freq[word]
                max_word = word
        return max_word
    return "User not found."

def first_last_msg(chats):
    user = input("Enter user name: ")
    if user in chats:
        return f"First: {chats[user][0]}, Last: {chats[user][-1]}"
    return "User not found."

def check_user_exists(chats):
    user = input("Enter user name: ")
    if user in chats:
        return "User found."
    return "User not found."

def common_words(chats):
    word_freq = {}
    for user in chats:
        for msg in chats[user]:
            words = msg.split()
            for word in words:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
    print("Repeated words:")
    for word in word_freq:
        if word_freq[word] > 1:
            print(word, end=" ")

def longest_avg_msg(chats):
    max_avg = 0
    user_result = ""
    for user in chats:
        total_length = 0
        count = 0
        for msg in chats[user]:
            total_length += len(msg)
            count += 1
        if count > 0:
            avg = total_length / count
            if avg > max_avg:
                max_avg = avg
                user_result = user
    return user_result

def count_mentions(chats):
    user = input("Enter user name: ")
    count = 0
    for sender in chats:
        for msg in chats[sender]:
            if user in msg:
                count += 1
    return f"Messages mentioning {user}: {count}"

def remove_duplicates(chats):
    for user in chats:
        unique_msgs = []
        for msg in chats[user]:
            if msg not in unique_msgs:
                unique_msgs.append(msg)
        chats[user] = unique_msgs
    return "Duplicates removed."

def sort_messages(chats):
    all_msgs = []
    for user in chats:
        for msg in chats[user]:
            all_msgs.append(msg)
    all_msgs.sort()
    return all_msgs

def extract_questions(chats):
    questions = []
    for user in chats:
        for msg in chats[user]:
            if "?" in msg:
                questions.append(msg)
    return questions

def reply_ratio(chats):
    a, b = input("Enter two usernames (A and B): ").split(" and ")
    count = 0
    if b in chats:
        for msg in chats[b]:
            if a in msg:
                count += 1
    return f"Reply ratio from {b} to {a} is {count}"

def check_deleted_msgs(chats):
    deleted = 0
    for user in chats:
        for msg in chats[user]:
            if "deleted" in msg.lower():
                deleted += 1
    return f"Deleted messages count: {deleted}"


# Main program
chats = input_chats()

while True:
    show_options()
    choice = int(input("Enter your choice: "))
    if choice == 0:
        break
    elif choice == 1:
        print("Total messages:", count_total_messages(chats))
    elif choice == 2:
        print(unique_users(chats))
    elif choice == 3:
        print("Total words:", total_words(chats))
    elif choice == 4:
        print("Average words per message:", average_words_per_message(chats))
    elif choice == 5:
        print("Longest message:", longest_message(chats))
    elif choice == 6:
        print("Most active user:", most_active_user(chats))
    elif choice == 7:
        print("Message count for user:", msg_count_for_user(chats))
    elif choice == 8:
        print("Most used word by user:", most_used_word_by_user(chats))
    elif choice == 9:
        print(first_last_msg(chats))
    elif choice == 10:
        print(check_user_exists(chats))
    elif choice == 11:
        common_words(chats)
    elif choice == 12:
        print("User with longest average message:", longest_avg_msg(chats))
    elif choice == 13:
        print(count_mentions(chats))
    elif choice == 14:
        print(remove_duplicates(chats))
    elif choice == 15:
        print("Sorted messages:", sort_messages(chats))
    elif choice == 16:
        print("Questions in chat:", extract_questions(chats))
    elif choice == 17:
        print(reply_ratio(chats))
    elif choice == 18:
        print(check_deleted_msgs(chats))
    else:
        print("Invalid choice.")
