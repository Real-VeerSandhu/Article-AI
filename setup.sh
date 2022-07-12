mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
[theme]\n\
base=\"light\"\n\
primaryColor=\"#00A200\"\n\
secondaryBackgroundColor=\"#F0F2F6\"\n\
textColor=\"#000000\"\n\
\n\
" > ~/.streamlit/config.toml