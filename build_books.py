"""
build_books.py — Generates all 10 Christian homeschool activity books as PDFs.
Run: python3 build_books.py
Output: books/*.pdf
"""

import os
from workbook import (
    Workbook, NAVY, GOLD, TEAL, CORAL, SKY, GREEN, PURPLE,
    icon_star, icon_heart, icon_fish, icon_sheep, icon_leaf, icon_dove,
    scene_ark, scene_creation, scene_shepherd, scene_praying, scene_cross_hill,
)

OUT = "books"
os.makedirs(OUT, exist_ok=True)


def finalize(wb, filename):
    """Rebuild TOC page-numbers by counting actual pages is complex;
    we instead record TOC entries as we add sections. Save file."""
    path = os.path.join(OUT, filename)
    wb.save(path)
    return path


def heart_pts(cx, cy, scale):
    """Return dot-to-dot points forming a heart outline."""
    import math
    pts = []
    for i in range(16):
        t = math.pi * 2 * i / 16
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        pts.append((cx + x * scale, cy + y * scale))
    return pts


def fish_pts(cx, cy, s):
    return [
        (cx - 3 * s, cy), (cx - 1.5 * s, cy + s), (cx + s, cy + 1.1 * s),
        (cx + 2.2 * s, cy + 0.4 * s), (cx + 2.2 * s, cy - 0.4 * s),
        (cx + s, cy - 1.1 * s), (cx - 1.5 * s, cy - s), (cx - 3 * s, cy),
        (cx - 3.8 * s, cy + 0.9 * s), (cx - 3.8 * s, cy - 0.9 * s),
    ]


# ============================================================
# BOOK 1 — Christian Bible Learning Workbook for Ages 5–8
# ============================================================
def book1():
    wb = Workbook(
        "Christian Bible Learning Workbook",
        "Fun Bible Lessons, Tracing, Coloring & Activities to Grow in Faith",
        "Ages 5–8", accent=NAVY, accent2=GOLD)
    wb.cover()
    wb.welcome(
        ["Welcome to your Bible learning adventure! This workbook helps young children "
         "explore God's Word through hands-on activities that build reading, writing, and faith.",
         "Each page can be printed as many times as you like. Sit beside your child, read the "
         "instructions together, and celebrate every effort. Learning about God should be joyful!"],
        "Train up a child in the way he should go, and when he is old he will not depart from it.",
        "Proverbs 22:6")
    wb.toc = [
        ("God Made Everything — Coloring", 4),
        ("Trace the Bible Words", 5),
        ("Memory Verse: God Is Love", 6),
        ("Match the Bible Friends", 7),
        ("Count God's Creation", 8),
        ("Bible Words Word Search", 9),
        ("Help Noah Find the Ark — Maze", 10),
        ("My Prayer Journal", 11),
    ]
    wb.table_of_contents()
    wb.coloring("Lesson 1", "God Made Everything", "In the beginning God created the heavens and the earth.", scene_creation)
    wb.tracing("Handwriting", "Trace the Bible Words", ["God", "Jesus", "Love", "Pray", "Bible"], "Trace each word, then write it on the dotted line.")
    wb.memory_verse("Verse 1", "God is love.", "1 John 4:8", note="Say it together three times before bed!")
    wb.matching("Think", "Match the Bible Friends", ["Noah", "David", "Jonah", "Moses"], ["Ark", "Sling", "Big Fish", "Ten Rules"], "Draw a line from each person to what they are known for.")
    wb.count_and_write("Numbers", "Count God's Creation", [
        ("How many stars?", 4, icon_star),
        ("How many fish?", 6, icon_fish),
        ("How many sheep?", 3, icon_sheep),
        ("How many leaves?", 5, icon_leaf),
    ], "Count the pictures and write the number in the box.")
    wb.word_search("Puzzle", "Bible Words Word Search", ["GOD", "LOVE", "JESUS", "PRAY", "BIBLE", "FAITH", "HOPE"])
    wb.maze("Puzzle", "Help Noah Reach the Ark", "Lead Noah safely through the maze to the ark!", seed=11)
    wb.journal("Faith", "My Prayer Journal", ["Today I want to thank God for...", "Please help me with..."])
    return finalize(wb, "01_Christian_Bible_Learning_Workbook_Ages_5-8.pdf")


# ============================================================
# BOOK 2 — Bible Stories & Activities Homeschool Workbook
# ============================================================
def book2():
    wb = Workbook(
        "Bible Stories & Activities Homeschool Workbook",
        "Read a Story, Then Play, Draw, and Learn — A Full Homeschool Companion",
        "Ages 6–10", accent=TEAL, accent2=GOLD)
    wb.cover()
    wb.welcome(
        ["This homeschool workbook pairs beloved Bible stories with activities that reinforce "
         "reading comprehension, vocabulary, and character lessons.",
         "Read the short story on each lesson page aloud, then complete the matching activity. "
         "It's a complete, faith-centered supplement for your school day."],
        "Thy word is a lamp unto my feet, and a light unto my path.",
        "Psalm 119:105")
    wb.toc = [
        ("Story: Noah's Ark — Coloring", 4),
        ("Noah Comprehension: True or False", 5),
        ("Story: David & Goliath — Word Search", 6),
        ("Memory Verse: Be Strong & Courageous", 7),
        ("Match the Story to the Lesson", 8),
        ("Fill the Blank: Bible Stories", 9),
        ("Jonah and the Big Fish — Maze", 10),
        ("Retell the Story Journal", 11),
    ]
    wb.table_of_contents()
    wb.coloring("Story 1", "Noah's Ark", "God kept Noah, his family, and the animals safe.", scene_ark)
    wb.true_false("Reading", "Noah — True or False?", [
        "Noah built a big boat called an ark.",
        "It rained for forty days and forty nights.",
        "Noah brought only one animal on the ark.",
        "God put a rainbow in the sky as a promise.",
    ], "Read each sentence. Circle True or False.")
    wb.word_search("Story 2", "David & Goliath", ["DAVID", "GIANT", "STONE", "SLING", "BRAVE", "SHEEP", "KING"])
    wb.memory_verse("Verse", "Be strong and courageous. Do not be afraid; for the Lord your God is with you.", "Joshua 1:9")
    wb.matching("Think", "Match Story to Lesson", ["Noah", "David", "Jonah", "Good Samaritan"], ["Obey God", "Be brave", "Say sorry", "Be kind"], "Draw a line from each story to the lesson it teaches.")
    wb.fill_blank("Words", "Fill in the Blank", [
        ("Noah built an", "ark", "to obey God."),
        ("David trusted God to defeat the", "giant", "."),
        ("Jonah was swallowed by a big", "fish", "."),
        ("Jesus taught us to", "love", "one another."),
    ], "Use the Word Bank to finish each sentence.", word_bank=["ark", "giant", "fish", "love"])
    wb.maze("Puzzle", "Jonah and the Big Fish", "Help Jonah find his way to dry land!", seed=22)
    wb.journal("Write", "Retell the Story", ["Which Bible story is your favorite, and why?", "What did the story teach you about God?"])
    return finalize(wb, "02_Bible_Stories_and_Activities_Homeschool_Workbook.pdf")


# ============================================================
# BOOK 3 — Faith, Kindness & Courage Christian Activity Book
# ============================================================
def book3():
    wb = Workbook(
        "Faith, Kindness & Courage",
        "A Christian Activity Book About Being Brave, Loving, and Trusting God",
        "Ages 6–9", accent=CORAL, accent2=NAVY)
    wb.cover()
    wb.welcome(
        ["Faith, kindness, and courage are three gifts God helps us grow. This activity book "
         "explores each one through verses, puzzles, and reflection.",
         "Encourage your child to notice ways they can show these virtues every day at home, "
         "at church, and with friends."],
        "Let all that you do be done in love.",
        "1 Corinthians 16:14")
    wb.toc = [
        ("What Is Faith? — Coloring", 4),
        ("Faith Memory Verse", 5),
        ("Acts of Kindness Word Search", 6),
        ("Kind or Unkind? True or False", 7),
        ("Courage Match-Up", 8),
        ("Trace: Brave Faith Words", 9),
        ("Be Brave Maze", 10),
        ("My Kindness Journal", 11),
    ]
    wb.table_of_contents()
    wb.coloring("Faith", "What Is Faith?", "Faith means trusting God even when we cannot see.", scene_cross_hill)
    wb.memory_verse("Faith", "Now faith is the substance of things hoped for, the evidence of things not seen.", "Hebrews 11:1")
    wb.word_search("Kindness", "Acts of Kindness", ["SHARE", "HELP", "SMILE", "GIVE", "CARE", "HUG", "LISTEN"])
    wb.true_false("Kindness", "Kind or Unkind?", [
        "Sharing your toys is a kind thing to do.",
        "Saying mean words helps a friend feel loved.",
        "Helping mom clean up shows kindness.",
        "Forgiving someone is showing God's love.",
    ], "Read each sentence. Circle True if it is kind and loving.")
    wb.matching("Courage", "Courage Match-Up", ["David", "Daniel", "Esther", "Joshua"], ["Faced a giant", "Trusted in the lions' den", "Spoke up for others", "Marched to Jericho"], "Match each brave hero to their courageous act.")
    wb.tracing("Handwriting", "Trace Brave Faith Words", ["Brave", "Trust", "Kind", "Faith"], "Trace each word and write it below.")
    wb.maze("Courage", "Be Brave!", "Courage helps you finish hard things. Solve the maze!", seed=33)
    wb.journal("Kindness", "My Kindness Journal", ["One kind thing I can do today is...", "Someone I want to show God's love to is..."])
    return finalize(wb, "03_Faith_Kindness_and_Courage_Christian_Activity_Book.pdf")


# ============================================================
# BOOK 4 — My First Bible Learning Activity Workbook
# ============================================================
def book4():
    wb = Workbook(
        "My First Bible Learning Activity Workbook",
        "Gentle First Activities: Colors, Shapes, Letters & Simple Bible Truths",
        "Ages 3–6", accent=SKY, accent2=CORAL)
    wb.cover()
    wb.welcome(
        ["Made for the youngest learners, this first workbook keeps activities simple, big, and "
         "friendly. Little hands will trace, count, and color while hearing about God's love.",
         "Keep sessions short and full of praise. Every scribble is a step toward learning!"],
        "Let the little children come to me.",
        "Matthew 19:14")
    wb.toc = [
        ("God Loves Me — Coloring", 4),
        ("Trace My First Bible Words", 5),
        ("Count the Animals", 6),
        ("Big Memory Verse: Jesus Loves Me", 7),
        ("Match the Shapes", 8),
        ("Connect the Dots: A Fish", 9),
        ("Find the Way to Church — Maze", 10),
        ("I Can Draw for God", 11),
    ]
    wb.table_of_contents()
    wb.coloring("Hello", "God Loves Me", "God made me and God loves me!", scene_shepherd)
    wb.tracing("Trace", "My First Bible Words", ["God", "Love", "Pray"], "Trace the big letters with your finger, then a crayon.")
    wb.count_and_write("Count", "Count the Animals", [
        ("Count the sheep", 3, icon_sheep),
        ("Count the fish", 4, icon_fish),
        ("Count the doves", 2, icon_dove),
    ], "Count the animals God made. Write how many.")
    wb.memory_verse("Sing", "Jesus loves me, this I know, for the Bible tells me so.", "A Children's Song")
    wb.matching("Match", "Match the Shapes", ["Circle", "Square", "Triangle", "Heart"], ["Sun", "Window", "Roof", "Love"], "Draw a line to match each shape to a picture.")
    wb.dot_to_dot("Draw", "Connect the Dots: A Fish", "Connect 1 to 10 to make a fish, like the ones Jesus' friends caught!", fish_pts(306, 430, 26))
    wb.maze("Go", "Find the Way to Church", "Help the family walk to church. Follow the path!", cols=7, rows=9, seed=44)
    wb.journal("Create", "I Can Draw for God", ["Draw something God made that you love."], draw_box=True)
    return finalize(wb, "04_My_First_Bible_Learning_Activity_Workbook.pdf")


# ============================================================
# BOOK 5 — Christian Character Building Activity Book
# ============================================================
def book5():
    wb = Workbook(
        "Christian Character Building Activity Book",
        "Growing the Fruit of the Spirit: Patience, Honesty, Self-Control & More",
        "Ages 7–11", accent=PURPLE, accent2=GOLD)
    wb.cover()
    wb.welcome(
        ["Godly character grows one choice at a time. This activity book focuses on the Fruit of "
         "the Spirit and other virtues, helping children connect faith to daily behavior.",
         "Use the journaling pages as conversation starters at dinner or bedtime."],
        "The fruit of the Spirit is love, joy, peace, patience, kindness, goodness, faithfulness.",
        "Galatians 5:22–23")
    wb.toc = [
        ("Fruit of the Spirit — Coloring", 4),
        ("Fruit of the Spirit Word Search", 5),
        ("Memory Verse: Kind Words", 6),
        ("Good Choice or Not? True or False", 7),
        ("Match the Virtue", 8),
        ("Fill the Blank: Character", 9),
        ("Patience Maze", 10),
        ("Character Goals Journal", 11),
    ]
    wb.table_of_contents()
    wb.coloring("Grow", "Fruit of the Spirit", "God's Spirit helps good things grow in us.", scene_creation)
    wb.word_search("Puzzle", "Fruit of the Spirit", ["LOVE", "JOY", "PEACE", "PATIENCE", "KINDNESS", "GOODNESS", "GENTLE"])
    wb.memory_verse("Verse", "Let no corrupt word proceed out of your mouth, but what is good for edification.", "Ephesians 4:29")
    wb.true_false("Choices", "Good Choice or Not?", [
        "Telling the truth even when it is hard shows honesty.",
        "Waiting your turn kindly shows patience.",
        "Taking something that is not yours is a good choice.",
        "Staying calm when angry shows self-control.",
    ], "Circle True for choices that build godly character.")
    wb.matching("Think", "Match the Virtue", ["Patience", "Honesty", "Generosity", "Forgiveness"], ["Waiting calmly", "Telling the truth", "Sharing freely", "Letting go of hurt"], "Match each virtue to what it looks like.")
    wb.fill_blank("Words", "Fill in the Blank", [
        ("God wants us to be", "honest", "and tell the truth."),
        ("Being", "patient", "means waiting without complaining."),
        ("We show", "kindness", "by helping others."),
        ("Self-", "control", "helps us make good choices."),
    ], "Complete each sentence using the Word Bank.", word_bank=["honest", "patient", "kindness", "control"])
    wb.maze("Practice", "Patience Maze", "Good things take time. Patiently find the path!", seed=55)
    wb.journal("Goals", "Character Goals", ["A part of my character I want to grow is...", "This week I will practice it by..."])
    return finalize(wb, "05_Christian_Character_Building_Activity_Book.pdf")


# ============================================================
# BOOK 6 — Bible Heroes Learning Workbook for Kids
# ============================================================
def book6():
    wb = Workbook(
        "Bible Heroes Learning Workbook",
        "Meet the Heroes of the Bible and the Great Things God Did Through Them",
        "Ages 6–10", accent=NAVY, accent2=CORAL)
    wb.cover()
    wb.welcome(
        ["From Moses to Mary, the Bible is full of ordinary people who trusted an extraordinary God. "
         "This workbook introduces kids to Bible heroes and the lessons their lives teach.",
         "Read each hero's short bio, then complete the activity to remember their story."],
        "These were all commended for their faith.",
        "Hebrews 11:39")
    wb.toc = [
        ("Bible Heroes — Coloring", 4),
        ("Bible Heroes Word Search", 5),
        ("Match the Hero to the Deed", 6),
        ("Memory Verse: Faith of Heroes", 7),
        ("Fill the Blank: Who Am I?", 8),
        ("Trace the Heroes' Names", 9),
        ("Moses Crosses the Sea — Maze", 10),
        ("My Hero of Faith Journal", 11),
    ]
    wb.table_of_contents()
    wb.coloring("Heroes", "Heroes of the Bible", "God used brave people to do amazing things.", scene_shepherd)
    wb.word_search("Puzzle", "Bible Heroes", ["MOSES", "DAVID", "RUTH", "DANIEL", "ESTHER", "PAUL", "MARY", "NOAH"])
    wb.matching("Think", "Match Hero to Deed", ["Moses", "Daniel", "Esther", "Noah"], ["Parted the sea", "Prayed with lions", "Saved her people", "Built the ark"], "Draw a line from each hero to what God did through them.")
    wb.memory_verse("Verse", "By faith Abraham obeyed when he was called to go out to a place he would receive.", "Hebrews 11:8")
    wb.fill_blank("Who Am I?", "Who Am I?", [
        ("I led God's people out of Egypt. I am", "Moses", "."),
        ("I was brave in the lions' den. I am", "Daniel", "."),
        ("I trusted God and became a queen. I am", "Esther", "."),
        ("I built an ark to obey God. I am", "Noah", "."),
    ], "Read each clue and write the hero's name.", word_bank=["Moses", "Daniel", "Esther", "Noah"])
    wb.tracing("Handwriting", "Trace the Heroes' Names", ["Moses", "David", "Ruth", "Paul"], "Trace each hero's name, then write it.")
    wb.maze("Puzzle", "Moses Crosses the Sea", "Help Moses lead the people safely across!", seed=66)
    wb.journal("Reflect", "My Hero of Faith", ["Which Bible hero do you admire most, and why?", "How can you be brave for God like they were?"])
    return finalize(wb, "06_Bible_Heroes_Learning_Workbook_for_Kids.pdf")


# ============================================================
# BOOK 7 — God's Creation Christian Homeschool Activity Pack
# ============================================================
def book7():
    wb = Workbook(
        "God's Creation Activity Pack",
        "Explore the Wonders of Creation Across Seven Days — A Homeschool Nature & Faith Pack",
        "Ages 5–9", accent=GREEN, accent2=GOLD)
    wb.cover()
    wb.welcome(
        ["God spoke, and the world came to be! This nature-and-faith pack walks through the seven "
         "days of creation while celebrating the beauty of the world around us.",
         "Take some activities outdoors. Point out the sky, plants, and animals as living proof of "
         "God's creativity."],
        "The heavens declare the glory of God; the skies proclaim the work of his hands.",
        "Psalm 19:1")
    wb.toc = [
        ("The Seven Days — Coloring", 4),
        ("Creation Word Search", 5),
        ("Match the Day of Creation", 6),
        ("Memory Verse: In the Beginning", 7),
        ("Count the Creatures", 8),
        ("Fill the Blank: Days of Creation", 9),
        ("Garden of Eden Maze", 10),
        ("Nature Thank-You Journal", 11),
    ]
    wb.table_of_contents()
    wb.coloring("Creation", "The Seven Days", "And God saw everything that he had made, and it was very good.", scene_creation)
    wb.word_search("Puzzle", "Creation", ["LIGHT", "SKY", "LAND", "SUN", "MOON", "FISH", "BIRDS", "PLANTS"])
    wb.matching("Think", "Match the Day", ["Day 1", "Day 4", "Day 5", "Day 6"], ["Light", "Sun & Moon", "Fish & Birds", "Animals & People"], "Match each day of creation to what God made.")
    wb.memory_verse("Verse", "In the beginning God created the heavens and the earth.", "Genesis 1:1")
    wb.count_and_write("Count", "Count the Creatures", [
        ("Count the birds (doves)", 5, icon_dove),
        ("Count the fish", 6, icon_fish),
        ("Count the leaves", 7, icon_leaf),
        ("Count the sheep", 4, icon_sheep),
    ], "God filled the earth with life! Count and write.")
    wb.fill_blank("Words", "Days of Creation", [
        ("On day one God made", "light", "."),
        ("On day four God made the sun and", "moon", "."),
        ("On day five God made fish and", "birds", "."),
        ("On day six God made", "people", "."),
    ], "Finish each sentence with the Word Bank.", word_bank=["light", "moon", "birds", "people"])
    wb.maze("Puzzle", "Garden of Eden Maze", "Find your way through God's beautiful garden!", seed=77)
    wb.journal("Thanks", "Nature Thank-You", ["My favorite thing God created is...", "When I look at creation, I thank God for..."])
    return finalize(wb, "07_Gods_Creation_Christian_Homeschool_Activity_Pack.pdf")


# ============================================================
# BOOK 8 — Prayer, Faith & Gratitude Activity Workbook
# ============================================================
def book8():
    wb = Workbook(
        "Prayer, Faith & Gratitude Activity Workbook",
        "Learning to Talk with God, Trust His Plan, and Give Thanks Every Day",
        "Ages 6–10", accent=TEAL, accent2=CORAL)
    wb.cover()
    wb.welcome(
        ["Prayer is simply talking with God. This workbook helps children build a habit of prayer, "
         "grow their faith, and develop a thankful heart.",
         "The journaling and gratitude pages are wonderful to revisit weekly so kids can see how God "
         "answers and provides over time."],
        "Do not be anxious about anything, but in every situation, by prayer, present your requests to God.",
        "Philippians 4:6")
    wb.toc = [
        ("Talking with God — Coloring", 4),
        ("Learn the Lord's Prayer — Trace", 5),
        ("Prayer & Gratitude Word Search", 6),
        ("Memory Verse: Give Thanks", 7),
        ("Match: Ways to Pray", 8),
        ("My Prayer List Journal", 9),
        ("Gratitude Maze", 10),
        ("Ten Things I'm Thankful For", 11),
    ]
    wb.table_of_contents()
    wb.coloring("Pray", "Talking with God", "God always hears us when we pray.", scene_praying)
    wb.tracing("Trace", "The Lord's Prayer", ["Our Father", "Hallowed", "Kingdom", "Amen"], "Trace these words from the prayer Jesus taught.")
    wb.word_search("Puzzle", "Prayer & Gratitude", ["PRAY", "THANKS", "FAITH", "AMEN", "TRUST", "PRAISE", "BLESS"])
    wb.memory_verse("Verse", "Give thanks to the Lord, for he is good; his love endures forever.", "Psalm 107:1")
    wb.matching("Think", "Ways to Pray", ["Praise", "Thank", "Sorry", "Ask"], ["Tell God He is great", "Say thank you", "Say I'm sorry", "Ask for help"], "Match each part of prayer to what it means.")
    wb.journal("Pray", "My Prayer List", ["People I want to pray for:", "Something I am asking God for:"])
    wb.maze("Puzzle", "Gratitude Maze", "Follow the thankful path all the way through!", seed=88)
    wb.journal("Thanks", "Ten Things I'm Thankful For", ["List or draw the things you are thankful to God for today."], draw_box=True)
    return finalize(wb, "08_Prayer_Faith_and_Gratitude_Activity_Workbook.pdf")


# ============================================================
# BOOK 9 — Bible Memory Verse Practice Workbook for Kids
# ============================================================
def book9():
    wb = Workbook(
        "Bible Memory Verse Practice Workbook",
        "Hide God's Word in Your Heart — Trace, Copy, and Master Key Verses",
        "Ages 6–11", accent=NAVY, accent2=GOLD)
    wb.cover()
    wb.welcome(
        ["Memorizing Scripture gives children truth they can carry for a lifetime. This practice "
         "workbook uses tracing, copying, and fill-in-the-blank to help verses stick.",
         "Aim for one verse per week. Review earlier verses often, and celebrate each one learned!"],
        "I have hidden your word in my heart that I might not sin against you.",
        "Psalm 119:11")
    wb.toc = [
        ("How to Memorize — Coloring", 4),
        ("Verse 1: John 3:16", 5),
        ("Verse 2: Psalm 23:1", 6),
        ("Verse 3: Philippians 4:13", 7),
        ("Verse Fill-in-the-Blank", 8),
        ("Verse Reference Match", 9),
        ("Key Words Word Search", 10),
        ("My Verses I Know Journal", 11),
    ]
    wb.table_of_contents()
    wb.coloring("Learn", "Hide It in Your Heart", "God's Word is a treasure to keep in our hearts.", scene_cross_hill)
    wb.memory_verse("Verse 1", "For God so loved the world that he gave his one and only Son.", "John 3:16")
    wb.memory_verse("Verse 2", "The Lord is my shepherd; I shall not want.", "Psalm 23:1")
    wb.memory_verse("Verse 3", "I can do all things through Christ who strengthens me.", "Philippians 4:13")
    wb.fill_blank("Practice", "Verse Fill-in-the-Blank", [
        ("For God so loved the", "world", "that he gave his Son."),
        ("The Lord is my", "shepherd", "; I shall not want."),
        ("I can do all things through", "Christ", "who strengthens me."),
        ("Trust in the Lord with all your", "heart", "."),
    ], "Fill in the missing word from each verse.", word_bank=["world", "shepherd", "Christ", "heart"])
    wb.matching("Match", "Verse Reference Match", ["God so loved the world", "The Lord is my shepherd", "I can do all things", "Be strong and courageous"], ["John 3:16", "Psalm 23:1", "Philippians 4:13", "Joshua 1:9"], "Match each verse to its reference.")
    wb.word_search("Puzzle", "Key Verse Words", ["LOVED", "WORLD", "SHEPHERD", "CHRIST", "STRONG", "HEART", "TRUST"])
    wb.journal("Track", "Verses I Know", ["Write a verse you have memorized this week:", "A verse I want to learn next is..."])
    return finalize(wb, "09_Bible_Memory_Verse_Practice_Workbook_for_Kids.pdf")


# ============================================================
# BOOK 10 — Christian Preschool & Kindergarten Bible Activity Book
# ============================================================
def book10():
    wb = Workbook(
        "Christian Preschool & Kindergarten Bible Activity Book",
        "Early Learning Fun: Letters, Numbers, Colors & First Bible Truths",
        "Ages 4–6", accent=CORAL, accent2=TEAL)
    wb.cover()
    wb.welcome(
        ["Perfect for preschool and kindergarten, this book blends early learning skills — letters, "
         "numbers, shapes — with simple, joyful Bible truths.",
         "Short, colorful activities keep little learners engaged while planting seeds of faith. "
         "Praise effort over perfection!"],
        "From infancy you have known the Holy Scriptures.",
        "2 Timothy 3:15")
    wb.toc = [
        ("Jesus Loves the Children — Coloring", 4),
        ("Trace the Letters: G is for God", 5),
        ("Count with Noah's Animals", 6),
        ("Big Verse: God Made Me", 7),
        ("Match Uppercase & Pictures", 8),
        ("Connect the Dots: A Heart", 9),
        ("Find the Lost Sheep — Maze", 10),
        ("I Can Draw My Family", 11),
    ]
    wb.table_of_contents()
    wb.coloring("Hello", "Jesus Loves the Children", "Jesus said, 'Let the little children come to me.'", scene_shepherd)
    wb.tracing("Letters", "G is for God", ["Aa", "Gg", "Jj", "Ll"], "Trace the letters. G is for God, J is for Jesus!")
    wb.count_and_write("Numbers", "Count Noah's Animals", [
        ("Count the sheep", 2, icon_sheep),
        ("Count the doves", 3, icon_dove),
        ("Count the fish", 5, icon_fish),
    ], "Two by two! Count the animals and write the number.")
    wb.memory_verse("Verse", "I praise you, for I am fearfully and wonderfully made.", "Psalm 139:14")
    wb.matching("Match", "Match Letters & Pictures", ["G", "J", "H", "S"], ["God", "Jesus", "Heart", "Sheep"], "Match each letter to a picture that starts with it.")
    wb.dot_to_dot("Draw", "Connect the Dots: A Heart", "Connect the dots to make a heart — God loves you!", heart_pts(306, 430, 9))
    wb.maze("Go", "Find the Lost Sheep", "The shepherd looks for the lost sheep. Help him through!", cols=7, rows=9, seed=100)
    wb.journal("Create", "I Can Draw My Family", ["Draw your family. God gave them to you as a gift!"], draw_box=True)
    return finalize(wb, "10_Christian_Preschool_and_Kindergarten_Bible_Activity_Book.pdf")


if __name__ == "__main__":
    builders = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]
    for b in builders:
        path = b()
        size = os.path.getsize(path)
        print(f"[OK] {path}  ({size:,} bytes)")
    print("\nAll books generated in ./books/")
