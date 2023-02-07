import textwrap

story = '''You are an adventurous traveler, who has always wanted to explore the world. One day, you decide you are going to take on the ultimate challenge and try to find the elusive and mysterious diamond of the sky.

You set off on your journey, traveling to the first airport on your list. When you arrived, you were greeted with a message on the airport's display board that said "Welcome to X Airport! You have X$ and Xkm of range left."

You are determined to find the diamond, and you know you need money and range to do so. You decide to try your luck and open a lootbox at the airport. Much to your surprise, you win a great reward- money! You are ecstatic and now have the funds to continue on your journey.

With your newfound wealth, you are able to continue on your journey, but you have to be careful with your money and range. You are able to purchase fuel at each airport, and you eventually make it to the airport where the diamond is rumored to be.

Much to your surprise, when you arrive, you see the diamond shining in the sunlight. You have finally found the diamond!

You are elated, but you know you have to be careful as you make your way back to the starting airport. You have heard rumors that robbers are prowling around the airports, hoping to steal money and valuable items. As you make your way back, you are careful to not fall victim to any of their schemes.

When you finally arrive back at the starting airport, you are relieved to find that you still have the diamond and all the money you won along the way. You have won the challenge!

You are overjoyed with your success and the money you have won. You have finally found the diamond of the sky and were able to keep all of your hard-earned money.

'''

# Set column width to 80 characters
wrapper = textwrap.TextWrapper(width=80, break_long_words=False, replace_whitespace=False)
# Wrap text
word_list = wrapper.wrap(text=story)


def getStory():
    return word_list
