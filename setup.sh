mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
[theme]\n\
base=\"light\"\n\
primaryColor=\"#c15bbf\"\n\
secondaryBackgroundColor=\"#dcdcdc\"\n\
textColor=\"#000000\"\n\
\n\
" > ~/.streamlit/config.toml