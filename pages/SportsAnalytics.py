import streamlit as st
st.set_page_config(page_title="Books", page_icon=":book:")
st.title('Sports Analytics Books')
st.text('Recommended by Ana Beatriz Macedo')
st.caption('Click on the books for more details.')

books = [
    {
        "title": "Moneyball: The Art of Winning an Unfair Game",
        "amazon_link": "https://www.amazon.com.br/Moneyball-Winning-Unfair-Game-English-ebook/dp/B000RH0C8G?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1RZ9H5CM8YU6J&keywords=moneyball&qid=1698675809&s=digital-text&sprefix=moneybal%2Cdigital-text%2C295&sr=1-2&linkCode=li2&tag=anamacedo06-20&linkId=43474854d6ab33b8672ef32b23b1b2be&language=pt_BR&ref_=as_li_ss_il",
        "image_src": "//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B000RH0C8G&Format=_SL160_&ID=AsinImage&MarketPlace=BR&ServiceVersion=20070822&WS=1&tag=anamacedo06-20&language=pt_BR",
        "tracking_image_src": "https://ir-br.amazon-adsystem.com/e/ir?t=anamacedo06-20&language=pt_BR&l=li2&o=33&a=B000RH0C8G"
    },
    {
        "title": "Soccermatics: Mathematical Adventures in the Beautiful Game",
        "amazon_link": "https://www.amazon.com.br/Soccermatics-Mathematical-Adventures-Beautiful-Bloomsbury-ebook/dp/B01AIB7YKE?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1VTFAFFBYFRUX&keywords=soccermatics&qid=1698676384&s=digital-text&sprefix=soccermatic%2Cdigital-text%2C267&sr=1-1&linkCode=li2&tag=anamacedo06-20&linkId=58ae429c5c947672557d747c66775329&language=pt_BR&ref_=as_li_ss_il",
        "image_src": "//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B01AIB7YKE&Format=_SL160_&ID=AsinImage&MarketPlace=BR&ServiceVersion=20070822&WS=1&tag=anamacedo06-20&language=pt_BR",
        "tracking_image_src": "https://ir-br.amazon-adsystem.com/e/ir?t=anamacedo06-20&language=pt_BR&l=li2&o=33&a=B01AIB7YKE"
    },
    {
        "title": "Football Hackers: The Science and Art of a Data Revolution",
        "amazon_link": "https://www.amazon.com.br/Football-Hackers-Science-Revolution-English-ebook/dp/B0CCYQ9K5D?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1TALKROEIWW08&keywords=football+hackers&qid=1698676649&s=digital-text&sprefix=football+hacker%2Cdigital-text%2C267&sr=1-1&linkCode=li2&tag=anamacedo06-20&linkId=d993aaff015b533de8a799e5e2810e4c&language=pt_BR&ref_=as_li_ss_il",
        "image_src": "//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0CCYQ9K5D&Format=_SL160_&ID=AsinImage&MarketPlace=BR&ServiceVersion=20070822&WS=1&tag=anamacedo06-20&language=pt_BR",
        "tracking_image_src": "https://ir-br.amazon-adsystem.com/e/ir?t=anamacedo06-20&language=pt_BR&l=li2&o=33&a=B0CCYQ9K5D"
    },
    {
        "title": "Betaball: How Silicon Valley and Science Built One of the Greatest Basketball Teams in History",
        "amazon_link": "https://www.amazon.com.br/Betaball-Silicon-Science-Greatest-Basketball-ebook/dp/B071CK11X9?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=7BWJLR69OQOL&keywords=beta+ball&qid=1698676681&s=digital-text&sprefix=beta+bal%2Cdigital-text%2C374&sr=1-4&linkCode=li2&tag=anamacedo06-20&linkId=742698f92a72747c78ad6ef945c69f2d&language=pt_BR&ref_=as_li_ss_il",
        "image_src": "//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B071CK11X9&Format=_SL160_&ID=AsinImage&MarketPlace=BR&ServiceVersion=20070822&WS=1&tag=anamacedo06-20&language=pt_BR",
        "tracking_image_src": "https://ir-br.amazon-adsystem.com/e/ir?t=anamacedo06-20&language=pt_BR&l=li2&o=33&a=B071CK11X9"
    },
    {
        "title": "Thinking Basketball: What Is, and Isn't, a Smart Play",
        "amazon_link": "https://www.amazon.com.br/Thinking-Basketball-English-Ben-Taylor-ebook/dp/B072KM9BJN?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=36642YNKXXKHT&keywords=thinking+basketball&qid=1698676718&s=digital-text&sprefix=thinking+basketbal%2Cdigital-text%2C226&sr=1-1&linkCode=li2&tag=anamacedo06-20&linkId=2a97b67bd52b8625f41a6814316b0aab&language=pt_BR&ref_=as_li_ss_il",
        "image_src": "//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B072KM9BJN&Format=_SL160_&ID=AsinImage&MarketPlace=BR&ServiceVersion=20070822&WS=1&tag=anamacedo06-20&language=pt_BR",
        "tracking_image_src": "https://ir-br.amazon-adsystem.com/e/ir?t=anamacedo06-20&language=pt_BR&l=li2&o=33&a=B072KM9BJN"
    },
    {
        "title": "Mathletics: How Gamblers, Managers, and Sports Enthusiasts Use Mathematics in Baseball, Basketball, and Football",
        "amazon_link": "https://www.amazon.com.br/Mathletics-Gamblers-Managers-Mathematics-English-ebook/dp/B09KP3ZCVL?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2SLVN1QR9695Q&keywords=mathletics&qid=1698676950&s=digital-text&sprefix=mathletics%2Cdigital-text%2C270&sr=1-1&linkCode=li2&tag=anamacedo06-20&linkId=3478e2d4da8c94ce55c21c81cb0111bc&language=pt_BR&ref_=as_li_ss_il",
        "image_src": "//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B09KP3ZCVL&Format=_SL160_&ID=AsinImage&MarketPlace=BR&ServiceVersion=20070822&WS=1&tag=anamacedo06-20&language=pt_BR",
        "tracking_image_src": "https://ir-br.amazon-adsystem.com/e/ir?t=anamacedo06-20&language=pt_BR&l=li2&o=33&a=B09KP3ZCVL"
    },
    {
        "title": "Expected Goals: The Philosophy and Methods of Game-Changing Football Analytics",
        "amazon_link": "https://www.amazon.com.br/Expected-Goals-Philosophy-Game-Changing-Analysing-ebook/dp/B0815ZLX3B?pd_rd_w=U7cQt&content-id=amzn1.sym.a6b2045c-97ef-4110-af35-a6f988be578c&pf_rd_p=a6b2045c-97ef-4110-af35-a6f988be578c&pf_rd_r=YFV2E00NW85PMA9T7FM6&pd_rd_wg=Bkl50&pd_rd_r=ac958696-9980-4bc3-bd1c-13142aa0629d&pd_rd_i=B0815ZLX3B&psc=1&linkCode=li2&tag=anamacedo06-20&linkId=8f60daff25c514204b097e7a12991fb0&language=pt_BR&ref_=as_li_ss_il",
        "image_src": "//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0815ZLX3B&Format=_SL160_&ID=AsinImage&MarketPlace=BR&ServiceVersion=20070822&WS=1&tag=anamacedo06-20&language=pt_BR",
        "tracking_image_src": "https://ir-br.amazon-adsystem.com/e/ir?t=anamacedo06-20&language=pt_BR&l=li2&o=33&a=B0815ZLX3B"
    }
]

for book in books:
    html_code = f'''
    <h2>{book['title']}</h2>
    <a href="{book['amazon_link']}" target="_blank">
        <img border="0" src="{book['image_src']}">
    </a>
    <img src="{book['tracking_image_src']}" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    '''
    st.markdown(html_code, unsafe_allow_html=True)
