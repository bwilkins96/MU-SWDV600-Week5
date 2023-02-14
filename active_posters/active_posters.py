# Prints out the most active users, based on data in a csv file

def main():
    forum_file = open('forum_posters.csv', 'r')
    line = forum_file.readline()

    while line:
        [name, status, posts] = line.split(',')
        posts = int(posts)
        status = status.strip()

        if status == 'A' and posts > 200:
            print(f'{name}: {posts} posts in the last month')
            print(len(name))

        line = forum_file.readline()

    forum_file.close()

main()