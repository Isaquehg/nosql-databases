from teachercrud import TeacherCRUD

crud = TeacherCRUD()

# Create
crud.create("Chris Lima", 1956, "189.052.396-66")

# Retrieve
print(crud.retrieve("Chris Lima"))
# ['Chris Lima']

# Update CPF
crud.update("Chris Lima", "189.052.777-77")