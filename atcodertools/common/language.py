import re
from typing import Pattern, Callable

from atcodertools.codegen.code_generators import cpp, java
from atcodertools.tools.templates import get_default_template_path


class LanguageNotFoundError(Exception):
    pass


class Language:

    def __init__(self,
                 name: str,
                 display_name: str,
                 extension: str,
                 submission_lang_pattern: Pattern[str],
                 default_code_generator: Callable[['CodeGenArgs'], str],
                 default_template_path: str,
                 ):
        self.name = name
        self.display_name = display_name
        self.extension = extension
        self.submission_lang_pattern = submission_lang_pattern
        self.default_code_generator = default_code_generator
        self.default_template_path = default_template_path

    @classmethod
    def from_name(cls, name: str):
        for l in ALL_LANGUAGES:
            if l.name == name:
                return l
        raise LanguageNotFoundError(
            "No language support for '{}'".format(ALL_LANGUAGE_NAMES))


CPP = Language(
    name="cpp",
    display_name="C++",
    extension="cpp",
    submission_lang_pattern=re.compile(".*C\\+\\+14 \\(GCC.*"),
    default_code_generator=cpp.main,
    default_template_path=get_default_template_path('cpp'),
)

JAVA = Language(
    name="java",
    display_name="Java",
    extension="java",
    submission_lang_pattern=re.compile(".*Java8.*"),
    default_code_generator=java.main,
    default_template_path=get_default_template_path('java'),
)

RUST = Language(
    name="rust",
    display_name="Rust",
    extension="rs",
    submission_lang_pattern=re.compile(".*Rust \\(1.*"),
    default_code_generator=java.main,
    default_template_path=get_default_template_path('rs'),
)

ALL_LANGUAGES = [CPP, JAVA, RUST]
ALL_LANGUAGE_NAMES = [lang.display_name for lang in ALL_LANGUAGES]
