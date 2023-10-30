import streamlit as st
st.set_page_config(page_title="Books", page_icon=":book:")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Data Science Books')
st.write('Recommended by Ana Beatriz Macedo')
st.caption('Click on the books for more details.')
books = [
     {
        "title": "Data Science para negócios: Do entendimento à aplicação",
        "amazon_link": "https://www.amazon.com.br/Data-Science-para-neg%C3%B3cios-pensamento-ebook/dp/B07HQTW1X6?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=29PG54CN75EVA&keywords=data+science+books&qid=1698677326&s=digital-text&sprefix=data+science+boo%2Cdigital-text%2C261&sr=1-3&linkCode=li2&tag=anamacedo06-20&linkId=49080f2d2768c8aa1f3bbb16fd4449ce&language=pt_BR&ref_=as_li_ss_il",
        "image_src": "//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07HQTW1X6&Format=_SL160_&ID=AsinImage&MarketPlace=BR&ServiceVersion=20070822&WS=1&tag=anamacedo06-20&language=pt_BR",
        "tracking_image_src": "https://ir-br.amazon-adsystem.com/e/ir?t=anamacedo06-20&language=pt_BR&l=li2&o=33&a=B07HQTW1X6"
    },
    {
        "title": "Storytelling com Dados: Um guia para profissionais de análise de dados",
        "amazon_link": "https://www.amazon.com.br/Storytelling-com-Dados-visualiza%C3%A7%C3%A3o-profissionais-ebook/dp/B0851R57ZL?pd_rd_w=daz9n&content-id=amzn1.sym.a6b2045c-97ef-4110-af35-a6f988be578c&pf_rd_p=a6b2045c-97ef-4110-af35-a6f988be578c&pf_rd_r=ED8HG7SPD0VZRP9HFGQJ&pd_rd_wg=KJQu3&pd_rd_r=3b86ac5c-f7eb-4bfe-abbb-7bb69a351c03&pd_rd_i=B0851R57ZL&psc=1&linkCode=li2&tag=anamacedo06-20&linkId=9ea5c598b6cb3dff7cdb782f7266c042&language=pt_BR&ref_=as_li_ss_il",
        "image_src": "//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0851R57ZL&Format=_SL160_&ID=AsinImage&MarketPlace=BR&ServiceVersion=20070822&WS=1&tag=anamacedo06-20&language=pt_BR",
        "tracking_image_src": "https://ir-br.amazon-adsystem.com/e/ir?t=anamacedo06-20&language=pt_BR&l=li2&o=33&a=B0851R57ZL"
    },
    {
        "title": "Estatística: O que é, para que serve, como funciona",
        "amazon_link": "https://www.amazon.com.br/Estat%C3%ADstica-para-serve-como-funciona-ebook/dp/B01D209XHK?pd_rd_w=OiH9g&content-id=amzn1.sym.0f6fcb32-d08e-42cd-a81a-deaaada04787&pf_rd_p=0f6fcb32-d08e-42cd-a81a-deaaada04787&pf_rd_r=N8952BXWDH6G1ATGXTWF&pd_rd_wg=YPrgy&pd_rd_r=326e8eef-4032-45a1-83e0-75c4f48e785c&pd_rd_i=B01D209XHK&psc=1&linkCode=li2&tag=anamacedo06-20&linkId=43c953624cec7d9ecf48ad06ea6a5097&language=pt_BR&ref_=as_li_ss_il",
        "image_src": "//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B01D209XHK&Format=_SL160_&ID=AsinImage&MarketPlace=BR&ServiceVersion=20070822&WS=1&tag=anamacedo06-20&language=pt_BR",
        "tracking_image_src": "https://ir-br.amazon-adsystem.com/e/ir?t=anamacedo06-20&language=pt_BR&l=li2&o=33&a=B01D209XHK"
    },
    {
        "title": "Machine Learning: Guia de Referência Rápida com Scikit-Learn e TensorFlow",
        "amazon_link": "https://www.amazon.com.br/Machine-Learning-Scikit-Learn-TensorFlow-English-ebook/dp/B0BHCFNY9Q?&linkCode=li2&tag=anamacedo06-20&linkId=613acd87ae1415f83b2a28bb72820adf&language=pt_BR&ref_=as_li_ss_il",
        "image_src": "//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0BHCFNY9Q&Format=_SL160_&ID=AsinImage&MarketPlace=BR&ServiceVersion=20070822&WS=1&tag=anamacedo06-20&language=pt_BR",
        "tracking_image_src": "https://ir-br.amazon-adsystem.com/e/ir?t=anamacedo06-20&language=pt_BR&l=li2&o=33&a=B0BHCFNY9Q"
    },
    {
        "title": "An Introduction to Statistical Learning: with Applications in R",
        "amazon_link": "https://www.amazon.com.br/Introduction-Statistical-Learning-Applications-Statistics-ebook/dp/B09BHG37HZ?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3C9RUR4R8FK1O&keywords=introduction+to+statistical+learning&qid=1698677483&s=digital-text&sprefix=introdutdcion+to+statstical+learni+%2Cdigital-text%2C215&sr=1-1&linkCode=li2&tag=anamacedo06-20&linkId=a36f4990604498e553766f0ba378f882&language=pt_BR&ref_=as_li_ss_il",
        "image_src": "//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B09BHG37HZ&Format=_SL160_&ID=AsinImage&MarketPlace=BR&ServiceVersion=20070822&WS=1&tag=anamacedo06-20&language=pt_BR",
        "tracking_image_src": "https://ir-br.amazon-adsystem.com/e/ir?t=anamacedo06-20&language=pt_BR&l=li2&o=33&a=B09BHG37HZ"
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
