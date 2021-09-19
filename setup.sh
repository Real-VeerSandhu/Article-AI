mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
[theme]\n\
primaryColor=\"#5b81c1\"\n\
backgroundColor=\"#eeebe8\"\n\
secondaryBackgroundColor=\"#dcdcdc\"\n\
textColor=\"#000000\"\n\
\n\
" > ~/.streamlit/config.toml