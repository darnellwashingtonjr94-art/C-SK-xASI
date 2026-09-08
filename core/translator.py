import re

class PivotTranslator:
    """Low-latency Hanja/Hangul/Mandarin pivot translation layer."""
    
    def __init__(self):
        self.hanja_map = {"韓": "한", "中": "중", "國": "국", "智": "지", "能": "능"}

    async def pivot_to_target(self, text: str, target_lang: str) -> str:
        if target_lang == "ko":
            return self._hanja_to_hangul(text)
        elif target_lang == "zh":
            return text  # Passthrough/transformation logic
        return text

    def _hanja_to_hangul(self, text: str) -> str:
        for hanja, hangul in self.hanja_map.items():
            text = text.replace(hanja, hangul)
        return text
