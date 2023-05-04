import spacy


def englishifier(text):
    nlp = spacy.load("en_core_web_sm")

    # text = "[Pre-Chorus]\nThough that I'll the way I amaint to know\nLet it goes not your own, feel so call and see this are way\nTo see me know you sleep at me going and know\nHow long, I m in this sow you\n\n[Chorus: Ed Sheeran]\nI don't wanna know you're my baby\nI'll never lead you no"

    doc = nlp(text)

    corrected_text = ""
    for token in doc:
        if token.is_alpha and not token.is_stop:
            corrected_text += token.text_with_ws.capitalize()
        else:
            corrected_text += token.text_with_ws

    corrected_text = corrected_text.strip().replace(" i ", " I ")

    return (corrected_text)
