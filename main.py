from js import document

def generate_message(event=None):
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    output = document.getElementById("output")
    output.innerHTML = ""

    if not name or not age or not school:
        output.innerText = "⚠️ Please fill in all fields before generating your profile."
        return

    note = f"📌 Notes:\n{name} is currently {age} years old and studies at {school}.\nThis message includes escape characters like \"quotes\" and a tab:\tSee?"

    profile = f"""
🎓 Student Profile
─────────────────────────────
Name   : {name}
Age    : {age}
School : {school}///////////////////

{note}
   """

    output.innerText = profile

def setup(event=None):
    button = document.getElementById("generate-btn")
    button.addEventListener("click", generate_message)

    output = document.getElementById("output")
    output.innerText = "👉 Fill out the form and click 'Generate Message' to see your profile here."

document.addEventListener("DOMContentLoaded", setup)
