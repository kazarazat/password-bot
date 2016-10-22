# password-bot
A rivescript based chatbot that generates, validates and saves passwords.
I entered this bot in the 2016 VentureBeat Botathon and it is an excellent demonstration
of using advanced python objects inside of the [@AiChaos](https://github.com/aichaos) Rivescript scripting language.
If you're not familiar with Rivescript check it out [here](https://github.com/aichaos/rivescript-python)

# Functionality
**Generating**

    You> gimme a password
    Password Bot> what kind? regular, strong or a passphrase
    You> passphrase
    Password Bot> here you go my friend: manifestly-human-accusatrixes

**Validating**

    You> is this password strong?
    Password Bot> show me (type or copy it)
    You> p4ssWord
    Password Bot> could be stronger if you added: symbols, more characters
    
**Saving**

    You> can you save a password?
    Password Bot> sure. type 'nickname and password' just like this
    You> facebook and &jh$$fRt101
    Password Bot> saved nickname facebook and password &jh$$fRt101 are you done?
    
**Knowledge**

    You> tell me about rainbow tables
    Password Bot> Here's what I know: A rainbow table is a precomputed table for reversing 
    cryptographic hash functions, usually for cracking password hashes. Tables are usually 
    used in recovering a plaintext password up to a certain length consisting of a 
    limited set of characters.
    

# Python Objects
Rivescript supports python and javascript objects that can be executed inside the running chatbot.
The power and flexibility of this in my opinion surpasses what can be done with plain AIML.
    
    > object phrase python
	      import random
	      import sys
	      import string

	      dict_file = "eg/US.txt"
	      n_dict = open(dict_file).read().splitlines()
	
	      def pass_gen(size, phrases=n_dict):
		        return ''.join(random.choice(phrases)+'-' for _ in range(size))
	      passphrase = str(pass_gen(3))
	
	      return passphrase[:-1]
    < object

# Implementation
Run the chatbot in the terminal
       
       $ python password_bot.py
       
or try the twillio / flask app that comes with Rivescript.
Point to the correct directory of .rive files and test it out

    from flask import Flask, request, redirect
    from rivescript import RiveScript
    import twilio.twiml

    bot = RiveScript()
    bot.load_directory(
      os.path.join(os.path.dirname(__file__), "..", "brain")
    )
    bot.sort_replies()

    app = Flask(__name__)

    @app.route("/twilio", methods=["GET", "POST"])
    def hello_rivescript():
        """Receive an inbound SMS and send a reply from RiveScript."""

        from_number = request.values.get("From", "unknown")
        message     = request.values.get("Body")
        reply       = "(Internal error)"

        # Get a reply from RiveScript.
        if message:
            reply = bot.reply(from_number, message)

        # Send the response.
        resp = twilio.twiml.Response()
        resp.message(reply)
        return str(resp)

    if __name__ == "__main__":
        app.run(host='127.0.0.0', debug=True)
