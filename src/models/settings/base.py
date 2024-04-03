class Whatever:
    def __enter__(self):
      print('Starting...')
    
    def __exit__(self, exc_type, exc_value, exc_tb):
      print('Finished...')

with Whatever() as hello:
    print("Hiiiii, I'm here...")