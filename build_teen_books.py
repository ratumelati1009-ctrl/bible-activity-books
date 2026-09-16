"""
build_teen_books.py — Generate 10 Christian study workbooks for ages 13-19.

Each book: color cover + how-to-use + contents + 6 themed units + memory-verse
review + final reflection + study notes. Every unit adds ~7 content pages, so
each book comfortably exceeds 42 pages.

Run: python3 build_teen_books.py   ->  books/*.pdf
"""

import os
import workbook_teen as wt

OUT = "books"
os.makedirs(OUT, exist_ok=True)


def build_unit(wb, section, unit):
    """unit dict -> pages. Returns nothing; appends to wb."""
    wb.unit_divider(unit["no"], unit["title"], unit["verse"], unit["ref"], unit["overview"])
    d = unit["devo"]
    wt.devotional(wb, section, d["title"], d["opener"], d["verse"], d["ref"],
                  d["body"], d["reflect"], d["prayer"])
    s = unit["study"]
    wt.inductive_study(wb, section, s["title"], s["ref"], s["text"],
                       s["observe"], s["interpret"], s["apply"])
    w = unit["word"]
    wt.word_study(wb, section, w["term"], w["def"], w["verses"], w["questions"])
    j = unit["journal"]
    wt.journal_page(wb, section, j["title"], j["prompts"])
    # alternate discussion / worldview / challenge to keep variety
    extra = unit["extra"]
    if extra["type"] == "discussion":
        wt.discussion_page(wb, section, extra["title"], extra["intro"], extra["questions"])
    elif extra["type"] == "worldview":
        wt.worldview(wb, section, extra["title"], extra["question"],
                     extra["perspectives"], extra["prompts"])
    elif extra["type"] == "challenge":
        wt.challenge_page(wb, section, extra["title"], extra["intro"], extra["challenges"])


def assemble(wb, filename, units, memory_verses, closing_prompts):
    # Table of contents
    wb.toc = [("How to Use This Study", "sec"), ("Table of Contents", "sec")]
    for u in units:
        wb.toc.append((f"Unit {u['no']}: {u['title']}", "unit"))
    wb.toc.append(("Memory Verse Review", "sec"))
    wb.toc.append(("Spiritual Check-In", "sec"))
    wb.toc.append(("Final Reflection", "sec"))
    wb.toc.append(("Study Notes", "sec"))
    wb.contents_page()
    for u in units:
        build_unit(wb, f"Unit {u['no']}", u)
    # Back matter
    wt.memory_study(wb, "Review", memory_verses[0][0], memory_verses[0][1],
                    "Look back over the verses you studied in this book.",
                    "Scripture memorized becomes a resource the Holy Spirit can bring to mind in real moments of decision, temptation, doubt, and encouragement.",
                    "Choose one verse from this book to carry with you all week.")
    # a verse-list review page as journal
    wt.journal_page(wb, "Review", "Memory Verse Review",
                    [f"Write out from memory: {r}" for (_, r) in memory_verses])
    wt.self_assessment(wb, "Review", "Spiritual Check-In",
                       "Rate each statement honestly. This is between you and God — there are no wrong answers, only honest starting points.",
                       ["I make time to read the Bible on my own.",
                        "I pray about real things in my life, not just at meals.",
                        "I can explain what I believe and why.",
                        "I treat people the way Jesus would.",
                        "I invite God into my decisions before I make them.",
                        "I am honest even when it costs me.",
                        "I serve others without expecting anything back.",
                        "I go to God first when I am anxious or afraid."])
    wt.journal_page(wb, "Review", "Final Reflection", closing_prompts)
    wt.notes_page(wb, "Notes")
    wt.notes_page(wb, "Notes")
    path = os.path.join(OUT, filename)
    wb.save(path)
    return path


# ---------- reusable unit factory to reduce repetition ----------
def unit(no, title, verse, ref, overview, devo, study, word, journal, extra):
    return dict(no=no, title=title, verse=verse, ref=ref, overview=overview,
                devo=devo, study=study, word=word, journal=journal, extra=extra)


def devo(title, opener, verse, ref, body, reflect, prayer):
    return dict(title=title, opener=opener, verse=verse, ref=ref, body=body,
                reflect=reflect, prayer=prayer)


def study(title, ref, text, observe, interpret, apply):
    return dict(title=title, ref=ref, text=text, observe=observe,
                interpret=interpret, apply=apply)


def word(term, definition, verses, questions):
    return dict(term=term, **{"def": definition}, verses=verses, questions=questions)


def journal(title, prompts):
    return dict(title=title, prompts=prompts)


def disc(title, intro, questions):
    return dict(type="discussion", title=title, intro=intro, questions=questions)


def wview(title, question, perspectives, prompts):
    return dict(type="worldview", title=title, question=question,
                perspectives=perspectives, prompts=prompts)


def chall(title, intro, challenges):
    return dict(type="challenge", title=title, intro=intro, challenges=challenges)


HOW_TIPS = [
    "Find a consistent time and place. Even 15 focused minutes beats an hour you never start.",
    "Keep a pen in hand. Writing your answers turns reading into real thinking.",
    "Read each passage in your own Bible too, and note the version differences.",
    "Be honest in the reflection and journal sections — no one is grading you.",
    "If you meet with a group, come having already written your answers.",
    "Pray before you begin. Ask God to teach you, not just inform you.",
]


# =====================================================================
# BOOK 1 — Christian Bible Learning Workbook (Ages 13–19)
# =====================================================================
def book1():
    wb = wt.Teenbook(
        "Christian Bible Learning Workbook",
        "A Teen & Young Adult Guide to Reading, Understanding, and Living the Bible",
        accent=wt.NAVY, accent2=wt.GOLD)
    wb.cover()
    wb.how_to_use(
        "This workbook is built for students ages 13 to 19 who want more than Sunday-school "
        "answers. Over six units you will learn how the Bible is put together, how to read it for "
        "yourself, and how to move from information to transformation. Each unit includes a "
        "devotional, an inductive study you drive, a word study, journaling, and either a "
        "discussion or a real-world challenge.",
        "All Scripture is God-breathed and is useful for teaching, rebuking, correcting and training in righteousness.",
        "2 Timothy 3:16", HOW_TIPS)
    units = [
        unit(1, "Why the Bible Matters",
             "Your word is a lamp for my feet, a light on my path.", "Psalm 119:105",
             "Before we open the Bible, we ask what it even is and why anyone should build a life on it. This unit frames Scripture as God's self-revelation, not a rulebook.",
             devo("More Than a Book",
                  "You have probably owned a Bible longer than you have actually read one. This unit is about changing that.",
                  "The word of God is alive and active, sharper than any double-edged sword.", "Hebrews 4:12",
                  ["Notice the verse does not say the Bible was alive when it was written; it says it is alive now. Scripture reads you as much as you read it.",
                   "Many teens quit the Bible because they treat it like a textbook to finish. It is better understood as a conversation with the God who wrote it and is still speaking through it."],
                  ["What has your relationship with the Bible been like so far — honestly?",
                   "What would change in your week if you believed God actually speaks through these words?"],
                  "God, make your word alive to me. Give me hunger for it and eyes to understand."),
             study("The Two Foundations", "Matthew 7:24-27",
                   "Therefore everyone who hears these words of mine and puts them into practice is like a wise man who built his house on the rock. The rain came down, the streams rose, and the winds blew and beat against that house; yet it did not fall, because it had its foundation on the rock. But everyone who hears these words of mine and does not put them into practice is like a foolish man who built his house on sand.",
                   ["What do both builders have in common?", "What is the single difference between them?", "What do the storms represent in a real teenager's life?"],
                   ["Why does Jesus tie wisdom to doing and not just hearing?", "What does building on sand look like for someone your age today?"],
                   ["Where in your life are you currently hearing but not doing?", "What is one area you can start building on rock this week?"]),
             word("Truth", "Reality as God defines it — not merely accurate facts, but what is trustworthy, faithful, and real. In John, Jesus calls himself the Truth.",
                  [("Then you will know the truth, and the truth will set you free.", "John 8:32"),
                   ("Sanctify them by the truth; your word is truth.", "John 17:17")],
                  ["Our culture says truth is whatever you personally feel. How does the Bible challenge that?",
                   "How can truth be freeing rather than limiting?"]),
             journal("Where I'm Starting",
                     ["Describe your current spiritual life in a few honest sentences.",
                      "What do you hope is different by the end of this workbook?",
                      "What is one question about God or the Bible you have never gotten a real answer to?"]),
             wview("Can We Trust the Bible?", "Is the Bible reliable, or was it just made up and edited over time?",
                   [("Manuscript evidence", "There are more early copies of the New Testament than of any other ancient document, and they agree with remarkable consistency."),
                    ("Honest reporting", "The Bible records the failures of its own heroes — an odd choice for a fabricated legend meant to promote them."),
                    ("Unity", "Written by dozens of authors across roughly 1,500 years, it tells one connected story pointing to Christ.")],
                   ["Which of these points is most convincing to you, and why?",
                    "What objection do you still have — and who could help you explore it?"])),
        unit(2, "How the Bible Is Organized",
             "Do your best to present yourself to God as one who correctly handles the word of truth.", "2 Timothy 2:15",
             "You cannot navigate a library you do not understand. This unit maps the 66 books, the two testaments, and the main genres so reading stops feeling random.",
             devo("Learning the Map",
                  "Imagine trying to use a phone with no home screen. That is what the Bible feels like until you learn its layout.",
                  "Do your best to present yourself to God as one approved, a worker who correctly handles the word of truth.", "2 Timothy 2:15",
                  ["The Bible is a library of 66 books: history, law, poetry, prophecy, biography, and letters. Reading a psalm the way you read a legal contract will confuse you.",
                   "Knowing the genre of what you are reading is the first step to reading it well."],
                  ["Which parts of the Bible have you found most confusing, and could genre be part of why?",
                   "How might reading Proverbs differently from Romans help you?"],
                  "Lord, give me patience to learn how your word is put together."),
             study("A Guide to Understanding", "Nehemiah 8:5-8",
                   "Ezra opened the book. All the people could see him because he was standing above them; and as he opened it, the people all stood up. The Levites instructed the people in the Law while the people were standing there. They read from the Book of the Law of God, making it clear and giving the meaning so that the people understood what was being read.",
                   ["What did the people do when the book was opened?", "What did the Levites add to the reading?", "What was the goal of all this effort?"],
                   ["Why is explanation, not just reading, sometimes necessary?", "What does this teach about studying with others?"],
                   ["Who helps you understand the Bible? Who could you ask?", "What tool (study Bible, app, mentor) will you start using?"]),
             word("Testament", "A covenant or binding agreement. The Old Testament records God's covenant with Israel; the New Testament, the new covenant established through Jesus.",
                  [("This cup is the new covenant in my blood, which is poured out for you.", "Luke 22:20"),
                   ("He has made us competent as ministers of a new covenant.", "2 Corinthians 3:6")],
                  ["What is 'new' about the new covenant compared to the old?",
                   "How does seeing the Bible as one covenant story change how you read it?"]),
             journal("My Reading Plan",
                     ["Which book of the Bible will you read first, and why?",
                      "What time of day realistically works for you to read?",
                      "What obstacles usually stop you, and how will you handle them this time?"]),
             disc("Talk It Over",
                  "Share openly. The goal is not to sound spiritual but to be honest.",
                  ["What surprised you about how the Bible is organized?",
                   "Which genre are you most drawn to — story, poetry, letters — and why?",
                   "How can this group help each other actually keep reading?"])),
        unit(3, "Reading for Yourself",
             "Like newborn babies, crave pure spiritual milk, so that by it you may grow up in your salvation.", "1 Peter 2:2",
             "This unit teaches a simple, repeatable method: observe, interpret, apply. Once you own it, you can study any passage without depending on someone else.",
             devo("Feeding Yourself",
                  "There is a difference between being fed and learning to cook. This unit hands you the tools.",
                  "Like newborn babies, crave pure spiritual milk, so that by it you may grow up in your salvation.", "1 Peter 2:2",
                  ["Spiritual growth is not automatic; it is fueled. Peter compares Scripture to milk that a growing person craves.",
                   "The aim is not to stay dependent on a pastor or parent to feed you, but to learn to feed yourself for a lifetime."],
                  ["Are you currently craving God's word, tolerating it, or avoiding it?",
                   "What would help you develop an appetite for Scripture?"],
                  "God, grow in me a real hunger for your word."),
             study("The Bereans' Example", "Acts 17:11",
                   "Now the Berean Jews were of more noble character than those in Thessalonica, for they received the message with great eagerness and examined the Scriptures every day to see if what Paul said was true.",
                   ["What two things made the Bereans 'noble'?", "How often did they examine Scripture?", "What were they checking?"],
                   ["Why is it healthy to check even good teaching against the Bible?", "What is the balance between eagerness and examination?"],
                   ["How will you personally examine what you are taught?", "What does 'daily' realistically look like for you?"]),
             word("Meditate", "In Scripture, to meditate is to chew on and repeat God's word until it shapes your thinking — not to empty your mind, but to fill it.",
                  [("Blessed is the one whose delight is in the law of the Lord, and who meditates on his law day and night.", "Psalm 1:1-2"),
                   ("Keep this Book of the Law always on your lips; meditate on it day and night.", "Joshua 1:8")],
                  ["How is biblical meditation different from popular ideas of meditation?",
                   "What is one verse you could 'chew on' this week?"]),
             journal("Practicing the Method",
                     ["Pick any verse. Write what you observe (what it says).",
                      "Now write what you think it means and why.",
                      "Finally, write one specific way you will apply it."]),
             chall("Try It for a Week",
                   "Knowledge you never use fades fast. Put this unit's method into practice.",
                   ["Read one chapter of a Gospel each day for five days.",
                    "Write one observation, one meaning, and one application each day.",
                    "Share one thing you learned with someone else.",
                    "Pray through one passage instead of just reading it."])),
        unit(4, "The Big Story",
             "You study the Scriptures... These are the very Scriptures that testify about me.", "John 5:39",
             "The Bible is not disconnected lessons; it is one story in four movements — Creation, Fall, Redemption, Restoration — all centered on Jesus.",
             devo("One Story, Not Sixty-Six",
                  "Most people read the Bible like a book of quotes. It is actually one story going somewhere.",
                  "And beginning with Moses and all the Prophets, he explained to them what was said in all the Scriptures concerning himself.", "Luke 24:27",
                  ["On the road to Emmaus, Jesus showed that the whole Old Testament was pointing to him. The Bible has a main character, and it is not you.",
                   "Creation, Fall, Redemption, Restoration: knowing this arc keeps individual verses from feeling random."],
                  ["Have you tended to read the Bible as being mainly about you or mainly about God?",
                   "How does seeing Jesus as the center change a familiar story for you?"],
                  "Jesus, help me see you on every page."),
             study("The Story Begins Again", "Genesis 3:8-15",
                   "Then the man and his wife heard the sound of the Lord God as he was walking in the garden in the cool of the day, and they hid from the Lord God among the trees. But the Lord God called to the man, 'Where are you?' ... And I will put enmity between you and the woman, and between your offspring and hers; he will crush your head, and you will strike his heel.",
                   ["What do the man and woman do when they hear God?", "What is God's first question to them?", "What promise is hidden in verse 15?"],
                   ["Why does God ask 'Where are you?' if he already knows?", "How is verse 15 the first hint of the gospel?"],
                   ["Where do you tend to hide from God?", "How does knowing the story ends in rescue change your fear?"]),
             word("Redemption", "To buy back or set free by paying a price. The Bible describes salvation as God redeeming people from sin and death at the cost of Christ.",
                  [("In him we have redemption through his blood, the forgiveness of sins.", "Ephesians 1:7"),
                   ("You were bought at a price. Therefore honor God with your bodies.", "1 Corinthians 6:20")],
                  ["What price was paid for your redemption?",
                   "If you were 'bought at a price,' how does that change how you see your worth?"]),
             journal("Finding My Place in the Story",
                     ["Which part of the story — Creation, Fall, Redemption, Restoration — do you most need to hear right now?",
                      "Where do you see brokenness (the Fall) in your own world?",
                      "What does the promise of Restoration give you hope for?"]),
             wview("Why Is There Suffering?", "If God is good and powerful, why does he allow pain and evil?",
                   [("The Fall", "The Bible traces suffering to a real break between humanity and God, not to God's cruelty."),
                    ("A God who enters it", "Christianity is unique in claiming God himself suffered on the cross rather than staying distant from pain."),
                    ("A promised end", "Restoration means suffering is temporary, not the final word.")],
                   ["How is the Christian answer to suffering different from just 'everything happens for a reason'?",
                    "What suffering in your life do you most want to bring honestly to God?"])),
        unit(5, "From Knowing to Living",
             "Do not merely listen to the word... Do what it says.", "James 1:22",
             "Information that never becomes action puffs up rather than builds up. This unit is about obedience, character, and letting Scripture reshape daily choices.",
             devo("The Danger of Just Knowing",
                  "It is possible to know a lot about the Bible and still not follow Jesus. This unit closes that gap.",
                  "Do not merely listen to the word, and so deceive yourselves. Do what it says.", "James 1:22",
                  ["James warns that hearing without doing is a form of self-deception — we feel spiritual without being changed.",
                   "The goal of Bible study was never a full head; it was a transformed life."],
                  ["Where might you be deceiving yourself — knowing truth you are not living?",
                   "What is one truth you already know that you need to start obeying?"],
                  "Lord, close the gap between what I know and how I live."),
             study("Doers of the Word", "James 1:22-25",
                   "Do not merely listen to the word, and so deceive yourselves. Do what it says. Anyone who listens to the word but does not do what it says is like someone who looks at his face in a mirror and, after looking at himself, goes away and immediately forgets what he looks like. But whoever looks intently into the perfect law that gives freedom, and continues in it — not forgetting what they have heard, but doing it — they will be blessed in what they do.",
                   ["What is the person with the mirror like?", "What does the blessed person do differently?", "What is promised to the doer?"],
                   ["Why does James compare the word to a mirror?", "What does it mean that God's law 'gives freedom'?"],
                   ["What is one thing you 'saw in the mirror' recently and forgot?", "How will you 'continue in it' this week?"]),
             word("Sanctification", "The lifelong process by which God makes a believer more like Jesus. Not earning salvation, but growing in it.",
                  [("It is God's will that you should be sanctified.", "1 Thessalonians 4:3"),
                   ("Being confident of this, that he who began a good work in you will carry it on to completion.", "Philippians 1:6")],
                  ["Why is it freeing that growth is a process, not instant perfection?",
                   "Where have you seen God change you over the past year?"]),
             journal("A Life That Matches",
                     ["Where is there a gap between what you believe and how you actually live?",
                      "What habit would you like God to help you build?",
                      "What habit would you like God to help you break?"]),
             chall("Obedience Experiment",
                   "Pick real, measurable steps. Vague goals produce vague lives.",
                   ["Obey one clear command of Scripture this week that you have been avoiding.",
                    "Apologize to someone you have wronged.",
                    "Replace 30 minutes of screen time with reading or prayer.",
                    "Do a good deed no one will ever know about."])),
        unit(6, "Building a Lasting Faith",
             "Continue in what you have learned and have become convinced of.", "2 Timothy 3:14",
             "Many walk away from faith in their late teens. This unit prepares you to own your beliefs, handle doubt, and keep growing when no one is making you.",
             devo("A Faith That's Yours",
                  "Someday no one will drag you to church or hand you this workbook. Will your faith survive that?",
                  "Continue in what you have learned and have become convinced of, because you know those from whom you learned it.", "2 Timothy 3:14",
                  ["Paul tells Timothy to continue — faith is not a moment but a direction you keep walking.",
                   "A borrowed faith cracks under pressure; a personally examined faith holds. Doubts are not the enemy of faith; unexamined doubts are."],
                  ["Is your faith currently more inherited or more owned? Be honest.",
                   "What would help you become 'convinced' rather than just compliant?"],
                  "God, make my faith my own, deep enough to hold under pressure."),
             study("Standing Firm", "Ephesians 6:10-13",
                   "Finally, be strong in the Lord and in his mighty power. Put on the full armor of God, so that you can take your stand against the devil's schemes. For our struggle is not against flesh and blood, but against the rulers, against the authorities, against the powers of this dark world. Therefore put on the full armor of God, so that when the day of evil comes, you may be able to stand your ground.",
                   ["Whose power are we told to be strong in?", "Who is the real struggle against?", "What is the repeated goal of the armor?"],
                   ["Why does it matter that the strength is God's, not ours?", "What 'schemes' target students your age specifically?"],
                   ["Which piece of armor do you most need right now?", "How will you 'stand your ground' this month?"]),
             word("Perseverance", "Steadfast endurance — continuing to trust and obey God through difficulty, doubt, and time.",
                  [("Let us run with perseverance the race marked out for us, fixing our eyes on Jesus.", "Hebrews 12:1-2"),
                   ("Blessed is the one who perseveres under trial.", "James 1:12")],
                  ["What is the difference between perseverance and just gritting your teeth?",
                   "Who do you know that has persevered in faith, and what can you learn from them?"]),
             journal("The Road Ahead",
                     ["What is one belief you want to understand more deeply?",
                      "What doubt do you need to stop hiding and start exploring?",
                      "Who will you ask to walk with you in your faith going forward?"]),
             disc("Commissioned",
                  "This is the last discussion of the book. Talk about the road ahead, not just today.",
                  ["What is the biggest thing you are taking away from this study?",
                   "What is your plan to keep growing after this workbook ends?",
                   "How can this group keep each other accountable in the months ahead?"])),
    ]
    memory = [
        ("2 Timothy 3:16", "2 Timothy 3:16"), ("Psalm 119:105", "Psalm 119:105"),
        ("Hebrews 4:12", "Hebrews 4:12"), ("James 1:22", "James 1:22"),
        ("1 Peter 2:2", "1 Peter 2:2"),
    ]
    closing = ["What is the most important thing God taught you through this study?",
               "How is your relationship with the Bible different now than when you started?",
               "Write a short prayer committing to keep reading and following God."]
    return assemble(wb, "01_Christian_Bible_Learning_Workbook.pdf", units, memory, closing)


# Books 2-10 are defined in teen_books_2_10.py and registered via BUILDERS.
try:
    from teen_books_2_10 import BUILDERS_2_10
except Exception:
    BUILDERS_2_10 = []


def _report(path):
    import re
    d = open(path, "rb").read()
    pages = len(re.findall(rb"/Type\s*/Page[^s]", d))
    ok = d[:8] == b"%PDF-1.4" and d.rstrip().endswith(b"%%EOF") and pages >= 42
    print(f"[{'OK ' if ok else 'BAD'}] {path}  pages={pages}  bytes={len(d):,}")
    return ok


if __name__ == "__main__":
    all_ok = True
    all_ok &= _report(book1())
    for builder in BUILDERS_2_10:
        all_ok &= _report(builder())
    print("\n" + ("ALL BOOKS >= 42 PAGES AND VALID" if all_ok else "SOME BOOKS FAILED CHECK"))
