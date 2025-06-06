from property_renting_bot.property_bot import PropertyBot

if __name__ == "__main__":
    bot = PropertyBot()
    bot.run_scraping()
    bot.run_auto_filler()