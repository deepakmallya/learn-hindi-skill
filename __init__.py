from mycroft import MycroftSkill, intent_file_handler


class LearnHindi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hindi.learn.intent')
    def handle_hindi_learn(self, message):
        self.speak_dialog('hindi.learn')


def create_skill():
    return LearnHindi()

