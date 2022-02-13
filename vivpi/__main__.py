from vivpi.app import App
import config

app = App(config.SYSTEM_CONFIG)
try:
  app.onStart()
except KeyboardInterrupt:
  print()
  app.onStop()