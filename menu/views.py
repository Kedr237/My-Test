from django.shortcuts import render
from .models import MenuModel

def menuView(request, name=None):
  objects = MenuModel.objects
  context = {
    'allMenu': objects.all,
    'selected': name,
    'parents': [],
    'childrens': [],
  }

  # get parents
  try:
    el = objects.get(name=name)
    parents = [el.parent]
    i = 0
    while parents[i].parent:
      parents.append(parents[i].parent)
      i += 1
    context['parents'] = parents
  except:
    pass

  # get children
  try:
    childrens = getChildrens(objects, el)
    context['childrens'] = childrens
  except:
    pass

  return render(request, 'index.html', context)


def getChildrens(objects, el):
  all_childrens = []
  childrens = objects.filter(parent=el)
  all_childrens.extend(childrens)
  for child in childrens:
    all_childrens.extend(getChildrens(objects, child))

  return all_childrens