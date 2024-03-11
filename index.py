from dotenv import load_dotenv
import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
from tqdm import *
import requests
import math
import json 
import re

# ---------------------------------------------SETUP CREDS--------------------------------------------------------------------------------------#
load_dotenv()

passo = os.environ["passo"]
mail = os.environ["mail"]

# ---------------------------------------------CHROME--------------------------------------------------------------------------------------#
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://elearning.unimib.it/enrol/index.php?id=37059
    page.goto("https://elearning.unimib.it/enrol/index.php?id=43161")

    # Click text=Continua
    # page.locator("text=Continua").click()
    # expect(page).to_have_url("https://elearning.unimib.it/login/index.php")

    # Click #unimibsaml_0 >> text=Login
    # with page.expect_navigation(url="https://idp-idm.unimib.it/idp/profile/SAML2/Redirect/SSO?execution=e1s2"):
    with page.expect_navigation():
        page.locator("#unimibsaml_0 >> text=Login").click()
    # expect(page).to_have_url("https://idp-idm.unimib.it/idp/profile/SAML2/Redirect/SSO?execution=e1s1")

    # Click [placeholder="Inserisci il tuo nome utente"]
    page.locator("[placeholder=\"Inserisci il tuo nome utente\"]").click()

    # Fill [placeholder="Inserisci il tuo nome utente"]
    page.locator("[placeholder=\"Inserisci il tuo nome utente\"]").fill(mail)

    # Click [placeholder="Inserisci la password"]
    page.locator("[placeholder=\"Inserisci la password\"]").click()

    # Fill [placeholder="Inserisci la password"]
    page.locator("[placeholder=\"Inserisci la password\"]").fill(passo)

    # Click button:has-text("Accesso")
    # with page.expect_navigation(url="https://elearning.unimib.it/course/view.php?id=37059"):
    with page.expect_navigation():
        page.locator("button:has-text(\"Accedi\")").click()
    # expect(page).to_have_url("https://idp-idm.unimib.it/idp/profile/SAML2/Redirect/SSO?execution=e1s2")


    # link setup: https://cdnapisec.kaltura.com/p/2351962/sp/235196200/playManifest/entryId/1_td1796t4/flavorIds/1_lnq9ip5m,1_pmo9dxb7,1_dkyxkcoi/format/applehttp/protocol/https/a.m3u8?referrer=aHR0cHM6Ly9rYWYuZWxlYXJuaW5nLnVuaW1pYi5pdA==&ks=djJ8MjM1MTk2Mnz4fq4V7_XQ4OEkHa6KMnjZnhyCeTjRF9X-uARSAUUQ408Cv0xhe_QxgZQMkcCTlc5OIIM5G_Ms8OeY33IDtNoda5ufED7Ul-fr4knDHwrAIdW_cAXF4wqkHM7vk7o6UZPT0XUiQRwBEroFQYiCak39dml4i28ACi1x7DUc_YfclDBS6qk_FoyJefoyKwmrez38FeE5p3HzBiVqnp9N9gtgLZcvzmuMHp6Wy7YBaUPlT0LQ8I2N-RQn23r1qfN1sQ-LLWD2TqYxQg5JMfhmlG05vLaNEvLea1NQaWzsdrJRTVz0cIcTXCxNbX8eIWlPcvxM5-95oVoSHwikuru0MgfKfpoNcDebOvU2Tc6eMug23moBilZJEiy07EdUAVMcPbBZuGz6j4a7VTI44b5EGq4aJ-vgqPqZSnS9bTsbWDti5Z5bMRAb2SPql-tJPFP7G7jZ2FDcSMGsL-gSYX2ley0j2DqspTmSmm-J_QmTFCRWkQ==&playSessionId=9c62e8a8-3031-5ca4-f60b-f39d830d3842&clientTag=html5:v2.85&playbackContext=231418223&uiConfId=46495023

    # --------------------------------------------------------------------SETUP JSON---------------------------------------------------------------------------
    
    # creating folders for each course if they don't exist
    f = open('all_courses_20202021.json')
    listaLink = json.load(f)

    for x in listaLink:
        try:
            os.makedirs("./video/" + x.get('course'))
        except FileExistsError:
            print("Directory already exists")
            pass
    f.close()
    
    linkRotti = []
    f = open('out_links.json')
    listaLink = json.load(f)
    # ^^^ ma il json è vuoto, prova a dumparci roba prima 

    #--------------------------------------------------------------------LAVORAZIONE LINK---------------------------------------------------------------------

    print("\n-----------------INIZIO LOGGING UTILI-----------------------\n")

    for x in listaLink:
        try:
            page.goto(x.get('link'))
            html = page.content()
            nomeCartella = x.get('course')['name']
            x = html.index("entryid%2F")
            entryid = html[x + 10 : x + 20]
            link = (
                "http://cdnbakmi.kaltura.com/p/2351962/sp/2351962/playManifest/entryId/"
                + entryid
                + "/flavorParamId/0/format/url/protocol/http/a.mp4"
            )
            nome = html.split("title>")[1].replace("</", "")
            # titolo = "./video/" + nomeCartella + "/" + html.split("title>")[1].replace("</", "").replace("Ã", "").replace("/", "_").replace('\\', "").replace(":", "").replace("\"", "").replace("'", "").replace("|", "") + ".mp4"
            # faccio un replace di tutti i caratteri che non vanno bene per il nome del file meno ingombranti possibile 

            # regex carina by Koalas 
            titolo = "./video/" + nomeCartella + "/" + re.sub("[\\/:*?\"<>|]", "", html.split("title>")[1]).strip() + ".mp4"
            
            # progress bar (ft. Depa)
            with requests.get(link, stream=True) as r:
                if r.status_code != 404:
                    r.raise_for_status()
                    with open(titolo, "wb") as p:
                        for chunk in tqdm(
                            r.iter_content(chunk_size=1000000),
                            total=math.ceil(
                                int(r.headers.get("content-length", 0)) // 1000000
                            ),
                            unit="MB",
                        ):
                            if chunk:  
                                p.write(chunk)
                else: 
                    print("Error 404 :C go mimir: " + link)

            print("Scaricato: " + nome + "\n")
        except Exception as error:
            print("Video broke or private, skipping to the next one ", error)
            linkRotti.append(x)
    f.close()
    context.close()
    browser.close()

    # svuoto file json link dato che sono stati tutti scaricati
    open('out_links.json', 'w').close()

    # Se ci sono link rotti, li dumpo in un file json
    if len(linkRotti) > 0:
        f = open('brokenLinks.json', 'w')
        json.dump(linkRotti, f, indent=2)
        f.close()
    
    
    print("\n--------------------Addios----------------------------------\n")


with sync_playwright() as playwright:
    run(playwright)
