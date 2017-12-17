# magic_8_ball.rb: Responds with a random answer to the user's question.
# Project found on https://www.redd.it/29aqox

answers = [
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes, definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy; try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don\'t count on it.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Very doubtful.']

loop do
    print 'What do you wish to know? '
    gets
    puts 'Thinking...'
    sleep 2
    puts answers.sample
    print 'Do you wish to continue (Y/n)? '
    break if gets.strip.downcase[0] == 'n'
    puts
end
