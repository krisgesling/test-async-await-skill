from mycroft import MycroftSkill, intent_file_handler


class TestAsyncAwait(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('await.async.test.intent')
    def handle_await_async_test(self, message):
        self.speak_dialog('await.async.test')


def create_skill():
    return TestAsyncAwait()

