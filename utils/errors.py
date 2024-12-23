def api_url_error(url):
    if not url:
        raise ValueError("A variável de ambiente API_URL não está definida ou não foi carregada.")