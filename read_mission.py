from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized

ENGLISH = ("Clean House Initiative aims to connect landlords with people who are looking for temporary jobs and potentially" +
"housing as well. The website matches landlords with candidate cleaners for their apartments, and landlords can" +
"then choose to rent to their cleaner. Each landlord and candidate also has a record of their hiring/cleaning" +
"history that serves as a reference for the matching process." +
"The goals of the initiative include:" +
"Provide local landlords with employees who can clean their apartments and improve hygiene of the surrounding" + 
"neighborhood as a result." +
"Provide people without permanent residence with a platform to find a job, which can potentially serve as" + 
"a way to find an apartment to rent.")


SPANISH = ("Declaración de Objetivos Fundamentales" +
"La Iniciativa de Casas Limpias aspira a conectar a los dueños y las personas que buscan para un trabajo temporal y" +
"potencialmente un lugar para vivir también. Este sitio crea parejas de dueño y limpiador, y los dueños pueden decidir" +
"alquilar su apartamento a sus limpiadores. Cada dueño y candidato que usa este sitio tendrá su propria historia" + 
"de contratación que serve como referencia para el process de crear las parejas." +
"Las metas de esta iniciativa incluyen:" +
"Ofrecer los dueños locales con empleados que puede limpiar sus apartamentos y mejorar la higiene del barrio." +
"Ofrecer la gente sin una residencia permanente con un sitio que le ayuda buscar para un trabajo, que potencialmente" +
"servirá como una manera de encontrar una casa para vivir.")

synthesis_input_en = texttospeech.types.SynthesisInput(text=ENGLISH)
synthesis_input_es = texttospeech.types.SynthesisInput(text=SPANISH)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice_en = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
    
voice_es = texttospeech.types.VoiceSelectionParams(
    language_code='es-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response_en = client.synthesize_speech(synthesis_input_en, voice_en, audio_config)
response_es = client.synthesize_speech(synthesis_input_es, voice_es, audio_config)

# The response's audio_content is binary.
with open('out_en.mp3', 'wb') as out_en:
    # Write the response to the output file.
    out_en.write(response_en.audio_content)

with open('out_es.mp3', 'wb') as out_es:
    # Write the response to the output file.
    out_es.write(response_es.audio_content)
