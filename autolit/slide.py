import altair as alt

class SlideShow:
 
    
    def __init__(self, charts: list, html: str, css:str, js: str) -> None:

        self.charts = charts
        self.html = html
        self.css = css
        self.js = js
    
    def create(self):
        slides = ''' '''
        for i in range(len(self.charts)):
            slides += \
        f'''
        <div class="mySlides fade">
        <div class="numbertext">{i+1} / {len(self.charts)}</div>
        <div id="vis{i+1}"></div>
        </div>
        '''

        dots = ''' '''
        for i in range(len(self.charts)):
            dots += \
        f'''
        <span class="dot" onclick="currentSlide({i+1})"></span> 
        '''

        embedings = ''' '''
        for i in range(len(self.charts)):
            embedings += \
        f'''
        vegaEmbed('#vis{i+1}', {self.charts[i].to_json(indent=None)}).catch(console.error);
        ''' 
        
        
        html = self.html
        css = self.css
        js = self.js
        
        html = html.format(
            css_styler=css,
            vega_version=alt.VEGA_VERSION,
            vegalite_version=alt.VEGALITE_VERSION,
            vegaembed_version=alt.VEGAEMBED_VERSION,
            slides=slides,
            dots=dots,
            slide_script=js,
            embedings=embedings
        )
        
        return html