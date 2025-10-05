from django.shortcuts import render, get_object_or_404

# Hardcoded announcements data
announcements = [
    {
        'id': 1,
        'title': '🍵 TeaTime Just Dropped!',
        'date': 'Yesterday',
        'content': "Hey bestie 👋 TeaTime is now live — your go-to spot for campus updates, class tea, and lowkey important stuff. We’re keeping it short, sweet, and scrollable. No cap.",
        'full_content': "Hey bestie 👋 TeaTime is now live — your go-to spot for campus updates, class tea, and lowkey important stuff. We’re keeping it short, sweet, and scrollable. No cap.\n\n🔔 What’s brewing this week?\n\nMidterm schedules are out (don’t ghost your exams)\n\nOrg fair this Friday — come thru!\n\nNew prof just joined the CS dept (👀)\n\nClick any headline to sip the full story. And yeah, we’ve got a “Read more” toggle because we know your attention span is on TikTok time.\n\nStay steeped. Stay informed. — TeaTime"
    },
    {
        'id': 2,
        'title': TeaTime Merch Incoming',
        'date': 'Today',
        'content': "Big drip alert 🚨 We’re dropping limited-edition TeaTime merch next week — hoodies, mugs, and stickers that scream ‘I read announcements unironically.’",
        'full_content': "Big drip alert 🚨 We’re dropping limited-edition TeaTime merch next week — hoodies, mugs, and stickers that scream ‘I read announcements unironically.’\n\n🧵 Details:\n\nPre-orders open Monday at 9 AM\n\nFirst 50 get a free sticker pack\n\nWanna see the designs? Click ‘Read more’ and get the full tea. Don’t sleep on this — it’s giving cozy, it’s giving campus-core.\n\n— TeaTime"
    },
    {
        'id': 3,
        'title': 'Maintenance Notice',
        'date': '2023-10-10',
        'content': 'Scheduled maintenance will occur on October 15th from 2 AM to 4 AM.',
        'full_content': 'Scheduled maintenance will occur on October 15th from 2 AM to 4 AM. During this time, the site may be unavailable. We apologize for any inconvenience. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    },
    {
        'id': 4,
        'title': 'TeaTime is now live',
        'date': '2023-10-15',
        'content': 'Hey bestie 👋 TeaTime is now live — your go-to spot for campus updates, class tea, and lowkey important stuff. We’re keeping it short, sweet, and scrollable. No cap.',
        'full_content': 'Hey bestie 👋 TeaTime is now live — your go-to spot for campus updates, class tea, and lowkey important stuff. We’re keeping it short, sweet, and scrollable. No cap.\n\n🔔 What’s brewing this week?\n\nMidterm schedules are out (don’t ghost your exams)\n\nOrg fair this Friday — come thru!\n\nNew prof just joined the CS dept (👀)\n\nClick any headline to sip the full story. And yeah, we’ve got a “Read more” toggle because we know your attention span is on TikTok time.\n\nStay steeped. Stay informed. — TeaTime Team'
    }
]

def home(request):
    return render(request, 'home.html')

def announcements_list(request):
    return render(request, 'announcements.html', {'announcements': announcements})

def announcement_detail(request, id):
    announcement = get_object_or_404(announcements, id=id)
    return render(request, 'announcement_detail.html', {'announcement': announcement})


