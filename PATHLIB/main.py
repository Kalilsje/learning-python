from pathlib import Path
diret = Path("folder1")
#diret = diret.absolute()
#print(diret.root)
#print(diret.parent)
#print(list(diret.parents))
#print(diret.parts)
#diret = diret / "test22.txt"
#print(diret.touch())
#diret.unlink()

#diret = diret / "Text1.txt"
#print(diret.read_text())
#diret.write_text("anfubasyuhfas")
#print(diret.read_text())

#diret = diret / "test1.txt"
#new_filename = "test22"
#renamed_file = diret.with_stem(new_filename)
#diret.rename(renamed_file)

diret = diret / "folder12"
diret.mkdir()