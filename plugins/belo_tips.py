import random

from petercord import petercord, Message
userge = petercord 

@petercord.on_cmd("belo", about={
    'header': "Get a Logical Quote",
    'petercord': "{tr}belo"}, allow_via_bot=False)
async def being_logical(message: Message):
    raw_list = await userge.get_history("@BeingLogical")
    raw_message = random.choice(raw_list)
    await message.edit(raw_message.text)


@petercord.on_cmd("tips", about={
    'header': "Get a Pro Tip",
    'petercord': "{tr}tips"}, allow_via_bot=False)
async def pro_tips(message: Message):
    raw_list = await petercord.get_history("@Interesting_Knowledge")
    try:
        raw_message = random.choice(raw_list)
        pru_text = raw_message.text
        while "Pro Tip" not in pru_text:
            raw_message = random.choice(raw_list)
            pru_text = raw_message.text
        await message.edit(pru_text)
    # None Type Error 😴🙃
    except Exception:
        await message.edit("I Ran Out of Tips.")
