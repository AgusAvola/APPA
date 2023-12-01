import datetime
pastillasactuales=2
pastillas=3
now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
print(now)
now=now.split(':')
now= now[0]+":"+now[1]
print(now)