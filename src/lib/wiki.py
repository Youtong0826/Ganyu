import wikipedia

def wiki_search(*keywords: str, lang: str = "zh"):
    if keywords == None: return None
    wikipedia.set_lang(lang)
    
    return wikipedia.search(keywords)

def wiki_info(title: str = None, sentences: int = 1, lang: str = "zh"):
    if not title:
        return None
    
    wikipedia.set_lang(lang)
    
    try: 
        return wikipedia.summary(title, sentences=sentences)
    
    except: 
        return None