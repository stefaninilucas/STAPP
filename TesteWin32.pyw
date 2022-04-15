import win32com.client

acad = win32com.client.Dispatch("AutoCAD.Application")

doc = acad.ActiveDocument  # Document object

x = doc.Utility.GetEntity()

x[0].color = 1
x[0].copy()

z = doc.Utility.GetEntity()
p = z[0].IntersectWith(x[0], 0)

y = doc.Utility.GetPoint()
doc.Utility.prompt(y[0])

doc.sendcommand("zoom all ")


# iterate trough all objects (entities) in the currently opened drawing
# and if its a BlockReference, display its attributes and some other things.
for entity in acad.ActiveDocument.ModelSpace:
    name = entity.EntityName
    if name == 'AcDbBlockReference':
        HasAttributes = entity.HasAttributes
        if HasAttributes:
            print(entity.Name)
            print(entity.Layer)
            print(entity.ObjectID)
            for attrib in entity.GetAttributes():
                print("  {}: {}".format(attrib.TagString, attrib.TextString))

                # update text
                attrib.TextString = 'modified with python'
                attrib.Update()