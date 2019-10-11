from peewee import Model

class BaseModel(Model):

  def __str__(self):
    r = {}
    for k in self.__data__.keys():
      try:
         r[k] = str(getattr(self, k))
      except:
         r[k] = json.dumps(getattr(self, k))
    return str(r)
