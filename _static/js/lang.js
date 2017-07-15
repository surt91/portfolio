function init_language() {
    var lang = localStorage.getItem("language");

    if (lang == "de") {
        window.location.replace("de/");
    } else if (lang=="en") {
        window.location.replace("en/");
    } else {
        // nothing known saved, guess language
        var userLang = navigator.language || navigator.userLanguage;
        if (userLang.substring(0, 1).toLowerCase() == "de") {
            window.location.replace("de/");
        } else {
            window.location.replace("en/");
        }
    }
}

function switch_language_de() {
    localStorage.setItem("language", "de");
}

function switch_language_en() {
    localStorage.setItem("language", "en");
}
