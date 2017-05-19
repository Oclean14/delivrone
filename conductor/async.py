import asyncio

def slow_square(x):
   f = asyncio.Future()

   def resolve():
      f.set_result(x * x)

   loop = asyncio.get_event_loop()
   loop.call_later(1, resolve)
   return f

def test():
   f = slow_square(3)

   def done(f):
      res = f.result()
      print(res)

   f.add_done_callback(done)
   return f

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()