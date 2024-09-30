async def progress_bar(current, total, reply, start):
    if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return
        else:
            perc = f"{current * 100 / total:.1f}%"
            elapsed_time = round(diff)
            speed = current / elapsed_time
            remaining_bytes = total - current
            if speed > 0:
                eta_seconds = remaining_bytes / speed
                eta = hrt(eta_seconds, precision=1)
            else:
                eta = "-"
            sp = str(hrb(speed)) + "/s"
            tot = hrb(total)
            cur = hrb(current)

            # Calculate progress bar dots
            bar_length = 11
            completed_length = int(current * bar_length / total)
            remaining_length = bar_length - completed_length
            progress_bar = "▰" * completed_length + "▱" * remaining_length

            # Choose sticker based on progress
            sticker = "alexwa_by_fStikBot"  # Replace this with the actual sticker ID
            if completed_length == bar_length:
                sticker = "alexwa_by_fStikBot"  # Final sticker when upload is complete
            elif completed_length > 0:
                sticker = "alexwa_by_fStikBot"  # Sticker for in-progress

            try:
                await reply.edit(f'`╭──⌈📤 𝙐𝙥𝙡𝙤𝙖𝙙𝙞𝙣𝙜 📤⌋──╮ \n├{progress_bar}\n├ 𝙎𝙥𝙚𝙚𝙙 : {sp} \n├ 𝙋𝙧𝙤𝙜𝙧𝙚𝙨𝙨 : {perc} \n├ 𝙇𝙤𝙖𝙙𝙚𝙙 : {cur}\n├ 𝙎𝙞𝙯𝙚 :  {tot} \n├ 𝙀𝙏𝘼 : {eta} \n╰────⌈ 🇨‌ 🇴‌ 🇻 🇮 🇩 ⌋────╯`\n')
                await reply.reply_sticker(sticker)  # Send the sticker
            except FloodWait as e:
                time.sleep(e.x)
