def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
    
print(greet('en'),'Will')

print(greet('es'),'Jelly')

print(greet('fr'),'Sally')