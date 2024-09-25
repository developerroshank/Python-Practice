import pywhatkit as pw

txt = """Hello My Name is Roshan
Kumar
"""

pw.text_to_handwriting(txt, "demo.png", [0, 0, 138])

print("End")
