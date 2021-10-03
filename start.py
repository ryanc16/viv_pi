from vivpi.main import Main
import config

app = Main(config.SYSTEM_CONFIG)
try:
  app.onStart()
except KeyboardInterrupt:
  print()
  app.onStop()