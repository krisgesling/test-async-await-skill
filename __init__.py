import asyncio
import time

from mycroft import MycroftSkill, intent_handler


class TestAsyncAwait(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('await.async.test.intent')
    def handle_await_async_test(self, message):
        async def sleep():
            self.log.info(f'Time: {time.time() - start:.2f}')
            await asyncio.sleep(1)

        async def sum(name, numbers):
            total = 0
            for number in numbers:
                self.log.info(f'Task {name}: Computing {total}+{number}')
                await sleep()
                total += number
            self.log.info(f'Task {name}: Sum = {total}\n')

        start = time.time()

        # We cannot access any existing loop because each Skill runs in it's
        # own thread. So the usual approach below does not work.
        # loop = asyncio.get_event_loop()
        
        # Instead we can create a new loop for our Skill's dedicated thread.
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        tasks = [
            loop.create_task(sum("A", [1, 2])),
            loop.create_task(sum("B", [1, 2, 3])),
        ]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()

        end = time.time()
        duration = "{:.2f}".format(end - start)
        self.log.info(f'Time taken: {duration} sec')

        self.speak_dialog('await.async.test', {'duration': duration})


def create_skill():
    return TestAsyncAwait()

